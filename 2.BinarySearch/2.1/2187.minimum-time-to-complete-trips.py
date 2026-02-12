#
# @lc app=leetcode.cn id=2187 lang=python3
# @lcpr version=30204
#
# [2187] 完成旅途的最少时间
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # 计算能够完成的最大时间
        mx = totalTrips * min(time)
        mi = 1 
        # 此处无需定义数组，可以直接用数字进行计算
        # 定义时间数组
        # cnt = []
        # for i in range(mx):
        #     cnt.append(i + 1)

        
        # left = 0
        # 对答案数组进行二分
        # right = len(cnt) - 1
        while mi <= mx:
            mid = (mi + mx) // 2
            add = 0
            for i, val in enumerate(time):
                # 总时间//单次时间
                add += mid // val
            if add < totalTrips:
                mi = mid + 1
            else:
                mx = mid - 1
        return mi

# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [2]\n1\n
# @lcpr case=end

#

