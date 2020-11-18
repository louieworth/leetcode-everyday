#
# @lc app=leetcode.cn id=129 lang=python
#
# [129] 求根到叶子节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        时间复杂度O(N) 空间复杂度O(N)，主要是看递归站栈的调用次数
        """
        def helper(node, i):
            if not node: return 0
            tmp = 10 * i + node.val
            if not node.left and not node.right:
                return tmp 
            return helper(node.left, tmp) + helper(node.right, tmp)

        return helper(root, 0)
# @lc code=end

