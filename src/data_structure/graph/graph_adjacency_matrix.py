"""
基于邻接矩阵的图
File: graph_adjacency_matrix.py
Author: Hanjiang Chen
email:chen_han_jiang@163.com
"""
from typing import List


class GraphAdjMatrix:
    def __init__(self, vertices: List[int], edges: List[List[int]]):
        """构造方法"""
        # 顶点列表，元素代表“顶点值”，索引代表“顶点索引”
        self.vertices = []
        # 邻接矩阵，行列索引代表“顶点索引”
        self.adj_matrix = []
        # 添加顶点
        for val in vertices:
            self.adj_vertex(val)
        # 添加边
        for edge in edges:
            self.add_edge(edge[0], edge[1])

    def size(self):
        return len(self.adj_matrix)


if __name__ == '__main__':
    # 初始化无向图
    vertices = [1, 3, 2, 5, 4]
    edges = [[0, 1], [0, 3], [1, 2], [2, 3], [2, 4], [3, 4]]
    graph = GraphAdjMatrix(vertices, edges)
    graph.print()
