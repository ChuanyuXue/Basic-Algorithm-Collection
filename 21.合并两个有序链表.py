#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = ListNode(None)
        head = p
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        while l1 != None:
            p.next = l1
            p = p.next
            l1 = l1.next
        while l2 != None:
            p.next = l2
            p = p.next
            l2 = l2.next
        return head.next
# @lc code=end

