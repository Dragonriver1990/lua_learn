--
-- Created by IntelliJ IDEA.
-- User: dragonriver
-- Date: 16/12/15
-- Time: 下午3:11
-- To change this template use File | Settings | File Templates.
--

--The return 'table name' must be same with module name(File name)
--And module name can not be same with lua module

local mymath =  {}
function mymath.add(a,b)
    print(a+b)
end

function mymath.sub(a,b)
    print(a-b)
end

function mymath.mul(a,b)
    print(a*b)
end

function mymath.div(a,b)
    print(a/b)
end

return mymath
