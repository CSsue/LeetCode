#
# @lc app=leetcode.cn id=1423 lang=python3
# @lcpr version=30204
#
# [1423] 可获得的最大点数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from enum import CONTINUOUS


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # 错误答案：
        # 原因：中间留下的空白段是固定的，漏掉很多正确答案
        # 
        # # 将后K个元素移位到前面，则得到正常的滑动窗口
        # # 0 1 2 3 4 (5 6 7)  k = 3, 等价--> (5 6 7) 0 1 2 3 4
        # # 1.调整数组
        # n = len(cardPoints)
        # cardPoints = cardPoints[n - k : n] + cardPoints[ : n - k]

        # # 2. 滑动窗口计算最大值
        # ans = 0
        # sum = 0

        # for i in range(k):
        #     sum += cardPoints[i]

        # ans = sum

        # bound = min(2 * k - 1, n)

        # for i in range(k, bound):
        #     sum = sum + cardPoints[i] - cardPoints[i - k]
        #     ans = max(ans, sum)

        # return ans

        # 正确方法：
        # 计算中间空白段的最小值，可以利用定长窗口
        n = len(cardPoints)

        # inf表示正无穷
        ans = inf
        sums = 0
        all = 0

        win = n - k
        if win == 0:
            return sum(cardPoints)
        
        for i, val in enumerate(cardPoints):
            sums += val
            all += val

            # 当窗口为0，left = i + 1越界
            left = i - win + 1
            if left < 0:
              continue
            
            ans = min(ans, sums)

            sums -= cardPoints[left]

        return all - ans



# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [9,7,7,9,7,7,9]\n7\n
# @lcpr case=end

# @lcpr case=start
# [1,1000,1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,79,80,1,1,1,200,1]\n3\n
# @lcpr case=end

#

