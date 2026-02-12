#
# @lc app=leetcode.cn id=2461 lang=python3
# @lcpr version=30204
#
# [2461] 长度为 K 子数组中的最大和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        ans = 0
        cnt = defaultdict(int)

        for i, val in enumerate(nums):
            sum += val
            cnt[val] += 1

            left = i - k + 1
            if left < 0:
                continue
            
            if len(cnt) == k:
                ans = max(ans, sum)
            
            f_val = nums[left]
            sum -= f_val
            cnt[f_val] -= 1

            if cnt[f_val] == 0:
                del cnt[f_val]

        return ans
        
        
# @lc code=end



#
# @lcpr case=start
# [1,5,4,2,9,9,9]\n3\n
# @lcpr case=end

# @lcpr case=start
# [4,4,4]\n3\n
# @lcpr case=end

#

