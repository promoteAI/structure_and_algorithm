"""
二叉树深度优先遍历
File: binary_tree_dfs.py
Author: Hanjiang Chen
email:chen_han_jiang@163.com
"""
import sys
from pathlib import Path
from typing import List

sys.path.append(str(Path(__file__).parent.parent))
from modules import TreeNode, print_tree, list_to_tree, tree_to_list


class BiTreeDfs:

    def __init__(self, res):
        self.res = res

    def pre_order(self, root: TreeNode or None):
        if not root:
            return
        self.res.append(root.val)
        self.pre_order(root.left)
        self.pre_order(root.right)

    def in_order(self, root: TreeNode or None):
        if not root:
            return
        self.in_order(root.left)
        self.res.append(root.val)
        self.in_order(root.right)

    def post_order(self, root: TreeNode or None):
        if not root:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        self.res.append(root.val)


if __name__ == '__main__':
    # 构建二叉树
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = list_to_tree(arr)
    print_tree(root)

    # 先序遍历
    arr = []
    bi_tree = BiTreeDfs(arr)
    bi_tree.pre_order(root)
    print("先序遍历结果:", arr)

    # 中序遍历
    arr = []
    bi_tree = BiTreeDfs(arr)
    bi_tree.in_order(root)
    print("中序遍历结果:", arr)

    # 后序遍历
    arr = []
    bi_tree = BiTreeDfs(arr)
    bi_tree.post_order(root)
    print("后序遍历结果:", arr)
