#!/usr/bin/env python2
import logging
import ssl
import sys
import urllib
import urllib2


def calculate_cookies(headers):
    cookies = ''
    for one_header in headers:
        cookies += one_header.split(' ')[1]
    return cookies


class NoRedirect(urllib2.HTTPRedirectHandler):

    def http_error_302(self, req, fp, code, msg, headers):
        page = fp.read()
        cookies = calculate_cookies(fp.headers.headers)
        return code, cookies, page


def test_request_with_date(url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    cookies = ''

    opener = urllib2.build_opener(urllib2.HTTPSHandler(context=ctx), NoRedirect())

    body = {'username': 'test', 'password': 'test'}
    data = urllib.urlencode(body)
    req_one = urllib2.Request(url, data=data)
    req_one.add_header('Cookie', cookies)

    response = opener.open(req_one)
    return response


def test_request(url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    opener = urllib2.build_opener(urllib2.HTTPSHandler(context=ctx), NoRedirect())
    response = opener.open(url)

    return response


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)

    url = sys.argv[1]
    test_request(url)
    test_request_with_date(url)

