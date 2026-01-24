#
# @lc app=leetcode.cn id=1422 lang=python3
# @lcpr version=30204
#
# [1422] 分割字符串的最大得分
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        # class内定义函数调用
        def countzero(s: str):
            return s.count("0")
        
        def countone(s: str):
            return s.count("1")
        n = len(s)
        cz = 0
        co = 0
        count = 0
        # range(1,n)保证了没有空字符串
        for i in range(1,n):
            cz = countzero(s[:i])
            co = countone(s[i:n])
            count = max(count,cz+co)
        return count

        
# @lc code=end



#
# @lcpr case=start
# "011101"\n
# @lcpr case=end

# @lcpr case=start
# "00111"\n
# @lcpr case=end

# @lcpr case=start
# "1111"\n
# @lcpr case=end

#

