#
# @lc app=leetcode.cn id=110 lang=python
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(NlogN) O(h)
# ref:https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/solution/ping-heng-er-cha-shu-zhuan-ti-by-fe-lucifer-3/
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node, deep):
            if not node: return 0 # return height
            l = dfs(node.left, deep + 1)
            r = dfs(node.right, deep + 1)
            return max(l, r) + 1
        if not root:
            return True
        if abs(dfs(root.left, 0) - dfs(root.right, 0)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
# @lc code=end

