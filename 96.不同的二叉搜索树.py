# @before-stub-for-debug-begin
from python3problem96 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start

'''
思路： 
https://leetcode-cn.com/problems/unique-binary-search-trees/solution/er-cha-sou-suo-shu-fu-xi-li-zi-jie-shi-si-lu-by-xi/
时间复杂度：O(n^2)
'''
class Solution:
    def numTrees(self, n: int) -> int:
        store = [1,1] # n=0,1
        if n < 2:
            return store[n]
        for m in range(2,n+1):
            count = 0
            for i in range(m):
                count += store[i] * store[m-1-i]
            store.append(count)
        return store[n]
# @lc code=end

