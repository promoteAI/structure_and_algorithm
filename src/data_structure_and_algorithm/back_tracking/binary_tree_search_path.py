#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     :2024/4/11 17:36
# @Author   :Hanjiang Chen
# @Email    :chen_han_jiang@163.com
# @Project  :structure_and_algorithm 
# @File     :binary_tree_search_path.py
# @Software :PyCharm
from back_track import BackTrack

class BinaryTreeSearchPath(BackTrack):
    """
    在二叉树中搜索所有值为7的节点，请返回根节点到这些节点的路径，并要求路径中不包含值为3的节点。
    """

    def __init__(self):
        super.__init__(self, BinaryTreeSearchPath)

    def is_solution(self, state):
        return state and state[-1].val==7

    def record_solution(self, state, res):
        res.append(state)

    def is_valid(self, state, choice):
        return not choice and state[-1].val!=3

    def make_choice(self, state, choice):
        choice.append(state)

    def undo_choice(self, state, choice):
        choice.pop()


if __name__ == '__main__':
    root = list_to_tree([1, 7, 3, 4, 5, 6, 7])
    # 回溯算法
    res = []
    backtrack(state=[], choices=[root], res=res)
    print("\n输出所有路径")
    for path in res:
        print([node.val for node in path])
