#!/usr/bin/env python
# -*-coding:utf-8-*-

from lua_script_helper import LuaRedisHelper


if __name__ == "__main__":
    redis_conf = {}
    lua_redis_helper = LuaRedisHelper(
        redis_conf=redis_conf, lua_script_path="../lua_lib/distribute_lock.lua")
    keys, args = ["test"], ["10"]
    res = lua_redis_helper.multiply(keys, args)
    print res