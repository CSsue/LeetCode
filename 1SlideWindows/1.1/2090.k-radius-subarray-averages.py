#
# @lc app=leetcode.cn id=2090 lang=python3
# @lcpr version=30204
#
# [2090] 半径为 k 的子数组平均值
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        avgs = [-1] * n
        sum = 0
        
        # 错误处理
        if (2 * k + 1) > n:
            return avgs
        
        for i in range(2 * k + 1):
            sum += nums[i]
        
        avgs[k] = sum // (2 * k + 1)

        for i in range(k + 1, n - k):
            sum = sum + nums[i + k] - nums[i - k -1]
            avgs[i] = sum // (2 * k + 1)

        return avgs



# @lc code=end



#
# @lcpr case=start
# [7,4,3,9,1,8,5,2,6]\n3\n
# @lcpr case=end

# @lcpr case=start
# [100000]\n0\n
# @lcpr case=end

# @lcpr case=start
# [8]\n100000\n
# @lcpr case=end

#

