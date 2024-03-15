"""
链表
File: link_list.py
Author: Hanjiang Chen
email:chen_han_jiang@163.com
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import ListNode


def insert(n0: ListNode, P: ListNode):
    """ 在链表的节点n0之后插入节点P """
    n1 = n0.next
    P.next = n1
    n0.next = P


def remove(n0: ListNode):
    """ 删除链表的节点n0之后的首个节点"""
    if not n0.next:
        return
    # n0->P->n1
    P = n0.next
    n1 = P.next
    n0.next = n1


def access(head: ListNode, index: int) -> ListNode:
    """访问链表中索引为 index 的节点"""
    for _ in range(index):
        if not head:
            return None
        head = head.next
    return head


def find(head: ListNode, target: int) -> int:
    """ 查找链表中第一个值等于target的节点,返回其索引 """
    cur = head
    index = 0
    while cur:
        if cur.val == target:
            return index
        cur = cur.next
        index += 1
    return -1


if __name__ == '__main__':
    node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    print(node)
    # 插入
    insert(node, ListNode(6, None))
    print(node)
    # 删除
    remove(node)
    print(node)
    # 查找
    x = find(node, 3)
    print(x)
    # 访问
    x = access(node, 2)
    print(x.val)
