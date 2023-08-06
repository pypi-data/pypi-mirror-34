#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
    @file:      request.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @auther:    Tangmi(tangmi360@gmail.com)
    @date:      June 21, 2018
    @desc:      Request class
"""


class Request(object):

    def __init__(self, url):
        self._url = url
        self._meta = {}

    @property
    def url(self):
        return self._url

    @property
    def meta(self):
        return self._meta

    @meta.setter
    def meta(self, meta):
        if isinstance(meta, dict):
            self._meta = meta
