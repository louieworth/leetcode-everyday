#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
BFS 模板
level=0
while queue 不空：
    cur = queue.pop()
    for 节点 in cur的所有相邻节点：
        if 该节点有效且未访问过：
            queue.push(该节点)
level++

要求记录层数：level
'''

import collections
from typing import Collection


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        deque = collections.deque()
        res = []
        deque.append(root)
        while deque:
            cur = []
            for _ in range(len(deque)):
                tmp = deque.popleft()
                if tmp:
                    cur.append(tmp.val)
                    deque.append(tmp.left)
                    deque.append(tmp.right)
            if cur:
                res.append(cur)
        return res

'''
Operations: 双端队列：dq = collection.deque()

dq.append(x)
dq.appendleft(x)
dq.count(x)  # count the number of deque elements equal to x
dq.popleft()
dq.remove(x)
dq.reverse()
see detail: https://docs.python.org/2/library/collections.html
'''       
# @lc code=end

