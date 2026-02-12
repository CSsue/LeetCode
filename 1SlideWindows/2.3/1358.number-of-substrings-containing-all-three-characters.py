#
# @lc app=leetcode.cn id=1358 lang=python3
# @lcpr version=30204
#
# [1358] 包含所有三种字符的子字符串数目
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # 先找到abc各出现一次的字符串,向左任意扩展都满足条件
        ans = 0
        cnt = defaultdict(int)
        left = 0
        for right, val in enumerate(s):
            cnt[val] += 1
            while len(cnt) == 3:
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    del cnt[s[left]]
                
                left += 1
            ans += left


        return ans
        
# @lc code=end



#
# @lcpr case=start
# "abcabc"\n
# @lcpr case=end

# @lcpr case=start
# "aaacb"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n
# @lcpr case=end

#

