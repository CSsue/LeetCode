#
# @lc app=leetcode.cn id=34 lang=python3
# @lcpr version=30204
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 二分查找，红黑树
        # 递归实现
        def lower_bound(nums: List[int], target: int):
            n = len(nums)
            left = 0
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                # red
                if nums[mid] < target:
                    left = mid + 1
                # blue
                else:
                    right = mid - 1
            return left
        
        start = lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        else:
            end = lower_bound(nums, target + 1) -1
        
        return [start, end]
# @lc code=end



#
# @lcpr case=start
# [5,7,7,8,8,10]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,7,7,8,8,10]\n6\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#

