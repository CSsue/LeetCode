# @lcpr-before-debug-begin
from python3problem231 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=231 lang=python3
# @lcpr version=30204
#
# [231] 2 的幂
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n == 1):
            return True
        while(n):
            if (n % 2 == 0 and n != 2):
                n /= 2
            elif n == 2:
                return True
            else:
                return False
        return False
        
# @lc code=end



#
# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 16\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#

