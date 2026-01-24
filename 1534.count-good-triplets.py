#
# @lc app=leetcode.cn id=1534 lang=python3
# @lcpr version=30204
#
# [1534] 统计好三元组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if(-a <= (arr[i] - arr[j]) and (arr[i] - arr[j]) <= a
                       and -b <= (arr[j] - arr[k]) and (arr[j] - arr[k]) <= b
                       and -c <= (arr[i] - arr[k]) and (arr[i] - arr[k]) <= c
  
                       ):
                        count += 1
        return count

                        
# @lc code=end



#
# @lcpr case=start
# [3,0,1,1,9,7]\n7\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,2,3]\n0\n0\n1\n
# @lcpr case=end

#

