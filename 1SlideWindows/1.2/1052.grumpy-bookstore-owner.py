# @lcpr-before-debug-begin
from python3problem1052 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=1052 lang=python3
# @lcpr version=30204
#
# [1052] 爱生气的书店老板
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        count = 0
        n = len(customers)
        good = 0 # 记录初始状态满意顾客的数量
        for i in range(n):    
            if grumpy[i] == 0:
                good += customers[i]


        better = 0 # 窗口内产生的满意顾客
        i = 0
        for i, val in enumerate(grumpy):
            if val == 1:
                count += customers[i]
            
            left = i - minutes + 1
            if left < 0:
                continue
            
            better = max(better, count)

            if grumpy[left] == 1:
                count -= customers[left]
        
        return good + better
# @lc code=end



#
# @lcpr case=start
# [1,0,1,2,1,1,7,5]\n[0,1,0,1,0,1,0,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n[0]\n1\n
# @lcpr case=end

#

