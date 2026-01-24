#
# @lc app=leetcode.cn id=1456 lang=python3
# @lcpr version=30204
#
# [1456] 定长子串中元音的最大数目
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
       # 1.暴力解法
       # 在字符串长度过大时，时间复杂度太大，无输出 
        # yuan = 'aeiou'
        # i = 0
        # j = 0
        # n = len(s)
        # count = 0
        # for i in range(n-k+1):
        #     temp = 0
        #     for j in range(k):
        #         if(s[i+j] in yuan):
        #             temp += 1
        #     count = max(count, temp)
        # return count

        # 正确解法：滑动窗口
        yuan = 'aeiou'
        i = 0
        n = len(s)
        count = 0
        # ans = 0
        for i in range(k):
            if(s[i] in yuan): # 此处代码未处理k>n的情况，合理情况下需要加边界判断
                count += 1
        ans = count
        j = 0
        for j in range(k, n):
            if(s[j] in yuan):
                count += 1
            if(s[j-k] in yuan):
                count -= 1
            ans = max(ans, count)
            if(ans == k):
                return k
        return ans

        # # 2.灵神滑动窗口解法
        # ans = vowel = 0
        # for i,c in enumerate(s): 
        #     # 将可迭代的对象变成带索引的序列，同时输出[索引，元素]
        #     if c in "aeiou":
        #         vowel += 1
            
        #     left = i-k+1 
        #     if left < 0:
        #         continue
        #     # 进入 更新最大值 退出元素
        #     ans = max(ans, vowel)
        #     if(s[left] in "aeiou"):
        #         vowel -= 1
        #     # ans = max(ans, vowel) 在这个位置后更新，实际窗口为2
        # return ans
            






        
# @lc code=end



#
# @lcpr case=start
# "abciiidef"\n3\n
# @lcpr case=end

# @lcpr case=start
# "aeiou"\n2\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n3\n
# @lcpr case=end

# @lcpr case=start
# "rhythms"\n4\n
# @lcpr case=end

# @lcpr case=start
# "tryhard"\n4\n
# @lcpr case=end

#

