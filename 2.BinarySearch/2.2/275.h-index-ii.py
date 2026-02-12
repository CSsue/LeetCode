#
# @lc app=leetcode.cn id=275 lang=python3
# @lcpr version=30204
#
# [275] H 指数 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if n == 1:
            return 1 if citations[0] != 0 else 0
        
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if citations[mid] < (n - mid):
                left = mid + 1
            else:
                right = mid - 1
        # 注意此处返回值不是left
        return n - left
                



# @lc code=end



#
# @lcpr case=start
# [0,1,3,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,100]\n
# @lcpr case=end

#

