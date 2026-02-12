#
# @lc app=leetcode.cn id=74 lang=python3
# @lcpr version=30204
#
# [74] 搜索二维矩阵
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       # 下面做法的边界处理容易出错
        # n = len(matrix)
        # def solve(s: List[int], k: int):
        #     left = 0
        #     right = len(s) - 1
        #     while left <= right:
        #         mid = (left + right) // 2
        #         if s[mid] < k:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
        #     return left
        # num0 = []
        # for i in range(n):
        #     num0.append(matrix[i][0])
        
        # col = solve(num0, target) - 1
        # # 边界处理
        # # 这个边界处理仍然有问题，在部分用例中无法通过
        # if col < 0:
        #     return False
        
        # ans = solve(matrix[col], target)
        # # 边界处理
        # if ans < len(matrix[col]):
        
        #     if matrix[col][ans] == target:
        #         return True
        #     else:
        #         return False
        # else:
        #     return False

        # 方法二：

        # 将矩阵转换为一个完整的数组
        m = len(matrix)
        n = len(matrix[0])
        nums = []
        for i in range(m):
            for j in range(n):
                nums.append(matrix[i][j])
        
        right = len(nums) - 1
        left = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if left < len(nums) and nums[left] == target:
            return True
        else:
            return False

      

# @lc code=end



#
# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n13\n
# @lcpr case=end

#

