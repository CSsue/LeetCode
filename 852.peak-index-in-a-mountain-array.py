#
# @lc app=leetcode.cn id=852 lang=python3
# @lcpr version=30204
#
# [852] 山脉数组的峰顶索引
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # 二分查找
        # 用切片数组会导致下标变化，无法正确输出索引
        # 1. 错误示范
        # n = len(arr)
        # def twoselect(arr : List[int]):
        #     n = len(arr)
        #     if((arr[n // 2] < arr[(n // 2) - 1]) and (arr[n // 2] < arr[(n // 2) + 1])):
        #         return n // 2
        #     elif((arr[n // 2] > arr[(n // 2) - 1]) and (arr[n // 2] < arr[(n // 2) + 1])):
        #         return twoselect(arr[:n//2])
        #     else:
        #         return twoselect(arr[n//2:])
        # return twoselect(arr)


        # 2，用左右指针操作原数组，进行原地寻找
        
        n = len(arr)
        low = 0
        high = n-1
        while(low < high):
            if(arr[low] < arr[low + 1]):
                low += 1
            if(arr[high] < arr[high - 1]):
                high -= 1

        return low
# @lc code=end



#
# @lcpr case=start
# [0,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,2,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,10,5,2]\n
# @lcpr case=end

#

