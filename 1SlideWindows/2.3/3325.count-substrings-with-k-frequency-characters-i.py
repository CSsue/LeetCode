#
# @lc app=leetcode.cn id=3325 lang=python3
# @lcpr version=30204
#
# [3325] 字符至少出现 K 次的子字符串 I
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        ans = 0
        left = 0
        for right, val in enumerate(s):
            cnt[val] += 1
            while max(cnt.values()) >= k:
                cnt[s[left]] -= 1
                left += 1
            ans += left
        return ans
        
# @lc code=end



#
# @lcpr case=start
# "abacb"\n2\n
# @lcpr case=end

# @lcpr case=start
# "abcde"\n1\n
# @lcpr case=end

#

