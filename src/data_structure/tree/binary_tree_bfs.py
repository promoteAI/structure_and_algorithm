"""
二叉树广度优先遍历,又叫层次遍历
File: binary_tree_bfs.py
Author: Hanjiang Chen
email:chen_han_jiang@163.com
"""
import sys
from pathlib import Path
from typing import List

sys.path.append(str(Path(__file__).parent.parent))
from modules import TreeNode, print_tree, list_to_tree, tree_to_list
from collections import deque


class BiTreeBfs:

    def __init__(self, res: List):
        self.res = res  # 最终结果
        self.queue = deque()  # 维持队列

    def level_order(self, root: TreeNode or None):
        """层次遍历:维持一个队列，每次从队列中取出一个节点，并访问该节点，然后将该节点的左右子节点入队"""
        # 将root入队
        self.queue.append(root)
        while self.queue:
            # 从队列中取出一个节点，加入列表
            node = self.queue.popleft()
            self.res.append(node.val)

            # 将当前左子节点入队
            if node.left:
                self.queue.append(node.left)

            # 将当前右子节点入队
            if node.right:
                self.queue.append(node.right)


if __name__ == '__main__':
    # 构建二叉树
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = list_to_tree(arr)
    print_tree(root)

    # 层次遍历
    arr = []
    bi_tree = BiTreeBfs(arr)
    bi_tree.level_order(root)
    print("层次遍历结果:", arr)
