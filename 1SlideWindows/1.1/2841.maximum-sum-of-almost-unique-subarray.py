#
# @lc app=leetcode.cn id=2841 lang=python3
# @lcpr version=30204
#
# [2841] 几乎唯一子数组的最大和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        # 法一：通过数组切片 + set计算不同元素的个数，时间复杂度大
        # n = len(nums)
        # ans = 0
        # sum = 0 # 滑动窗口的元素和
        # count = 0 # 不同元素的数量
        # # 错误处理
        # if k > n:
        #     return 0
        
        # for i in range(k):
        #     sum += nums[i]  
        
        # count = len(set(nums[:k]))
        # # 错误处理
        # if k == n and count < m:
        #     return 0
        # # 没有符合要求的数组，返回0
        # elif count >= m:
        #     ans = sum
        
        # for i in range(k, n):
        #     # ans = sum
        #     sum = sum + nums[i] - nums[i-k]
        #     count = len(set(nums[i-k+1:i+1]))
        #     if(count >= m):
        #         ans = max(ans, sum)
            
        # return ans


        #法二：滑动窗口 + 哈希表（灵）
        ans = 0
        sum = 0
        # 此处用字典的变种：defaultdict,作用是自动初始化为0，计数器专用字典
        cnt = defaultdict(int)

        for i, val in enumerate(nums):
            # 1.进入窗口
            sum += val
            cnt[val] += 1
            left = i - k + 1

            if left < 0:
                continue

            # 2.更新数值
            if len(cnt) >= m:
                ans = max(ans, sum)

            # 3.退出窗口
            f_val = nums[left] 
            sum -= f_val
            cnt[f_val] -= 1

            # 唯一的元素退出，需要进行删除，改变dict的长度
            if cnt[f_val] == 0:
                del cnt[f_val]

        return ans

            
# @lc code=end



#
# @lcpr case=start
# [2,6,7,3,1,7]\n3\n4\n
# @lcpr case=end

# @lcpr case=start
# [5,9,9,2,4,5,4]\n1\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,2,1,2,1]\n3\n3\n
# @lcpr case=end

#

