#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def get_str(l1):
    a = ''
    while(l1 != None):
        a = a + str(l1.val)
        l1 = l1.next
    return a

def format(val):
    phead = None
    for x in str(val):
        if phead == None:
            phead = ListNode(int(x))
        else:
            pnext = ListNode(int(x))
            pnext.next = phead
            phead = pnext
    return phead

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a, b = get_str(l1)[::-1], get_str(l2)[::-1]
        return format(int(a) + int(b))
        
# @lc code=end

a = Solution()
a.addTwoNumbers(ListNode(3), ListNode(5))
