#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        flag = False
        queue = [root]
        while queue:
            cur = []
            next_queue = []
            for node in queue:
                if not node: continue
                cur.append(node.val)
                next_queue.extend([node.left, node.right])
            if cur:
                if flag:
                    cur = cur[::-1]
                res.append(cur)
            flag = False if flag else True
            queue = next_queue    
        return res

# @lc code=end

