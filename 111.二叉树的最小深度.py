#
# @lc app=leetcode.cn id=111 lang=python
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #################
        #BFS
        ################
        '''
        if not root:
            return 0
        deque = collections.deque([(root, 1)])
        while deque:
            node, depth = deque.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                deque.append((node.left, depth+1))
            if node.right:
                deque.append((node.right, depth+1))
        '''
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        min_depth = float('inf')
        if root.left:
            min_depth = min(min_depth, self.minDepth(root.left))
        if root.right:
            min_depth = min(min_depth, self.minDepth(root.right))
        return min_depth + 1
        

# @lc code=end

