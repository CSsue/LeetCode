#
# @lc app=leetcode.cn id=3795 lang=python3
# @lcpr version=30204
#
# [3795] 不同元素和至少为 K 的最短子数组长度
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = inf
        cnt = defaultdict(int)
        sum = 0
        left = 0
        for right, val in enumerate(nums):
            cnt[val] += 1
            if cnt[val] == 1:
                sum += val
            else:
                continue

            while sum >= k:
                ans = min(ans, right - left + 1)
                
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                    sum -= nums[left]
                left += 1
            
        return ans if ans <= n else -1

            

        
# @lc code=end



#
# @lcpr case=start
# [2,2,3,1]\n4\n
# @lcpr case=end

# @lcpr case=start
# [3,2,3,4]\n5\n
# @lcpr case=end

# @lcpr case=start
# [5,5,4]\n5\n
# @lcpr case=end

#

