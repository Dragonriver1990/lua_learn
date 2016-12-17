#!/usr/bin/env python
# -*-coding:utf-8-*-

"""
    实现访问频率限制: 实现访问者 $ip 在一定的时间 $time 内只能访问 $limit 次.
    使用场景：提供REST服务，例如对某些特别消耗资源的请求，下载报告单位之间内进行限制

    Lua嵌入Redis优势：
    a：减少网络开销: 不使用 Lua 的代码需要向 Redis 发送多次请求, 而脚本只需一次即可, 减少网络传输
    b：原子操作: Redis 将整个脚本作为一个原子执行, 无需担心并发, 也就无需事务
    c：复用: 脚本会永久保存 Redis 中, 其他客户端可继续使用
"""

from lua_script_helper import LuaRedisHelper


if __name__ == "__main__":
    redis_conf = {}
    lua_redis_helper = LuaRedisHelper(
        redis_conf=redis_conf, lua_script_path="../lua_lib/ip_limit.lua")
    keys, args = ["127.0.0.1"], ["5", "10"]
    res = lua_redis_helper.multiply(keys, args)
    print res
