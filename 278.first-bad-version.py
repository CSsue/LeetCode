#
# @lc app=leetcode.cn id=278 lang=python3
# @lcpr version=30204
#
# [278] 第一个错误的版本
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid) == False:
                left = mid + 1
            else:
                right = mid - 1
        return left
        
# @lc code=end



#
# @lcpr case=start
# 5\n4\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n
# @lcpr case=end

#

