"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
 

示例 1：


输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
示例 2：


输入：head = [1,2]
输出：[2,1]
示例 3：

输入：head = []
输出：[]
"""

class LinkNode:
    def __init__(self,v=0,next=None) -> None:
        self.v=v
        self.next=next


def reverse_linklist(head:LinkNode)->LinkNode:
    # 反转链表
    pre=None
    cur = head
    while cur:
        tmp=cur.next
        cur.next=pre
        pre=cur
        cur=tmp

    return pre

if __name__ == "__main__":
    # 构造链表1,2,3
    node1 = LinkNode(1)
    node2 = LinkNode(2)
    node3 = LinkNode(3)
    node1.next=node2
    node2.next=node3
    # 调用
    reverse_linklist(head=node1)