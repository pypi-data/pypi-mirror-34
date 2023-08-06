#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
    @file:      response.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @auther:    Tangmi(tangmi360@gmail.com)
    @date:      June 21, 2018
    @desc:      Response class
"""


class Response(object):

    def __init__(self):
        self._headers = None
        self._status = None
        self._data = None
        self._meta = {}

    @property
    def meta(self):
        return self._meta

    @meta.setter
    def meta(self, meta):
        if isinstance(meta, dict):
            self._meta = meta

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, headers):
        self._headers = headers

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data
