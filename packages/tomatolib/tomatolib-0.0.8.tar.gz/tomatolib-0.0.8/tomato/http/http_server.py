#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
    @file:      http_server.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @auther:    Tangmi(tangmi360@gmail.com)
    @date:      June 11, 2018
    @desc:      Basic http server functions and router rules encapsulation
"""

import json
import signal
import logging
import asyncio
import functools
from aiohttp import web

from tomato.utils import util
from tomato.utils import singleton


@singleton
class HttpServer(object):

    def __init__(self, host, port):
        self._loop = asyncio.get_event_loop()
        self._host = host
        self._port = int(port)
        self._handlers = {'/': self.default_handler}

    async def default_handler(self, request):
        req_params = request.query
        response = 'Welcome to tomato'
        return response

    def init_handler(self, conf_file=None):
        logging.info('init handlers...')
        conf = util.load_conf(conf_file)
        secs = conf.sections()
        for sec in secs:
            handler = conf.get(sec, 'name')
            router = conf.get(sec, 'router')
            module_name = '.'.join(handler.split('.')[0:-1])
            class_name = handler.split('.')[-1]
            cls_obj = util.gen_object(module_name=module_name, class_name=class_name)
            for attr in dir(cls_obj):
                # 加载非__前缀的属性
                if attr[0] != '_':
                    # 获取导入obj方法。
                    class_attr_obj = getattr(cls_obj, attr)
                    # 判断类属性是否为函数
                    if hasattr(class_attr_obj, '__call__'):
                        # TODO 未判断函数是否有装饰器
                        # TODO 尾段如果是{}未做处理
                        # TODO (\w+)的正则匹配判断
                        abs_router = router
                        handler_name = router.split('/')[-1]
                        if '(' in router and ')' in router:
                            begin_idx = router.index('(')
                            end_idx = router.index(')')
                            replace_str = router[begin_idx:end_idx+1]
                            abs_router = router.replace(replace_str, attr)
                            handler_name = attr

                        if attr == 'setup':
                            logging.info('execute call[%s:%s]', handler, attr)
                            self._loop.run_until_complete(class_attr_obj())
                        elif attr == handler_name:
                            if abs_router not in self._handlers:
                                self._handlers[abs_router] = class_attr_obj
                                logging.info('init router info: router[%s--->%s:%s]',
                                             abs_router, handler, handler_name)
                            else:
                                logging.warning('duplicate router configuration: '
                                                'router[%s--->%s:%s]',
                                                abs_router, handler, handler_name)

        logging.info('handler initialization is complete')

    @web.middleware
    async def data_codec(self, request, handler):
        """http简单解包与封包
           1.qs信息从request.query属性中直接获取（MultiDictProxy类型）
           2.http body内容如果请求头为content_type=application/json,
             则通过json标准库进行解析，并覆盖request.body，
             否则直接把body内容抛到业务层自行处理（默认是byte类型）
           3.对于response的处理，目前简单判断为dict则直接转成json格式str发给调用端
             否则直接按业务层返回值返回给调用端
        """
        request.body = None
        if request.body_exists and request.can_read_body:
            request.body = await request.content.read()
            if request.content_type == 'application/json':
                try:
                    request.body = json.loads(request.body)
                except Exception as e:
                    logging.warning('json format warning, errmsg[%s]', str(e))
                    return web.json_response({'ret': 0, 'msg': 'params error'})
        response = await handler(request)
        if isinstance(response, dict):
            return web.json_response(response)
        else:
            return web.Response(body=response)

    async def init_server(self):
        self._app = web.Application(middlewares=[self.data_codec,])

        for router in self._handlers:
            self._app.router.add_route('*', router, self._handlers[router])

        self._runner = web.AppRunner(self._app)
        await self._runner.setup()
        site = web.TCPSite(self._runner, self._host, self._port)
        await site.start()
        logging.info('serving on [%s]', site.name)

    async def start(self):
        await self.init_server()

    async def close(self):
        await self._runner.cleanup()
        await self._app.shutdown()
        await self._app.cleanup()
