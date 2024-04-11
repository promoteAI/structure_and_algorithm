#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     :2024/4/11 16:50
# @Author   :Hanjiang Chen
# @Email    :chen_han_jiang@163.com
# @Project  :structure_and_algorithm 
# @File     :back_track.py
# @Software :PyCharm
"""
框架代码:回溯问题的通用解题模版:
本质：深度优先搜索算法
reference:
https://www.hello-algo.com/chapter_backtracking/backtracking_algorithm/
"""
from typing import List
from abc import abstractmethod


class BackTrack:
    """继承此类,重写模版中方法"""

    @abstractmethod
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
                self.back_track(state, choices, res)
                # 回退
                self.undo_choice(state, choice)

    @abstractmethod
    def is_solution(self, state):
        pass

    @abstractmethod
    def record_solution(self, state, res):
        pass

    @abstractmethod
    def is_valid(self, state, choice):
        pass

    @abstractmethod
    def make_choice(self, state, choice):
        pass

    @abstractmethod
    def undo_choice(self, state, choice):
        pass
