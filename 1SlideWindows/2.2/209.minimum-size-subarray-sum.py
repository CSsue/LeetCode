#
# @lc app=leetcode.cn id=209 lang=python3
# @lcpr version=30204
#
# [209] 长度最小的子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        # inf表达最大正数
        ans = inf
        sum = 0
        left = 0

        # 法一
        # for right, val in enumerate(nums):
        #     sum += val
        #     while sum - nums[left] > target:
        #         sum -= nums[left]
        #         left += 1
        #     if sum >= target:
        #         ans = min(ans, right - left + 1)

        for right, val in enumerate(nums):
            sum += val
            while sum >= target:
                ans = min(ans, right - left + 1)
                sum -= nums[left]
                left += 1
        
        return ans if ans <= n else 0
                


            
# @lc code=end



#
# @lcpr case=start
# 7\n[2,3,1,2,4,3]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[1,4,4]\n
# @lcpr case=end

# @lcpr case=start
# 11\n[1,1,1,1,1,1,1,1]\n
# @lcpr case=end

#

