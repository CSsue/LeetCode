#
# @lc app=leetcode.cn id=1901 lang=python3
# @lcpr version=30204
#
# [1901] 寻找峰值 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        # 已知一维数组峰值的算法
        # 下面是162的函数
        def findPeak(nums: List[int]) -> int:
            
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2
                # 应用左右闭区间方法，需要对边界进行一次额外判断
                if (mid + 1) == len(nums):
                    left = mid + 1
                elif nums[mid] < nums[mid + 1] and (mid  + 1) != len(nums):
                    left = mid + 1
                else:
                    right = mid - 1
            return left if (mid + 1) != len(nums) else left - 1
        # 通过根据行和列先后找峰值的办法或许可以成功，但是操作难度大，容易出现问题
        # 先在行中找到符合范围的值
        # anscol = []
        # col = len(mat) 
        # for i in col:
        #     # 逐行调用峰值函数
        #     cnt = findPeak(mat[i]) 
        #     # 将满足条件的下标返回到anscol数组中
        #     if cnt != len(mat[i]) and cnt > 0:
        #         ans = findPeak(mat[cnt])

        # 下面考虑将二维数组转换为一维数组进行寻找
        

            

        
# @lc code=end



#
# @lcpr case=start
# [[1,4],[3,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[10,20,15],[21,30,14],[7,16,32]]\n
# @lcpr case=end

#

