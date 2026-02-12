#
# @lc app=leetcode.cn id=1493 lang=python3
# @lcpr version=30204
#
# [1493] 删掉一个元素以后全为 1 的最长子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # 窗口中最多只有一个0
        ans = 0
        # 可以不用hash维护计数，直接用变量即可
        # cnt = Counter()
        cnt0 = 0

        left = 0
        for right, val in enumerate(nums):
            # 1. 右端点移动
            cnt0 += 1 - val
            # 2. 条件判断，左端点移动
            while cnt0 > 1:
                cnt0 -= 1 - nums[left]
                left += 1

            # 3. 更新答案
            ans = max(ans, right - left)
        
        return ans
                
                    
        
# @lc code=end



#
# @lcpr case=start
# [1,1,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1,1,0,1,1,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1]\n
# @lcpr case=end

#

