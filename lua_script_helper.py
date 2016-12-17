#!/usr/bin/env python
# -*-coding:utf-8-*-

import redis


class LuaRedisHelper(object):

    def __init__(self, redis_conf, lua_script_path):
        self.redis_client = redis.StrictRedis(
            host=redis_conf.get("host", "localhost"),
            port=redis_conf.get("port", 6379), db=0)
        self.lua_script = open(lua_script_path).read()
        self.multiply = self.redis_client.register_script(self.lua_script)

    def multiply_excete(self, keys=list(), args=list()):
        return self.multiply(keys=keys, args=args)





