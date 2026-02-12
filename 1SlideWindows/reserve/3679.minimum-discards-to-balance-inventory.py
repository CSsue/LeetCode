# @lcpr-before-debug-begin
from collections import defaultdict
from python3problem3679 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=3679 lang=python3
# @lcpr version=30204
#
# [3679] 使库存平衡的最少丢弃次数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        '''
            遗留问题：下述算法并未找出具体问题，428/543 cases passed
            问题test:
                [9,2,5,2,10,9,8,7]
                5
                1
                结果：2  答案：1

            更新：问题是 x 在未来要离开窗口，但由于已经丢弃，不能在离开窗口时修改 cnt
            未解决！！！

        
        '''
        # # 错误解答：下面是贪心算法，当发现计数出错后，下面算法选择丢弃最新进入的元素
        # # 
        # ans = 0
        # count = 0
        # cnt = defaultdict(int)

        # n = len(arrivals)
        # out = []

        # for i, val in enumerate(arrivals):
        #     cnt[val] += 1

        #     left = i - w + 1
        #     if left < 0:
        #         while cnt[val] > m:
        #             count += 1
        #             cnt[val] -= 1
        #             out.append(i)
        #         continue
        #     # count 自动计数，不用ans变量二次处理

        #     while cnt[val] > m:
        #         count += 1
        #         cnt[val] -= 1
        #         out.append(i)


        #     # 出窗口(注意cnt中应该写arrival的值)
        #     # 此处有错误，如果在丢弃前对这个值进行了丢弃，则此处的删除无效，会产生负数
        #     # 需要额外维护一个丢弃元素的数组？
        #     if (i - w ) not in out:
        #         cnt[arrivals[i - w]] -= 1
        

        #     if(cnt[arrivals[i - w]] == 0):
        #         del cnt[arrivals[i - w]]

        # return count

        # 灵神解答：如果窗口中还有另一元素等于当前元素，则丢弃更远的那个，才能得到最优解
        # 本质是贪心算法
        # 需要保持索引的连续性来进行窗口滑动，所以将丢弃的元素进行'软删除'

        count = 0
        cnt = defaultdict(int)
  
        for i, val in enumerate(arrivals):
            # 条件判断
            # 此方法通过将丢弃元素置0，解决窗口滑动时最左端元素被丢弃的问题
            if cnt[val] == m:
                arrivals[i] = 0
                count += 1
            else:
                cnt[val] += 1

            # 下面的分支，可以节省此处的窗口判断
            # left = i - w + 1
            # if left < 0:
            #     continue

            # 此题不需要中间元素的处理，可以直接进行窗口滑动


            if(i - w + 1 >= 0):
                cnt[arrivals[i - w + 1]] -= 1

        return count



            

                

# @lc code=end


# @lcpr-div-debug-arg-start
# funName=minArrivalsToDiscard
# paramTypes= ["number[]","number","number"]
# @lcpr-div-debug-arg-end




#
# @lcpr case=start
# [1,2,1,3,1]\n4\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,3,3,4]\n3\n2\n
# @lcpr case=end

# @lcpr case=start
# [7,3,9,9,7,3,5,9,7,2,6,10,9,7,9,1,3,6,2,4,6,2,6,8,4,8,2,7,5,6]\n10\n1\n
# @lcpr case=end

# @lcpr case=start
# [9,2,5,2,10,9,8,7]\n5\n1\n
# @lcpr case=end
