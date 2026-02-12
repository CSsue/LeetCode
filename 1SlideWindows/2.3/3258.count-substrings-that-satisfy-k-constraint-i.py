#
# @lc app=leetcode.cn id=3258 lang=python3
# @lcpr version=30204
#
# [3258] 统计满足 K 约束的子字符串数量 I
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = 0
        cnt1 = 0
        cnt0 = 0
        left = 0
        for right, val in enumerate(s):
            if val == '0':
                cnt0 += 1
            else:
                cnt1 += 1
            
            # 此处条件用and
            while cnt0 > k and cnt1 > k:
                if s[left] == '0':
                    cnt0 -= 1
                else:
                    cnt1 -= 1
                left += 1
            
            ans += right - left + 1
        
        return ans
        
# @lc code=end



#
# @lcpr case=start
# "10101"\n1\n
# @lcpr case=end

# @lcpr case=start
# "1010101"\n2\n
# @lcpr case=end

# @lcpr case=start
# "11111"\n1\n
# @lcpr case=end

#

