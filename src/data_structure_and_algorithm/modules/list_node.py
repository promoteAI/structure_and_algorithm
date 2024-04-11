"""
链表节点定义类
File: link_node.py
Author: Hanjiang Chen
email:chen_han_jiang@163.com
"""


class ListNode:
    """链表节点类"""

    def __init__(self, val, next=None):
        self.val = val  # 节点值
        self.next: ListNode = next  # 后继节点

    def __repr__(self):
        return f"{self.val} -> {self.next}"


def list_to_linklist(arr: list) -> ListNode:
    """列表转换成链表"""
    dum = head = ListNode(0)
    for a in arr:
        node = ListNode(a)
        head.next = node
        head = head.next
    return dum.next


def linklist_to_list(head: ListNode) -> list:
    """链表转换成列表"""
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res
