#
# @lc app=leetcode.cn id=374 lang=python3
# @lcpr version=30204
#
# [374] 猜数字大小
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if guess(mid) > 0:
                left = mid + 1
            # 下面的分支会导致1时溢出
            # elif guess(mid) == 0:
            #     return mid
            else:
                right = mid - 1
        return left

        
# @lc code=end



#
# @lcpr case=start
# 10\n6\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n
# @lcpr case=end

# @lcpr case=start
# 2\n1\n
# @lcpr case=end

#

