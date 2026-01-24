#
# @lc app=leetcode.cn id=1343 lang=python3
# @lcpr version=30204
#
# [1343] 大小为 K 且平均值大于等于阈值的子数组数目
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # # 灵神定长窗口答案模版
        # # n = len(arr)
        # count = 0
        # sum = 0
        # for i, c in enumerate(arr):
        #     sum += c
        #     if(i - k + 1) < 0:
        #         continue
        #     if sum >= threshold * k:
        #         count += 1
        #     sum -= arr[i - k + 1]
        # return count
    
    # 法二：运行速度更快
        n = len(arr)
        count = 0
        sum = 0
        for i in range(k):
            sum += arr[i]
        if sum >= (k * threshold):
            count += 1
        for i in range(k, n):
            sum = sum + arr[i] - arr[i-k]
            if sum >= (k * threshold):
                count += 1
        return count

# @lc code=end



#
# @lcpr case=start
# [2,2,2,2,5,5,5,8]\n3\n4\n
# @lcpr case=end

# @lcpr case=start
# [11,13,17,23,29,31,7,5,2,3]\n3\n5\n
# @lcpr case=end

#

