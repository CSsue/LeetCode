#
# @lc app=leetcode.cn id=1281 lang=python3
# @lcpr version=30204
#
# [1281] 整数的各位积和之差
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        str1 = str(n)
        lens = len(str1)
        mul = 1
        sum = 0
        for i in range(lens):
            mul *= int(str1[i])
            sum += int(str1[i])
        return mul - sum
        
# @lc code=end



#
# @lcpr case=start
# 234\n
# @lcpr case=end

# @lcpr case=start
# 4421\n
# @lcpr case=end

#

