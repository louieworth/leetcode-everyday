#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from functools import lru_cache
from numpy.core.numeric import tensordot

# 递归调用 
# 学习了新的判断节点的方法 not(l or r) = not l and not r
# 也可以使用队列的方法判断
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        def dfs(l , r):
            # 递归终止条件：两个节点都不存在/一个节点不存在/节点值不相等
            if not (l or r):
                return True
            if not (l and r):
                return False
            if not l.val == r.val:
                return False
            return dfs(l.left, r.right) and dfs(l.right, r.left)
        return dfs(root.left, root.right)
      
# @lc code=end

