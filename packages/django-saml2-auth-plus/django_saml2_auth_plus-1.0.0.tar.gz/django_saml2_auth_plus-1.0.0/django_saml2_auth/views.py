#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django_saml2_auth.conf import get_saml_client
from django_saml2_auth.utils import get_reverse, get_sp_domain
from saml2 import (
    BINDING_HTTP_POST,
    BINDING_HTTP_REDIRECT,
    entity,
)
from saml2.client import Saml2Client
from saml2.config import Config as Saml2Config

from django import get_version
from pkg_resources import parse_version
from django.conf import settings
from django.contrib.auth.models import (User, Group)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.template import TemplateDoesNotExist
from django.http import HttpResponseRedirect
from django.utils.http import is_safe_url

try:
    import urllib2 as _urllib
except:
    import urllib.request as _urllib
    import urllib.error
    import urllib.parse

if parse_version(get_version()) >= parse_version('1.7'):
    from django.utils.module_loading import import_string
else:
    from django.utils.module_loading import import_by_path as import_string


def denied(r):
    return render(r, 'django_saml2_auth/denied.html')


@csrf_exempt
def acs(r):
    saml_client = get_saml_client(get_sp_domain(r))
    resp = r.POST.get('SAMLResponse', None)
    next_url = r.session.get('login_next_url', settings.SAML2_AUTH.get('DEFAULT_NEXT_URL'))

    if not resp:
        return HttpResponseRedirect(get_reverse(['denied', 'django_saml2_auth:denied']))

    authn_response = saml_client.parse_authn_request_response(
        resp, entity.BINDING_HTTP_POST)
    if authn_response is None:
        return HttpResponseRedirect(get_reverse(['denied', 'django_saml2_auth:denied']))

    entity_id = authn_response.issuer()
    if entity_id is None:
        return HttpResponseRedirect(get_reverse(['denied', 'django_saml2_auth:denied']))

    attributes_for_entity = settings.SAML2_AUTH['ATTRIBUTES_MAP'].get(entity_id, {})
    if not attributes_for_entity:
        return HttpResponseRedirect(get_reverse(['denied', 'django_saml2_auth:denied']))

    identifier = attributes_for_entity["UNIQUE_IDENTIFIER"]

    if attributes_for_entity.get("USE_NAME_ID", False):
        name_id = authn_response.name_id
        if name_id is None:
            return HttpResponseRedirect(get_reverse(['denied', 'django_saml2_auth:denied']))

        unique_kwarg = {identifier: name_id.text}

    else:
        user_identity = authn_response.get_identity()
        if user_identity is None:
            return HttpResponseRedirect(get_reverse(['denied', 'django_saml2_auth:denied']))

        unique_kwarg = {identifier: user_identity[identifier][0]}

    target_user = None
    try:
        target_user = User.objects.get(**unique_kwarg)
        if settings.SAML2_AUTH.get('TRIGGER', {}).get('BEFORE_LOGIN', None):
            import_string(settings.SAML2_AUTH['TRIGGER']['BEFORE_LOGIN'])(user_identity)
    except User.DoesNotExist:
        return HttpResponseRedirect(get_reverse(['denied', 'django_saml2_auth:denied']))

    r.session.flush()

    if target_user.is_active:
        target_user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(r, target_user)
    else:
        return HttpResponseRedirect(get_reverse(['denied', 'django_saml2_auth:denied']))

    return HttpResponseRedirect(next_url)


def signin(r):
    try:
        import urlparse as _urlparse
        from urllib import unquote
    except:
        import urllib.parse as _urlparse
        from urllib.parse import unquote
    next_url = r.GET.get('next', settings.SAML2_AUTH.get('DEFAULT_NEXT_URL', get_reverse('admin:index')))

    try:
        if 'next=' in unquote(next_url):
            next_url = _urlparse.parse_qs(_urlparse.urlparse(unquote(next_url)).query)['next'][0]
    except:
        next_url = r.GET.get('next', settings.SAML2_AUTH.get('DEFAULT_NEXT_URL', get_reverse('admin:index')))

    # Only permit signin requests where the next_url is a safe URL
    if not is_safe_url(next_url):
        return HttpResponseRedirect(get_reverse(['denied', 'django_saml2_auth:denied']))

    r.session['login_next_url'] = next_url

    # Allow the requester to select the IDP they want to use. Required if multiple IDPs are configured.
    selected_idp = r.GET.get('idp', None)

    saml_client = get_saml_client(get_sp_domain(r))
    idps = saml_client.config.metadata.identity_providers()

    if selected_idp is None and len(idps) > 1:
        # TODO: Explain that idp selection is required
        return HttpResponseRedirect(get_reverse(['denied', 'django_saml2_auth:denied']))

    _, info = saml_client.prepare_for_authenticate(entityid=selected_idp)

    redirect_url = None

    for key, value in info['headers']:
        if key == 'Location':
            redirect_url = value
            break

    return HttpResponseRedirect(redirect_url)


def signout(r):
    logout(r)
    return render(r, 'django_saml2_auth/signout.html')
