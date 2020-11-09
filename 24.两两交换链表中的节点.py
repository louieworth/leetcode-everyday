#
# @lc app=leetcode.cn id=24 lang=python
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next):
            return head
        p = ListNode(-1) #初始化空节点
        cur, head, stack = head, p, []
        while cur and cur.next:
            _,_ = stack.append(cur), stack.append(cur.next)
            cur = cur.next.next
            p.next = stack.pop()
            p.next.next = stack.pop()
            p = p.next.next
        if cur:
            p.next = cur
        else:
            p.next = None
        return head.next
# 设置头节点为head， 当时需要处理的两个节点为cur，以及cur.next不断更新
# O(N)  O(1)
# @lc code=end

