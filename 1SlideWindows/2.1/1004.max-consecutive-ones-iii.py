#
# @lc app=leetcode.cn id=1004 lang=python3
# @lcpr version=30204
#
# [1004] 最大连续1的个数 III
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # 窗口中0的个数最大为K
        ans = 0
        cnt1 = 0
        cnt0 = 0
        left = 0
        for right, val in enumerate(nums):
            if val == 1:
                cnt1 += 1
            else:
                cnt0 += 1
            while cnt0 > k:
                if nums[left] == 0:
                    cnt0 -= 1
                else:
                    cnt1 -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [1,1,1,0,0,0,1,1,1,1,0]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]\n3\n
# @lcpr case=end

#

