#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30204
#
# [3] 无重复字符的最长子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 不定长滑动窗口，利用双指针解决
        ans = 0
        cnt = Counter() # hashmap char int

        left = 0
        for right, val in enumerate(s):
            cnt[val] += 1
            while cnt[val] > 1:
                cnt[s[left]] -= 1
                left += 1
            len = right - left + 1
            ans = max(ans, len)
        
        return ans
    
        
        
# @lc code=end



#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#

