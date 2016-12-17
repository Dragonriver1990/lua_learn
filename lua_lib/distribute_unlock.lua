--
-- Created by IntelliJ IDEA.
-- User: dragonriver
-- Date: 16/12/16
-- Time: 下午4:11
-- To change this template use File | Settings | File Templates.
--

-- Release Lock

local distribut_lock_key = "distribute:lock:" .. KEYS[1]

local release_res = redis.call("set", distribut_lock_key, 1)

if release_res["ok"] == "OK" then
    return 1
end
return  0

