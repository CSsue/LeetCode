#
# @lc app=leetcode.cn id=2529 lang=python3
# @lcpr version=30204
#
# [2529] 正整数和负整数的最大计数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def lower(nums: List[int], k: int):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < k:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        n = len(nums)
        pos = n - lower(nums, 1) 
        neg = lower(nums, 0)

        return max(pos, neg)

        
# @lc code=end



#
# @lcpr case=start
# [-2,-1,-1,1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [-3,-2,-1,0,0,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [5,20,66,1314]\n
# @lcpr case=end

#

