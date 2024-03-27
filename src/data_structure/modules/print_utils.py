from .tree_node import TreeNode

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
    """打印二叉树"""
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
