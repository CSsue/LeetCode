#
# @lc app=leetcode.cn id=2379 lang=python3
# @lcpr version=30204
#
# [2379] 得到 K 个黑块的最少涂色次数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # 定长滑动窗口，记录最少的白色块并返回
        n = len(blocks)
        count = 0
        ans = 0
        for i in range(k):
            if blocks[i] == 'W':
                count += 1
        ans = count

        for i in range(k, n):
            if(blocks[i] == 'W'):
                count += 1
            if(blocks[i-k] == 'W'):
                count -= 1
            if count == 0:
                return count
            ans = min(ans, count)
        return ans
# @lc code=end



#
# @lcpr case=start
# "WBBWWBBWBW"\n7\n
# @lcpr case=end

# @lcpr case=start
# "WBWBBBW"\n2\n
# @lcpr case=end

#

