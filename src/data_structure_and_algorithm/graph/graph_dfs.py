"""
深度优先遍历
Author: Hanjiang Chen
email:chen_han_jiang@163.com
"""
import sys
from pathlib import Path
from typing import List, Dict

sys.path.append(str(Path(__file__).parent.parent))

from modules import Vertex, list_to_vertex, vertex_to_list
from collections import deque
from graph_adjacency_list import GraphAdjList


class GraphDFS:
    """
    DFS是一种优先走到底、无路可走再回头的遍历方式。
    主要思路:

    """

    def __init__(self, graph: GraphAdjList, start_vet: Vertex):
        self.graph = graph
        self.start_vet = start_vet
        # 记录最终遍历顶点序列
        self.res = []
        # 记录访问过的顶点
        self.visited = set()

    def dfs(self) -> List[Vertex]:
        """深度优先遍历"""
        # 记录最终遍历顶点序列
        self.res.append(self.start_vet.val)
        # 记录访问过的顶点,并加入开始顶点
        self.visited.add(self.start_vet)
        # 遍历该顶点所有邻接接顶点
        for adj_vet in self.graph.adj_list[self.start_vet]:
            if adj_vet in self.visited:
                continue
            self.start_vet = adj_vet
            # 递归访问子节点
            self.dfs()
        return self.res


if __name__ == '__main__':
    # 初始化无向图
    v = list_to_vertex([1, 3, 2, 5, 4])
    print(v)
    edges = [
        [v[0], v[1]],
        [v[0], v[3]],
        [v[1], v[2]],
        [v[2], v[3]],
        [v[2], v[4]],
        [v[3], v[4]]]
    graph = GraphAdjList(edges)
    print("\n初始化后的图:")
    graph.print()

    # 深度优先遍历
    res = GraphDFS(graph, start_vet=v[2]).dfs()
    print("深度优先遍历结果", res)
