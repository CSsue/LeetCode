#
# @lc app=leetcode.cn id=326 lang=python3
# @lcpr version=30204
#
# [326] 3 的幂
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if (n == 1):
            return True
        while(n):
            if (n % 3 == 0 and n != 3):
                n /= 3
            elif n == 3:
                return True
            else:
                return False
        return False        
        
# @lc code=end



#
# @lcpr case=start
# 27\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

# @lcpr case=start
# 9\n
# @lcpr case=end

# @lcpr case=start
# 45\n
# @lcpr case=end

#

