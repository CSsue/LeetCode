#
# @lc app=leetcode.cn id=162 lang=python3
# @lcpr version=30204
#
# [162] 寻找峰值
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from math import inf


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 此处修改了原数组，将最后一个元素改为-1，列表长度变化，都会影响结果
        # nums[-1] = -1
        # nums.append(-1)
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            # 此处峰值范围判断条件参考灵神题解
            # 需要额外推论

            # 应用左右闭区间方法，需要对边界进行一次额外判断
            if (mid + 1) == len(nums):
                left = mid + 1
            elif nums[mid] < nums[mid + 1] and (mid  + 1) != len(nums):
                left = mid + 1
            else:
                right = mid - 1
        return left if (mid + 1) != len(nums) else left - 1

        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,3,5,6,4]\n
# @lcpr case=end

#

