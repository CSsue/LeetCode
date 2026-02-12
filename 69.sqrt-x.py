#
# @lc app=leetcode.cn id=69 lang=python3
# @lcpr version=30204
#
# [69] x 的平方根 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        
        left = 0
        right = x // 2
        while left <= right:
            mid = (left + right) // 2
            if mid * mid < x and (mid + 1) * (mid + 1) :
                left = mid + 1
            else:
                right = mid - 1
        return left if left * left == x else left - 1


        
# @lc code=end



#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 8\n
# @lcpr case=end

#

