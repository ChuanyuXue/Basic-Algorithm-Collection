#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import *

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = 0
        lenth = 0
        p = head
        while p != None:
            p = p.next
            lenth = lenth + 1

        if lenth == n:
            return head.next
        
        copy = head
        while count != lenth - n:
            last_point = head
            head = head.next
            count = count + 1
        last_point.next = head.next
        return copy
        
# @lc code=end

p1 = ListNode(1)
p2 = ListNode(2)
p1.next = p2

a = Solution()
a.removeNthFromEnd(p1, 2)
