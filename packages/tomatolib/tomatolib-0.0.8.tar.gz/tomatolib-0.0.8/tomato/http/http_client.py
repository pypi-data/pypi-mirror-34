#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
    @file:      http_client.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @auther:    Tangmi(tangmi360@gmail.com)
    @date:      June 11, 2018
    @desc:      Basic http client functions
"""

import json
import aiohttp
import asyncio
import logging
import async_timeout

from tomato.utils import singleton
from tomato.http.request import Request
from tomato.http.response import Response


@singleton
class HttpClient(object):

    def __init__(self, max_pool_size=0, limit_per_host=0,
                 dummy_cookie=False):
        self._loop = asyncio.get_event_loop()
        self._headers = {'Accept-Encoding': 'gzip,deflate'}
        self._cookie_jar = None
        if dummy_cookie:
            self._cookie_jar = aiohttp.helper.DummyCookieJar()
        self._connector = aiohttp.TCPConnector(limit=max_pool_size,
                                               limit_per_host=limit_per_host)
        self._session = aiohttp.ClientSession(loop=self._loop, connector_owner=True,
                                              connector=self._connector,
                                              headers=self._headers,
                                              cookie_jar=self._cookie_jar)

    async def get(self, url, params=None, cookies=None,
                  headers=None, resp_type='text', timeout=10):
        # TODO cookies field not used
        async with async_timeout.timeout(timeout):
            async with self._session.get(url=url, params=params,
                                         headers=headers) as resp:
                response = await self._parse_response(resp, resp_type)
                return response

    async def post(self, url, params=None, data=None,
                   cookies=None, headers=None,
                   resp_type='text', timeout=10):
        # TODO cookies field not used
        async with async_timeout.timeout(timeout):
            async with self._session.post(url, params=params,
                                          headers=headers,
                                          data=data) as resp:
                response = await self._parse_response(resp, resp_type)
                return response

    async def _parse_response(self, resp, resp_type):
        response = Response()
        response.headers = resp.headers
        response.status = resp.status
        if 'text' == resp_type:
            response.data = await resp.text()
        return response

    async def close(self):
        await self._session.close()
