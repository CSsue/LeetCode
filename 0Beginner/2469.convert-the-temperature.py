#
# @lc app=leetcode.cn id=2469 lang=python3
# @lcpr version=30204
#
# [2469] 温度转换
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.8 + 32.00
        ans = [kelvin,fahrenheit]
        return ans
# @lc code=end



#
# @lcpr case=start
# 36.50\n
# @lcpr case=end

# @lcpr case=start
# 122.11\n
# @lcpr case=end

#

