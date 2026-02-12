#
# @lc app=leetcode.cn id=904 lang=python3
# @lcpr version=30204
#
# [904] 水果成篮
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        cnt = defaultdict(int)
        left = 0
        for right, val in enumerate(fruits):
            cnt[val] += 1
            while len(cnt) > 2:
                cnt[fruits[left]] -= 1
                if cnt[fruits[left]] == 0:
                    del cnt[fruits[left]]
                left += 1
            # 计算字典value的和
            # ans = max(ans, sum(cnt.values()))
            # 或者计算窗口长度,答案相同，但计算窗口长度显然降低时间复杂度
            ans = max(ans, right - left + 1)
        return ans


            
        
# @lc code=end



#
# @lcpr case=start
# [1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3,1,2,1,1,2,3,3,4]\n
# @lcpr case=end

#

