#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
#
'''
思路：
我们分别想所有节点到左边第一个C字符的最短距离和到右边C字符的最短距离。
左边是： i-pre 
右边是   pre-i
我们取最小值，那么pre-<=负无穷  pre->正无穷 
重点： enumerate, range函数的使用
'''
# @lc code=start
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        res = []
        pre = float('-inf')
        for i,x in enumerate(S):  
            if x == C: pre = i
            res.append(i - pre)
        pre = float('inf')
        for i in range(len(S)-1, -1, -1): # 转换为list
            if S[i] == C: pre = i
            res[i] = min(res[i], pre - i)
        return res 
                    


# 题解：https://leetcode-cn.com/problems/shortest-distance-to-a-character/solution/zi-fu-de-zui-duan-ju-chi-by-leetcode/
# O(N)  O(N)

# @lc code=end

