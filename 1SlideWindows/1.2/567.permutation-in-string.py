#
# @lc app=leetcode.cn id=567 lang=python3
# @lcpr version=30204
#
# [567] 字符串的排列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 题解：记录每种字母的次数，滑动窗口进行对比，如果相同则满足条件
        n = len(s1)

        cnt = defaultdict(int) # 字典记录s1中字母的出现次数
        for i, val in enumerate(s1):
            cnt[val] += 1
        
        cnt2 = defaultdict(int) # 字典记录s2滑动窗口中字母出现的次数

        for i,  val in enumerate(s2):
            cnt2[val] += 1

            left = i - n + 1
            if left < 0:
                continue

            if cnt == cnt2:
                return True
            
            cnt2[s2[left]] -= 1
            if cnt2[s2[left]] == 0:
                del cnt2[s2[left]]
            
        return False

        
# @lc code=end



#
# @lcpr case=start
# "eidbaooo"\n
# @lcpr case=end

# @lcpr case=start
# "eidboaoo"\n
# @lcpr case=end

#

