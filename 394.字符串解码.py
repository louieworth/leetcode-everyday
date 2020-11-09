#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#
'''
思路：首先最开始想到的就是stack的思想。
但是例如：2[a3[bc]]这种叠加应该如何实现就比较困难。
利用返回栈实现
我们设置一个stack, res, multi
遇见数字的时候，我们用multi保存数字
当遇见字母的时候，就直接输入到res
遇见[的时候，
'''
# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for i in s:
            if i == '[':
                stack.append([multi, res])
                res = ""
                multi = 0
            elif i == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= i <= '9':
                multi = 10 * multi + int(i)
            else:
                res += i
        return res

# @lc code=end

