#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def show_list(node):
    while node:
        print(node.val)
        node = node.next
        

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not (head and head.next):
            return head
        hp = head
        lenth = 0
        while head.next:
            lenth += 1
            head = head.next
        lenth += 1
        head.next = hp
        k = lenth - k % lenth - 1
        while k:
            hp = hp.next
            k -= 1
        result = hp.next
        hp.next = None
        return result
# @lc code=end

a = Solution()
L = [ListNode(x) for x in range(1,6)]
for i,v in enumerate(L[:-1]):
    v.next = L[i+1]
show_list(a.rotateRight(L[0], 2))

