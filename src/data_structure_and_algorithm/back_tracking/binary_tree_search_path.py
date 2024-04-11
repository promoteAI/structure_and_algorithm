#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     :2024/4/11 17:36
# @Author   :Hanjiang Chen
# @Email    :chen_han_jiang@163.com
# @Project  :structure_and_algorithm 
# @File     :binary_tree_search_path.py
# @Software :PyCharm
from typing import List
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from back_track import BackTrack
from modules.tree_node import list_to_tree
from modules.print_utils import print_tree


class BinaryTreeSearchPath(BackTrack):
    """
    在二叉树中搜索所有值为7的节点，请返回根节点到这些节点的路径，并要求路径中不包含值为3的节点。
    """

    def back_track(self, state, choices: List, res: List):
        """
        回溯算法框架
        :param state: 表示问题的当前状态
        :param choices: 表示当前状态下可以做出的选择
        :param res: 记录解
        :return:
        """
        # 判断是否为解
        if self.is_solution(state):
            # 记录解
            self.record_solution(state, res)
            # 不再继续搜索
            return
        # 遍历所有的选择
        for choice in choices:
            # 剪枝：判断选择是否合法
            if self.is_valid(state, choice):
                # 尝试：做出选择，更新状态
                self.make_choice(state, choice)
                # 进行下一轮选择
                self.back_track(state, [choice.left, choice.right], res)
                # 回退
                self.undo_choice(state, choice)

    def is_solution(self, state):
        return state and state[-1].val == 7

    def record_solution(self, state, res):
        res.append(list(state))

    def is_valid(self, state, choice):
        return choice is not None and choice.val != 3

    def make_choice(self, state, choice):
        state.append(choice)

    def undo_choice(self, state, choice):
        state.pop()


if __name__ == '__main__':
    root = list_to_tree([1, 7, 3, 4, 5, 6, 7])
    print_tree(root)
    # 回溯算法
    res = []
    backtrack = BinaryTreeSearchPath()
    backtrack.back_track(state=[], choices=[root], res=res)
    print("\n输出所有路径")
    for path in res:
        print([node.val for node in path])
