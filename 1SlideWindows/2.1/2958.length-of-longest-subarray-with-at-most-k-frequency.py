#
# @lc app=leetcode.cn id=2958 lang=python3
# @lcpr version=30204
#
# [2958] 最多 K 个重复元素的最长子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        cnt = defaultdict(int)

        left = 0
        for right, val in enumerate(nums):
            cnt[val] += 1
            while cnt[val] > k:
                cnt[nums[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
            
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1,2,3,1,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,2,1,2,1,2]\n1\n
# @lcpr case=end

# @lcpr case=start
# [5,5,5,5,5,5,5]\n4\n
# @lcpr case=end

#

