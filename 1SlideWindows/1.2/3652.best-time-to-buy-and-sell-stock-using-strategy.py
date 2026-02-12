#
# @lc app=leetcode.cn id=3652 lang=python3
# @lcpr version=30204
#
# [3652] 按策略买卖股票的最佳时机
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        # 1. 用两次滑动窗口，增加了运行时间，效率低
        n = len(prices)
        init = 0
        # diff  =0
        # temp = 0

        # 计算初始值
        for i in range(n):
            init += prices[i] * strategy[i]

        # 考虑使用两次滑动窗口
        # 此处的写法会导致k成为浮点数，无法进行索引,需要进行类型转换
        # k = k / 2
        k = int(k / 2)

        # 滑动窗口1：前半部分，全部变成0，求差存入left数组中
        left = [0] * n
        leftcount = 0
        for i in range(n - k):
            leftcount += (0 - strategy[i]) * prices[i]

            l = i - k + 1
            if l < 0:
                continue
                
            left[l] += leftcount

            leftcount -= (0 - strategy[l]) * prices[l]

        # 滑动窗口2：后半部分，全部变成1，求差存入right数组中
        right = [0] * n
        rightcount = 0
        for i in range(k, n):
            rightcount += (1 - strategy[i]) * prices[i]

            l = i - k + 1
            if l < k:
                continue

            right[i - 2 * k + 1] += rightcount

            rightcount -= (1 - strategy[l]) * prices[l]
        
        ans = [0] * n
        for i in range(n):
            ans[i] = left[i] + right[i]
        
        return init + max(ans)
    

    # 2.用一次滑动窗口解决问题
    



# @lc code=end



#
# @lcpr case=start
# [4,2,8]\n[-1,0,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [5,4,3]\n[1,1,0]\n2\n
# @lcpr case=end

#

