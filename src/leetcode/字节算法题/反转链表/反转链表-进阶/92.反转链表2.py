"""
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
 

示例 1：


输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]
示例 2：

输入：head = [5], left = 1, right = 1
输出：[5]
"""
from ast import dump
import typing


from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 法1,遍历两次
def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    # 使用虚拟头结点，避免复杂情况讨论
    dummy_head = ListNode(-1)
    dummy_head.next = head
    pre = dummy_head
    # 第一步，走left-1,来到left前一个节点
    for _ in range(left-1):
        pre = pre.next

    # 第 2 步：从 pre 再走 right - left + 1 步，来到 right 节点
    # 记录右侧链表
    right_node = pre
    for _ in range(right-left+1):
        right_node = right_node.nextimage.png
    
    # 截取子链
    left_node = pre.next
    cur = right_node.next
    # 切断链接
    pre.next =None
    right_node.next =None

    # 反转子链
    def reverseLinkList(head:ListNode):
        # 反转
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

    reverseLinkList(left_node)

    # 拼接
    pre.next = right_node
    left_node.next = cur

    return dummy_head.next


# 法2,遍历一次，穿针引线