#
# @lc app=leetcode.cn id=30 lang=python3
# @lcpr version=30204
#
# [30] 串联所有单词的子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # 方法一：
        # 下述方法存在冗余，性能较差，可以正常通过测试，但可以直接按照单词粒度滑动
        # 先判断滑动窗口中的字符串与words中的字母个数一致
        # 再判断单词顺序一致
        cnt = defaultdict(int)
        word_cnt = defaultdict(int)
        n = len(s)
        m = len(words[0])
        k = len(words)
        win = m * k
        ans = []

        # 计算words中单词的计数，用哈希表word_cnt存储
        # 计算words数组中所有字母出现的次数，用哈希表cnt存储
        for i, val in enumerate(words):
            word_cnt[val] += 1
            for j, val in enumerate(words[i]):
                cnt[val] += 1
        # 验证words中字母个数统计个数相同
        # return cnt

        # 窗口内字母计数        
        cnt1 = defaultdict(int)
        for i, val in enumerate(s):
            cnt1[val] += 1

            left = i - win + 1
            if left < 0:
                continue

            if cnt1 == cnt:
                # 将该窗口的字符串，按照单词长度划分，和word_cnt对比，一致则成立
                temp = s[left : i + 1] # 将窗口暂存为一个新的字符串
                win_cnt = defaultdict(int)

                for j in range(k):
                    win_cnt[temp[j * m : j * m + m]] += 1

                if win_cnt == word_cnt:
                    ans.append(left)

            val_left = s[left]
            cnt1[val_left] -= 1
            if cnt1[val_left] == 0:
                del cnt1[val_left]
        
        return ans

        """
            保留问题：下述解答报错尚未解决
        """
        # 法二：按照单词粒度滑动，做起点不同的滑动
        # 窗口滑动次数增长为n(一个单词的长度)
        # n = len(s)
        # wordlen = len(words[0])
        # wordcnt = len(words)
        # win = wordlen * wordcnt

        # ans = []

        # # 记录words中单词出现的次数
        # cnt = defaultdict(int)
        # for i, val in enumerate(words):
        #     cnt[val] += 1

        # # 不同轮次的窗口滑动
        # for i in range(wordlen):
        #     # 初始化单次计数字典
        #     win_cnt = defaultdict(int)

        #     # 单次窗口滑动
        #     length = int(n / wordlen)
        #     if i == 0:
        #         for j in range(length):
        #             win_cnt[s[j * wordlen : (j + 1) * wordlen]] += 1
                
        #             left = j - wordcnt + 1
        #             if left < 0:
        #                 continue

        #             if win_cnt == cnt:
        #                 ans.append(j * wordlen - len + 1)
                    
                    
        #             win_cnt[s[(j - wordcnt + 1) * wordlen : (j - wordcnt + 1 + 1) * wordlen]]
                    
        #     if i != 0:
        #         for j in range(length - 1):
        #             win_cnt[s[(j - i) * wordlen : (j - i + 1) * wordlen]] += 1
                
        #             left = j - i - wordcnt + 1
        #             if left < 0:
        #                 continue

        #             if win_cnt == cnt:
        #                 ans.append((j - i) * wordlen - len + 1)
                    
                    
        #             win_cnt[s[(j - i - wordcnt + 1) * wordlen : (j - i - wordcnt + 1 + 1) * wordlen]]
                
        # return ans

# @lc code=end



#
# @lcpr case=start
# "barfoothefoobarman"\n["foo","bar"]\n
# @lcpr case=end

# @lcpr case=start
# "wordgoodgoodgoodbestword"\n["word","good","best","word"]\n
# @lcpr case=end

# @lcpr case=start
# "barfoofoobarthefoobarman"\n["bar","foo","the"]\n
# @lcpr case=end

#

