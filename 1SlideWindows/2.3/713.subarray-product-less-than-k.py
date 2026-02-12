#
# @lc app=leetcode.cn id=713 lang=python3
# @lcpr version=30204
#
# [713] 乘积小于 K 的子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        mul = 1
        left = 0
        if k < 2:
            return 0
        for right, val in enumerate(nums):
            mul *= val
            while mul >= k:
                mul /= nums[left]
                
                left += 1

            # 下述判断条件有误
            # 对于固定的右端点，所有移动的左端点都满足条件
            ans += right - left + 1
        return ans
    
# @lc code=end



#
# @lcpr case=start
# [10,5,2,6]\n100\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n0\n
# @lcpr case=end

#

