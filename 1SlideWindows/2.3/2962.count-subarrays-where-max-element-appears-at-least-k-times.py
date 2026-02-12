#
# @lc app=leetcode.cn id=2962 lang=python3
# @lcpr version=30204
#
# [2962] 统计最大元素出现至少 K 次的子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxnum = max(nums)
        count = nums.count(maxnum)
        if count < k:
            return 0
        cnt = 0
        left = 0
        ans = 0
        for right, val in enumerate(nums):
            if val == maxnum:
                cnt += 1
            # 此处不断右移左指针left，直到窗口中的 maxnum 的出现次数小于 k 为止
            while cnt >= k:
                if nums[left] == maxnum:
                    cnt -= 1
                left += 1
            ans += left

        return ans



# @lc code=end



#
# @lcpr case=start
# [1,3,2,3,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,4,2,1]\n3\n
# @lcpr case=end

#

