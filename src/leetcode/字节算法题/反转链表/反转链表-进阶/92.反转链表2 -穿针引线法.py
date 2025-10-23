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
from binhex import LINELEN
from tkinter import N
import typing


from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 法2,遍历一次，穿针引线

def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    # 设置dummy_node
    dummy_node = ListNode(-1)
    dummy_node.next = head
    pre = dummy_node
    for _ in range(left-1):
        pre = pre.next
    cur = pre.next
    next = cur.next
    for _ in range(left,right,1):
        next = cur.next
        cur.next = next.next
        next.next = pre.next 
        pre.next = next
    
    return dummy_node.next