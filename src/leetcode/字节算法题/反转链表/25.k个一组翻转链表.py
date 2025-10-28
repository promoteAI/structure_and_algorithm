"""
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
"""

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """k个一组反转"""
        # 统计节点数量
        n = 0
        cur = head
        while cur:
            n+=1
            cur=cur.next
            
        # 虚拟头节点
        dummy_head = ListNode(val=-1,next=head)
        p0 =dummy_head
        # 遍历，k个一组处理
        while n>=k:
            n-=k
            pre = None
            cur = p0.next
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            nxt = p0.next
            p0.next.next =cur
            p0.next = pre
            p0 = nxt

        return dummy_head.next



if __name__ == "__main__":
    # 构造链表1,2,3
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node5
    # 调用
    Solution().reverseKGroup(head=node1,k=3)