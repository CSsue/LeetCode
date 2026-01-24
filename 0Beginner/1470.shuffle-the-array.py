#
# @lc app=leetcode.cn id=1470 lang=python3
# @lcpr version=30204
#
# [1470] 重新排列数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # n = len(nums)/2
        odd = [0] * n
        even = [0] * n
        ans = [0] * (2*n)

        for i in range(0,n):
            even[i] = nums[i+n]
            odd[i] = nums[i]
        for i in range(0,2*n):
            if (i%2 == 0):
                ans[i] = odd[i//2]
            else:
                ans[i] = even[(i-1)//2]

        return ans
# @lc code=end



#
# @lcpr case=start
# [2,5,1,3,4,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,4,3,2,1]\n4\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,2]\n2\n
# @lcpr case=end

#

