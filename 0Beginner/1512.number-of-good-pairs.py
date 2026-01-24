# @lcpr-before-debug-begin
from python3problem1512 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=1512 lang=python3
# @lcpr version=30204
#
# [1512] 好数对的数目
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if(nums[i] == nums[j]):
                    count += 1
        return count

# @lc code=end


# @lcpr-div-debug-arg-start
# funName=numIdenticalPairs
# paramTypes= ["number[]"]
# @lcpr-div-debug-arg-end




#
# @lcpr case=start
# [1,2,3,1,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#

