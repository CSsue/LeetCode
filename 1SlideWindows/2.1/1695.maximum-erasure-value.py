#
# @lc app=leetcode.cn id=1695 lang=python3
# @lcpr version=30204
#
# [1695] 删除子数组的最大得分
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = 0
        sum = 0
        cnt = defaultdict(int)
        left = 0
        for right, val in enumerate(nums):
            sum += val
            cnt[val] += 1
            while cnt[val] > 1:
                cnt[nums[left]] -= 1
                sum -= nums[left]
                # 错误处理
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                left += 1
            ans = max(ans, sum)
     
        
        return ans

                

        
# @lc code=end



#
# @lcpr case=start
# [4,2,4,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [5,2,1,2,5,2,1,2,5]\n
# @lcpr case=end

#

