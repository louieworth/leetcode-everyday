#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
'''
思路：
从后到前循环遍历  for i in range(len(digits)-1, -1, -1)
1. 如果该位置 ！=9 ，直接➕1返回
2. 如果该位置 =9，直接=0， 留给下一个for循环来加1
边界判定：
1. 例如999情况，在首位+1
'''

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9 :
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        #如果跳出该循环，说明直接是999类似的情况
        digits.insert(0,1)
        return digits
        
         
# @lc code=end

