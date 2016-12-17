--
-- Created by IntelliJ IDEA.
-- User: dragonriver
-- Date: 16/12/16
-- Time: 下午3:09
-- To change this template use File | Settings | File Templates.
--

-- First Step:apply for lock

local distribute_lock_key = "distribute:lock:" .. KEYS[1]
local lock_timeout = tonumber(ARGV[1])

local lock_res = redis.call("get", distribute_lock_key)

-- Judge the lock used or not

-- Th lock has been applyed
if lock_res == "0" then
    return 0
else
    redis.call("set", distribute_lock_key, 0)
    local exp_res = redis.call("expire", distribute_lock_key, lock_timeout)
    if exp_res == 1 then
        return 1
    end
end
return 0




