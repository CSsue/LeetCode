#
# @lc app=leetcode.cn id=1208 lang=python3
# @lcpr version=30204
#
# [1208] 尽可能使字符串相等
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans = 0
        left = 0
        cost = 0

        for right, val in enumerate(s):
            cost += abs(ord(val) - ord(t[right]))
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans
            
        
# @lc code=end



#
# @lcpr case=start
# "abcd"\n"bcdf"\n3\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n"cdef"\n3\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n"acde"\n0\n
# @lcpr case=end

#

