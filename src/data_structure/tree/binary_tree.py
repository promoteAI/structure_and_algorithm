"""
二叉树
File: binary_tree.py
Author: Hanjiang Chen
email:chen_han_jiang@163.com
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import TreeNode,print_tree

if __name__ == '__main__':
    # 初始化二叉树
    # 初始化节点
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    # 构建节点之间的引用（指针）
    n1.left=n2
    n1.right=n3
    n2.left=n4
    n2.right=n5
    print("\n初始化二叉树\n")
    print_tree(n1)
