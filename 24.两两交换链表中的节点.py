#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next == None:
            return head

        previous_p = ListNode(None)
        copy = previous_p
        left_p = head
        right_p = left_p.next

        while left_p and right_p:
            left_p.next = right_p.next
            right_p.next = left_p
            previous_p.next = right_p
            
            if left_p.next != None:
                previous_p = right_p.next
                left_p = left_p.next
                right_p = left_p.next
            else:
                break

        return copy.next
        

# @lc code=end

