#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
    @file:      redis_client.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @auther:    Tangmi(tangmi360@gmail.com)
    @date:      June 11, 2018
    @desc:      Redis storage access class
"""

import logging
import asyncio
import aioredis

from tomato.utils import singleton


@singleton
class RedisClient(object):

    async def _create_pool(self):
        loop = asyncio.get_event_loop()
        redis_uri = 'redis://%s:%s' % (self._host, self._port)
        self._pool_dict = {}
        for db in self._db:
            pool = await aioredis.create_redis_pool(redis_uri,
                                                    db=int(db),
                                                    password=self._passwd,
                                                    minsize=self._minsize,
                                                    maxsize=self._maxsize,
                                                    loop=loop)
            self._pool_dict[int(db)] = pool
            logging.info('Redis Client Connecting to %s?db=%s', redis_uri, db)

    def __init__(self, host=None, port=None,
                   passwd=None, db='0',
                   minsize=None, maxsize=None):
        self._host = host
        self._port = port
        
        if passwd is None or len(passwd.strip()) == 0:
            self._passwd = None
        else:
            self._passwd = passwd

        self._minsize = minsize
        self._maxsize = maxsize
        self._db = db.split(',')

        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._create_pool())

    async def close(self):
        if hasattr(self, '_pool_dict'): # TODO 临时方案，待资源管理重构后处理
            for db in self._pool_dict:
                self._pool_dict[db].close()
                await self._pool_dict[db].wait_closed()

    async def rpop(self, key, db=0):
        """rpop
        """
        result = await self._pool_dict[db].rpop(key)
        return result

    async def exists(self, key, db=0):
        """exists
        """
        result = await self._pool_dict[db].exists(key)
        return result

    async def set(self, key, value, db=0):
        """set
        """
        result = await self._pool_dict[db].set(key, value)
        return result

    async def get(self, key, db=0):
        """get
        """
        result = await self._pool_dict[db].get(key)
        return result

    async def lpop(self, key, db=0):
        """lpop
        """
        result = await self._pool_dict[db].lpop(key)
        return result

    async def blpop(self, key, db=0, timeout=0):
        """blpop
        """
        result = await self._pool_dict[db].blpop(key, timeout)
        return result

    async def brpop(self, key, db=0, timeout=0):
        """brpop
        """
        result = await self._pool_dict[db].brpop(key, timeout)
        return result

    async def rpush(self, key, value, db=0):
        """rpush
        """
        result = await self._pool_dict[db].rpush(key, value)
        return result

    async def lpush(self, key, value, db=0):
        """lpush
        """
        result = await self._pool_dict[db].lpush(key, value)
        return result

    async def sadd(self, key, value, db=0):
        """sadd
        """
        result = await self._pool_dict[db].sadd(key, value)
        return result

    async def smembers(self, key, db=0):
        """smembers
        """
        result = await self._pool_dict[db].smembers(key)
        return result

    async def srem(self, key, value, db=0):
        """srem
        """
        result = await self._pool_dict[db].srem(key, value)
        return result

    async def bitop(self, op, dest, key, db=0):
        """bitop
        """
        result = await self._pool_dict[db].bitop(op, dest, key)
        return result

    async def bitcount(self, key, db=0):
        """bitcount
        """
        result = await self._pool_dict[db].bitcount(key)
        return result

    async def delete(self, key, db=0):
        """delete
        """
        result = await self._pool_dict[db].delete(key)
        return result

    async def zadd(self, key, value, score, db=0):
        """zadd
        """
        result = await self._pool_dict[db].zadd(key, value, score)
        return result

    async def zrem(self, key, member, db=0):
        """zrem
        """
        result = await self._pool_dict[db].zrem(key, member)
        return result

    async def sismember(self, key, value, db=0):
        """sismember
        """
        result = await self._pool_dict[db].sismember(key, value)
        return result

    async def zrangebyscore(self, key, min, max, db=0, withscores=False):
        """zrangebyscore
        """
        result = await self._pool_dict[db].zrangebyscore(name=key, min=min,
                                                         max=max, withscores=withscores)
        return result

    async def zincrby(self, key, member, incrment, db=0):
        """zincrby
        """
        result = await self._pool_dict[db].zincrby(key, member, incrment)
        return result

    async def hset(self, key, field, value, db=0):
        """hset
        """
        result = await self._pool_dict[db].hset(key, field, value)
        return result

    async def hsetnx(self, key, field, value, db=0):
        """hsetnx
        """
        result = await self._pool_dict[db].hsetnx(key, field, value)
        return result

    async def hget(self, key, field, db=0):
        """hget
        """
        result = await self._pool_dict[db].hget(key, field)
        return result
    
    async def hmget(self, key, field, db=0):
        """hmget
        """
        result = await self._pool_dict[db].hmget(key, field)
        return result

    async def hdel(self, key, field, db=0):
        """hdel
        """
        result = await self._pool_dict[db].hdel(key, field)
        return result
        
    async def llen(self, key, db=0):
        """llen
        """
        result = await self._pool_dict[db].llen(key)
        return result

    async def hlen(self, key, db=0):
        """hlen
        """
        result = await self._pool_dict[db].hlen(key)
        return result

    async def scard(self, key, db=0):
        """scard
        """
        result = await self._pool_dict[db].scard(key)
        return result

    async def zcard(self, key, db=0):
        """zcard
        """
        result = await self._pool_dict[db].zcard(key)
        return result
    
    async def lrange(self, key, start, end, db=0):
        """lrange
        """
        result = await self._pool_dict[db].lrange(key, start, end)
        return result
