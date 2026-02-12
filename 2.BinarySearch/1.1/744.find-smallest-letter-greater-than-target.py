#
# @lc app=leetcode.cn id=744 lang=python3
# @lcpr version=30204
#
# [744] 寻找比目标字母大的最小字母
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        if left == n:
            return letters[0]
        else:
            return letters[left]
# @lc code=end



#
# @lcpr case=start
# ['c', 'f'\n'a'\n
# @lcpr case=end

# @lcpr case=start
# ['c','f','j']\n'c'\n
# @lcpr case=end

# @lcpr case=start
# ['x','x','y','y']\n'z'\n
# @lcpr case=end

#

