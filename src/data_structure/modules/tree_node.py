"""
树节点
File: tree_node.py
Author: Hanjiang Chen
email:chen_han_jiang@163.com
"""


class TreeNode(object):
    """二叉树节点类"""

    def __init__(self, val):
        self.val = val  # 节点的值
        self.left = None
        self.right = None
