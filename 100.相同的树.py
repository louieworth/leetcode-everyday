#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # if p and not q:
        #     return False
        # if not p and q:
        #     return False
        # if not p.val == q.val:
        #     return False
        # if not p:
        #     return
        # self.isSameTree(p.left, q.left) 
        # self.isSameTree(p.right, q.right) 
        # return True
        if not p and not q: return True   # 这里的right只是当层的right
        if not p or not q: return False
        '''
        这里可以思考的地方很多：
        1. 如果 p q 都不存在，就直接返回了，如果执行到下一步说明至少p/q存在一个/
        2. or: 如果存在一个是not的话, 就直接return false.这里不可能存在两个都不存在的情况
        因为如果都不存在的话就直接return true
        ----------------------
        return true只是当层的return，并不是fun的return
        '''
        if p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
# @lc code=end

