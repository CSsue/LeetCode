#
# @lc app=leetcode.cn id=3634 lang=python3
# @lcpr version=30204
#
# [3634] 使数组平衡的最少移除数目
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        # 对数组进行排序，通过左右两个指针的移动调整数组的合理性
        nums.sort()
        left = 0
        minval = nums[left]
        ans = 0

        for right, val in enumerate(nums):
            while nums[left] * k < val:
                left += 1
            ans = max(ans, right - left + 1)
        
        return len(nums) - ans

            

        
# @lc code=end



#
# @lcpr case=start
# [2,1,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,6,2,9]\n3\n
# @lcpr case=end

# @lcpr case=start
# [4,6]\n2\n
# @lcpr case=end

#

