#
# @lc app=leetcode.cn id=2586 lang=python3
# @lcpr version=30204
#
# [2586] 统计范围内的元音字符串数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        yuan = ['a', 'e', 'i', 'o', 'u']
    
        
        for i in range(left, right+1):
            temp = words[i]
            n = len(temp)
            if (temp[0] in yuan) and (temp[n-1] in yuan):
                count += 1
        return count
            
# @lc code=end



#
# @lcpr case=start
# ["are","amy","u"]\n0\n2\n
# @lcpr case=end

# @lcpr case=start
# ["hey","aeo","mu","ooo","artro"]\n1\n4\n
# @lcpr case=end

#

