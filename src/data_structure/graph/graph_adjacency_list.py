"""
基于邻接表的无向图
File: graph_adjacency_list.py
Author: Hanjiang Chen
email:chen_han_jiang@163.com
"""
import sys
from pathlib import Path
from typing import List

sys.path.append(str(Path(__file__).parent.parent))

from modules import print_matrix


class GraphAdjList:
    """基于邻接表的无向图"""
    def __init__(self, vertices: List[int], edges: List[List[int]]):
        """构造方法"""
        # 顶点列表，元素代表“顶点值”，索引代表“顶点索引”
        self.vertices = []
        # 邻接矩阵，行列索引代表“顶点索引”
        self.adj_matrix = []
        # 添加顶点
        for val in vertices:
            self.add_vertex(val)
        # 添加边
        for edge in edges:
            self.add_edge(edge[0], edge[1])

    def add_vertex(self, val: int):
        """添加顶点"""
        n = self.size()
        # 向顶点列表中添加新顶点的值
        self.vertices.append(val)
        # 在邻接矩阵中添加一行
        new_row = [0] * n
        self.adj_matrix.append(new_row)
        # 在邻接矩阵中添加一列
        for row in self.adj_matrix:
            row.append(0)

    def add_edge(self, i: int, j: int):
        """添加边"""
        # 参数 i, j 对应 vertices 元素索引
        # 索引越界与相等处理
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError()
        # 在无向图中，邻接矩阵关于主对角线对称，即满足 (i, j) == (j, i)
        self.adj_matrix[i][j] = 1
        self.adj_matrix[j][i] = 1

    def remove_edge(self, i: int, j: int):
        """删除边"""
        # 参数 i, j 对应 vertices 元素索引
        # 索引越界与相等处理
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError()
        # 将[i,j]和[j,i]处值置为0
        self.adj_matrix[i][j] = 0
        self.adj_matrix[j][i] = 0

    def remove_vertex(self, i: int):
        """删除顶点"""
        if i < 0 or i >= self.size():
            raise IndexError()
        # 将顶点索引 i 对应的行和列置为0
        for j in range(self.size()):
            self.adj_matrix[i][j] = 0
            self.adj_matrix[j][i] = 0

    def size(self):
        return len(self.adj_matrix)

    def print(self):
        """打印邻接矩阵"""
        print("顶点列表 =", self.vertices)
        print("邻接矩阵 =")
        print_matrix(self.adj_matrix)


if __name__ == '__main__':
    # 初始化无向图
    vertices = [1, 3, 2, 5, 4]
    edges = [[0, 1], [0, 3], [1, 2], [2, 3], [2, 4], [3, 4]]
    graph = GraphAdjMatrix(vertices, edges)
    graph.print()

    # 删除边
    graph.remove_edge(0, 3)
    graph.print()

    # 删除顶点
    graph.remove_vertex(4)
    graph.print()

    # 添加顶点
    graph.add_vertex(6)
    graph.print()

    # 添加边
    graph.add_edge(3, 5)
    graph.print()
