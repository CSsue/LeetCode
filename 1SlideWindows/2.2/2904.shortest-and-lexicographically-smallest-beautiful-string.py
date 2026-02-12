#
# @lc app=leetcode.cn id=2904 lang=python3
# @lcpr version=30204
#
# [2904] 最短且字典序最小的美丽子字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # 错误处理
        if s.count('1') < k:
            return ""
        
        ans = s
        cnt1 = 0
        left = 0
        for right, val in enumerate(s):
            # 1是字符串，不是整数
            if val == '1':
                cnt1 += 1
            
            while cnt1 == k:
                # 此处需要调整判断条件，直接返回字符串
                # ans = min(ans, right - left + 1)
                # 对于相同长度的字符串，需要考虑字典序
                temp = s[left: right + 1]
                if (len(temp) < len(ans)) or (len(temp) == len(ans) and temp < ans): 
                    ans = temp
                if s[left] == '1':
                    cnt1 -= 1
                left += 1
        return ans
            
        
# @lc code=end



#
# @lcpr case=start
# "100011001"\n3\n
# @lcpr case=end

# @lcpr case=start
# "1011"\n2\n
# @lcpr case=end

# @lcpr case=start
# "000"\n1\n
# @lcpr case=end

#

