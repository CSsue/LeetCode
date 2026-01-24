#
# @lc app=leetcode.cn id=258 lang=python3
# @lcpr version=30204
#
# [258] 各位相加
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        """
            1.整数转换字符串循环求和
        """
        # count = 0
        str1 = str(num)
        # list1 = list(str1)
        n = len(str1)
        if(n == 1):
            return num
        while (n != 1):
            # 累加器需要在循环内清零
            count = 0
            for i in range(n):
                count += int(str1[i])
            str1 = str(count)    
            n = len(str1)
        return count
    
        """
            2.取余取整计算
        """
        # while num >= 10:
        #     count = 0
        #     while num:
        #         count += num % 10
        #         num //= 10
        #     num = count
        # return num
        





# @lc code=end



#
# @lcpr case=start
# 38\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

#

