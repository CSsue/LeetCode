#
# @lc app=leetcode.cn id=867 lang=python3
# @lcpr version=30204
#
# [867] 转置矩阵
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        # 列表的错误拷贝方式
        # temp = [0] * m
        # ans = [temp] * n

        # 用正确的列表推导式
        ans = [[0]*m for i in range(n)]
        
        for i in range(m):
            for j in range(n):
                ans[j][i] = matrix[i][j]
        return ans

        
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[4,5,6]]\n
# @lcpr case=end

#

