#
# @lc app=leetcode.cn id=930 lang=python3
# @lcpr version=30204
#
# [930] 和相同的二元子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        if max(nums) == 0:
            return int(n * (n + 1) / 2)
        # 构造函数solve计算>=k的数组数量
        def solve(nums: List[int], k: int):
            cnt1 = 0
            cnt0 = 0
            ans = 0
            left = 0
            for right, val in enumerate(nums):
                if val == 1:
                    cnt1 += 1
                while cnt1 > k:
                    if nums[left] == 1:
                        cnt1 -= 1
                    left += 1
                ans += left
            return ans
        ans = solve(nums, goal - 1) - solve(nums, goal)
        return ans

        
# @lc code=end



#
# @lcpr case=start
# [1,0,1,0,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0,0,0]\n0\n
# @lcpr case=end

#

