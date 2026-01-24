#
# @lc app=leetcode.cn id=643 lang=python3
# @lcpr version=30204
#
# [643] 子数组最大平均数 I
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

from typing import List
import math

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 法一：单独计算第一个窗口，逐个滑动
        n = len(nums)
        ans = 0
        count = 0
        for i in range(k):
            count += nums[i]
        ans = count

        for i in range(k, n):
            count = count + nums[i] - nums[i-k]
            ans = max(ans, count)
        return ans / k
    
        # # 法二：一次循环：入 更新 出Cus
        # n = len(nums)
        # ans = -inf # 最小负数
        # count = 0
        # for i, val in enumerate(nums):
        #     count += val
        #     if (i - k + 1) < 0:
        #         continue
        #     ans = max(ans, count)

        #     count -= nums[i - k + 1]

        # return ans/k


# @lc code=end



#
# @lcpr case=start
# [1,12,-5,-6,50,3]\n4\n
# @lcpr case=end

# @lcpr case=start
# [5]\n1\n
# @lcpr case=end

#

