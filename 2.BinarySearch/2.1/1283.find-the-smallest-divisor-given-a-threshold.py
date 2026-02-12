#
# @lc app=leetcode.cn id=1283 lang=python3
# @lcpr version=30204
#
# [1283] 使结果不超过阈值的最小除数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # 理解错误
        
        # nums.sort()
        # n = len(nums)
        # left = 0
        # right = n - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     add = 0
        #     for i, val in enumerate(nums):
        #         if val % nums[mid] == 0:
        #             add += val / nums[mid]
        #         else:
        #             add += (val / nums[mid] + 1)
        #     if add <= threshold:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return nums[right]

        # 对于数组最大值必然成立
        mx = max(nums)
        cnt = []
        # 生成数组进行计算
        for i in range(mx):
            cnt.append(i + 1)
        
        left = 0
        right = len(cnt) - 1
        while left <= right:
            mid = (left + right) // 2
            add = 0
            for i, val in enumerate(nums):
                if val % cnt[mid] == 0:
                    # 注意：此处应该使用整数除法，而非浮点数除法
                    add += val // cnt[mid]
                else:
                    add += (val // cnt[mid] + 1)
            

            if add > threshold:
                left = mid + 1
            else:
                right = mid - 1
        return cnt[left]

# @lc code=end



#
# @lcpr case=start
# [1,2,5,9]\n6\n
# @lcpr case=end

# @lcpr case=start
# [2,3,5,7,11]\n11\n
# @lcpr case=end

# @lcpr case=start
# [19]\n5\n
# @lcpr case=end

#

