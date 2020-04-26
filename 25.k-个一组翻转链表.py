#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 定义一个哨兵节点
        sentry = ListNode(0)
        pre = sentry
        start = head
        flag = True
        while head:
            for i in range(k):
                if not head:
                    # 剩余节点数量小于k，跳出
                    flag = False
                    break
                head = head.next
            if not flag:
                break
            # 上次翻转后的节点连接这次翻转后的节点
            pre.next = self.reverse(start,head)
            # 连接这次翻转以后的正常节点
            start.next = head
            # 更新位置
            pre = start
            # 更新位置
            start = head
        return sentry.next

    def reverse(self,start,end):
        pre, cur, nexts = None, start, start
        # 三个指针进行局部翻转
        while cur != end:
            nexts = nexts.next
            # 箭头反指
            cur.next = pre
            # 更新pre位置
            pre = cur 
            # 更新cur位置
            cur = nexts
        return pre

            
# @lc code=end

