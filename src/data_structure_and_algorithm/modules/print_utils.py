from .tree_node import TreeNode, list_to_tree
from typing import List


def print_matrix(matrix: List[List[int]]):
    """打印矩阵"""
    res = []
    for arr in matrix:
        res.append("    "+str(arr))
    print("[\n" + ",\n".join(res) + "\n]")


class Trunk:
    def __init__(self, prev, string: str):
        self.prev = prev
        self.string = string


def show_trunks(p: Trunk or None = None):
    if p is None:
        return
    show_trunks(p.prev)
    print(p.string, end="")


def print_tree(root: TreeNode, prev: Trunk or None = None, is_right: bool = False):
    """
    从右到左打印二叉树
    例如:
         /—— 3
     —— 1
       |    /—— 5
         \—— 2
             \—— 4
    """
    if root is None:
        return
    prev_str = "    "
    trunk = Trunk(prev, prev_str)
    print_tree(root.right, trunk, True)

    if prev is None:
        trunk.string = "——"
    elif is_right:
        trunk.string = "/——"
        prev_str = "  |"
    else:
        trunk.string = "\——"
        prev.string = prev_str
    show_trunks(trunk)
    print(" " + str(root.val))
    if prev:
        prev.string = prev_str
    trunk.string = "  |"
    print_tree(root.left, trunk, False)


def print_heap(heap: List[int]):
    """打印堆"""
    print("堆的数组表示：", heap)
    print("堆的树状表示：")
    root: TreeNode or None = list_to_tree(heap)
    print_tree(root)
