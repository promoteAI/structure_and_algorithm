"""
树节点
File: tree_node.py
Author: Hanjiang Chen
email:chen_han_jiang@163.com
"""
from typing import List


class TreeNode(object):
    """二叉树节点类"""

    def __init__(self, val):
        self.val = val  # 节点的值
        self.height = 0  # 节点高度
        self.left = None
        self.right = None

    # 二叉树的数组表示：
    # [1, 2, 3, 4, None, 6, 7, 8, 9, None, None, 12, None, None, 15]
    # 二叉树的链表表示：
    #             /——— 15
    #         /——— 7
    #     /——— 3
    #    |    \——— 6
    #    |        \——— 12
    # ——— 1
    #     \——— 2
    #        |    /——— 9
    #         \——— 4
    #             \——— 8


def list_to_tree_dfs(arr: List, i: int) -> TreeNode or None:
    """将列表反序列化为二叉树：递归"""
    if i < len(arr) and arr[i] is not None:
        root = TreeNode(arr[i])
        root.left = list_to_tree_dfs(arr, 2 * i + 1)
        root.right = list_to_tree_dfs(arr, 2 * i + 2)
        return root
    else:
        return None


def list_to_tree(arr: List[int]) -> TreeNode or None:
    """将列表反序列化为二叉树"""
    return list_to_tree_dfs(arr, 0)


def tree_to_list_dfs(root: TreeNode, i: int, res: List) -> List[int]:
    """将二叉树序列化为列表：递归"""
    if root is None:
        return
    if i >= len(res):
        res += [None] * (i - len(res) + 1)
    res[i] = root.val
    tree_to_list_dfs(root.left, 2 * i + 1, res)
    tree_to_list_dfs(root.right, 2 * i + 2, res)


def tree_to_list(root: TreeNode) -> List[int]:
    """将二叉树序列化为列表"""
    res = []  # 记录转换后的结果
    tree_to_list_dfs(root, 0, res)
    return res
