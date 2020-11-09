#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Catalan: Cn=1/(n+1)*(2n)!/n!
卡特兰数可用于求解的：
1. n对括号有多少中匹配方式？
2. 进栈出栈的问题？
3. 有多少个二叉搜索树的问题?
'''


'''
Note: DP，tomorrow!!!
'''
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n: return []
        def new_tree(start, end):
            if start > end:
                return [None]
            res = []
            for i in range(start, end+1):
                #left-hand tree
                left_trees = new_tree(start, i-1)
                # right-hand tree
                right_trees = new_tree(i+1, end)

                for left in left_trees:
                    for right in right_trees:
                        tree = TreeNode(i)
                        tree.left = left
                        tree.right = right
                        res.append(tree)
            print(res)
            return res
        return new_tree(1,n) 
# @lc code=end

