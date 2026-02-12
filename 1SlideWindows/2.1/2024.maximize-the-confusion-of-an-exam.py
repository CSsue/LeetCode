#
# @lc app=leetcode.cn id=2024 lang=python3
# @lcpr version=30204
#
# [2024] 考试的最大困扰度
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # 进行K次操作，等价于字符串可以有k个相反的字母
        ans = 0
        # 由于下述循环判断条件问题，此处转用变量记录数值
        # cnt = defaultdict(int)
        yes = 0
        no = 0

        left = 0
        for right, val in enumerate(answerKey):
            # cnt[val] += 1
            if val == 'T':
                yes += 1
            else:
                no += 1

            # 此处判断条件有问题，当窗口只有一种字符时仍然错误进入循环
            # while min(cnt.values()) > k:
            while min(yes, no) > k:
                # cnt[answerKey[left]] -= 1
                if answerKey[left] == 'T':
                    yes -= 1
                else:
                    no -= 1

                left += 1

            ans = max(ans, right - left + 1)
        return ans
# @lc code=end



#
# @lcpr case=start
# "TTFF"\n2\n
# @lcpr case=end

# @lcpr case=start
# "TFFT"\n1\n
# @lcpr case=end

# @lcpr case=start
# "TTFTTFTT"\n1\n
# @lcpr case=end

#

