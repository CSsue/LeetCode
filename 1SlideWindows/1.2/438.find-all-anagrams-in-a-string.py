#
# @lc app=leetcode.cn id=438 lang=python3
# @lcpr version=30204
#
# [438] 找到字符串中所有字母异位词
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 题解：计算s和滑动窗口的字母出现次数并对比，满足则记录
        ans = []
        n = len(p)
        cnt = defaultdict(int)
        for i, val in enumerate(p):
            cnt[val] += 1

        # 滑动窗口
        cnt1 = defaultdict(int)
        for i, val in enumerate(s):
            cnt1[val] += 1

            left = i - n + 1
            if left < 0:
                continue

            if cnt == cnt1:
                ans.append(left)
            
            cnt1[s[left]] -= 1
            if cnt1[s[left]] == 0:
                del cnt1[s[left]]
            
        return ans


# @lc code=end



#
# @lcpr case=start
# "cbaebabacd"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abab"\n"ab"\n
# @lcpr case=end

#

