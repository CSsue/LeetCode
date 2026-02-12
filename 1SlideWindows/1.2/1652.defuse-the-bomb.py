#
# @lc app=leetcode.cn id=1652 lang=python3
# @lcpr version=30204
#
# [1652] 拆炸弹
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        sum = 0

        if k == 0:
            return ans
        elif k > 0:
            # 计算第一个窗口的和
            for i in range(k):
                sum += code[i]
            ans[n - 1] = sum
            # 考虑第二个滑动窗口及之后
            for i in range(1, n):
                sum = sum + code[(i + k - 1) % n] - code[i - 1]
                ans[i - 1] = sum
            return ans
        
        elif k < 0:
            # 使用负数索引会导致滑动错误
            # 建议引用新变量
            #
            #  # 计算第一个窗口的和
            # for i in range(-k):
            #     sum += code[i]
            # ans[-k] = sum
            # # 考虑第二个滑动窗口及之后
            # for i in range(-k, n):
            #     sum = sum + code[i] - code[i + k]
            #     ans[(i + 1) % n] = sum
            # for i in range(- k - 1):
            #     sum = sum + code[(i - 1) % n] - code[(i + k - 1) % n]
            #     ans[i] = sum

            # 引用3作为窗口长度重新滑动
            k = -k
            for i in range(k):
                sum += code[i]
            ans[k] = sum

            for i in range(k, n):
                sum = sum + code[i] - code[i - k]
                ans[(i + 1) % n] = sum
            
            for i in range(k - 1):
                sum = sum +code[i] - code[(i - k) % n]
                ans[(i + 1) % n] = sum

            return ans





# @lc code=end



#
# @lcpr case=start
# [5,7,1,4]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n0\n
# @lcpr case=end

# @lcpr case=start
# [2,4,9,3]\n-2\n
# @lcpr case=end

#

