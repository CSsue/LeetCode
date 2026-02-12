#
# @lc app=leetcode.cn id=3090 lang=python3
# @lcpr version=30204
#
# [3090] 每个字符最多出现两次的最长子字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        cnt = Counter()

        left = 0
        for right, val in enumerate(s):
            cnt[val] += 1
            while cnt[val] > 2:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans
        
# @lc code=end



#
# @lcpr case=start
# "bcbbbcba"\n
# @lcpr case=end

# @lcpr case=start
# "aaaa"\n
# @lcpr case=end

#

