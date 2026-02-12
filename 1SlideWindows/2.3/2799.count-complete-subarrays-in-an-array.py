#
# @lc app=leetcode.cn id=2799 lang=python3
# @lcpr version=30204
#
# [2799] 统计完全子数组的数目
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count = defaultdict(int)
        cnt = defaultdict(int)
        ans = 0
        left = 0
        for i, val in enumerate(nums):
            count[val] += 1
        dif = len(count)

        for right, val in enumerate(nums):
            cnt[val] += 1
            while len(cnt) >= dif:
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                left += 1
            ans += left
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,3,1,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [5,5,5,5]\n
# @lcpr case=end

#

