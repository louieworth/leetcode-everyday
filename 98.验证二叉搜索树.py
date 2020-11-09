#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归的办法
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # stack = []
        # pre = None
        # p = root
        # while p or stack:
        #     while p:
        #         stack.append(p)
        #         p = p.left
        #     p = stack.pop()
        #     if pre and p.val <= pre.val:
        #         return False
        #     pre = p
        #     print('pre:',pre)
        # return True


        # 递归的办法
        # 利用float('inf')创建上下值域
        def dfs(node, min_val, max_val):
            if not node:
                return True #退出条件
            if not min_val < node.val < max_val:
                return False
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

        return dfs(root, float('-inf'), float('inf'))   
# @lc code=end

