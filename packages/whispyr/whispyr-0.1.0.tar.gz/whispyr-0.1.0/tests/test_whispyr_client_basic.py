# -*- coding: utf-8 -*-

"""Tests for `whispyr` package"""

import base64

import httpretty
from httpretty import HTTPretty

import pytest
import re

import whispyr
from whispyr import ClientError, WhispirRetry

httpretty.HTTPretty.allow_net_connect = False


TEST_USERNAME = 'U53RN4M3'
TEST_PASSWORD = 'P4ZZW0RD'
TEST_API_KEY = 'V4L1D4P1K3Y'


@pytest.fixture(params=[{'retry': WhispirRetry()}])
def whispir(request):
    params = request.param
    return whispyr.Whispir(TEST_USERNAME, TEST_PASSWORD, TEST_API_KEY,
                           **params)


@httpretty.activate
def test_basic_auth(whispir):
    httpretty.register_uri(httpretty.GET, re.compile(r'.*', re.M), body='{}')
    whispir.request('get', 'workspaces')

    assert httpretty.has_request()
    request = httpretty.last_request()
    assert 'Authorization' in request.headers
    basic_auth = request.headers['Authorization']
    expected_basic = _basic_auth(TEST_USERNAME, TEST_PASSWORD)
    assert basic_auth == expected_basic


@httpretty.activate
def test_api_key_provided(whispir):
    httpretty.register_uri(httpretty.GET, re.compile(r'.*', re.M), body='{}')
    whispir.request('get', 'workspaces')

    assert httpretty.has_request()
    request = httpretty.last_request()
    assert 'apikey' in request.querystring
    api_key = request.querystring['apikey'][0]
    assert api_key == TEST_API_KEY


@httpretty.activate
def test_user_agent_is_set(whispir):
    httpretty.register_uri(httpretty.GET, re.compile(r'.*', re.M), body='{}')
    whispir.request('get', 'workspaces')

    assert httpretty.has_request()
    request = httpretty.last_request()
    assert 'User-Agent' in request.headers
    expexted_agent = 'whispyr/{}'.format(whispyr.__version__)
    assert request.headers['User-Agent'] == expexted_agent


@httpretty.activate
def test_retry_succeeded(whispir):
    qps_headers = {
        'X-Mashery-Error-Code': 'ERR_403_DEVELOPER_OVER_QPS',
        'X-Mashery-Error-Detail': 'Account Over Queries Per Second Limit',
        'Retry-After': 1
    }

    qps_response = HTTPretty.Response(
        body='', status=403, adding_headers=qps_headers)

    httpretty.register_uri(
        httpretty.GET, re.compile(r'.*', re.M),
        responses=[
            qps_response,
            qps_response,
            HTTPretty.Response(body='{}', status=200),
        ]
    )

    assert whispir.request('get', 'workspaces') == {}


@httpretty.activate
@pytest.mark.parametrize('whispir', [{'retry': WhispirRetry(total=1)}],
                         indirect=True)
def test_retry_limit(whispir):
    qps_headers = {
        'X-Mashery-Error-Code': 'ERR_403_DEVELOPER_OVER_QPS',
        'X-Mashery-Error-Detail': 'Account Over Queries Per Second Limit',
        'Retry-After': 1
    }

    qps_response = HTTPretty.Response(
        body='', status=403, adding_headers=qps_headers)

    httpretty.register_uri(
        httpretty.GET, re.compile(r'.*', re.M),
        responses=[
            qps_response,
            qps_response,
            qps_response,
            HTTPretty.Response(body='{}', status=200),
        ]
    )

    with pytest.raises(ClientError) as excinfo:
        whispir.request('get', 'workspaces')

    exc = excinfo.value
    assert exc.response.status_code == 403


@httpretty.activate
def test_do_not_retry_qpd(whispir):
    qps_headers = {
        'X-Mashery-Error-Code': 'ERR_403_DEVELOPER_OVER_QPD',
        'X-Mashery-Error-Detail': 'Account Over Queries Per Day Limit',
        'Retry-After': 20 * 60 * 60  # 20 hours in seconds
    }

    httpretty.register_uri(
        httpretty.GET, re.compile(r'.*', re.M),
        responses=[
            HTTPretty.Response(
                body='', status=403, adding_headers=qps_headers),
            HTTPretty.Response(body='{}', status=200),
        ]
    )

    with pytest.raises(ClientError) as excinfo:
        whispir.request('get', 'workspaces')

    exc = excinfo.value
    assert exc.response.status_code == 403


@httpretty.activate
def test_no_retry_for_forbidden(whispir):
    httpretty.register_uri(
        httpretty.GET, re.compile(r'.*', re.M),
        responses=[
            HTTPretty.Response(body='', status=403),
            HTTPretty.Response(body='{}', status=200),
        ]
    )

    with pytest.raises(ClientError) as excinfo:
        whispir.request('get', 'workspaces')

    exc = excinfo.value
    assert exc.response.status_code == 403


def _basic_auth(username, password):
    username = username.encode('latin1')
    password = password.encode('latin1')
    b64auth = base64.b64encode(b':'.join((username, password)))
    return 'Basic {}'.format(b64auth.decode('utf-8'))
