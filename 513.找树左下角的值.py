#
# @lc app=leetcode.cn id=513 lang=python
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        queue = [root]
        while queue:
            cur = []
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                if tmp:
                    cur.append(tmp.val)
                    queue.extend([tmp.left, tmp.right])
            if cur:
                res.append(cur)
        array = res[-1]
        return array[0]


        


        
# @lc code=end

