#
# @lc app=leetcode.cn id=142 lang=python
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# ------------------------------------
# 数学推导-> nb
# 了解了while true 的语句
# Python continue 语句跳出本次循环，而break跳出整个循环。
# continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
# continue语句用在while和for循环中。
# 逻辑运算中 not > and > or

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return 
            fast, slow = fast.next.next, slow.next
            if fast == slow: break 
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
# @lc code=end

