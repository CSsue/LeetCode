# @lcpr-before-debug-begin
from python3problem1486 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=1486 lang=python3
# @lcpr version=30204
#
# [1486] 数组异或操作
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        i = 0
        nums = [0] * n
        ans = 0
        while i < n:
            nums[i] = start + 2 * i
            ans ^= nums[i]
            i += 1
        
        return ans
        
# @lc code=end


# @lcpr-div-debug-arg-start
# funName=xorOperation
# paramTypes= ["number","number"]
# @lcpr-div-debug-arg-end




#
# @lcpr case=start
# 5\n0\n
# @lcpr case=end

# @lcpr case=start
# 4\n3\n
# @lcpr case=end

# @lcpr case=start
# 1\n7\n
# @lcpr case=end

# @lcpr case=start
# 10\n5\n
# @lcpr case=end

#

