#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(None)
        p = head
        flag = True
        while flag:
            min_node = ListNode(1e9)
            min_index = None
            flag = False
            for index, each_node in enumerate(lists):
                if each_node and each_node.val < min_node.val:
                    min_node = each_node
                    min_index = index
                    flag = True
            if flag:
                lists[min_index] = lists[min_index].next
                head.next = min_node
                head = head.next
                if not lists[min_index]:
                    lists.pop(min_index)
        return p.next
# @lc code=end

