#
# @lc app=leetcode.cn id=263 lang=python3
# @lcpr version=30204
#
# [263] 丑数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        if(n <= 0):
            return False
        else:
            while(n % 2 == 0):
                n /= 2
            while(n % 3 == 0):
                n /= 3
            while(n % 5 == 0):
                n /= 5
            if(n == 1):
                return True
            return False
# @lc code=end



#
# @lcpr case=start
# 6\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 14\n
# @lcpr case=end

#

