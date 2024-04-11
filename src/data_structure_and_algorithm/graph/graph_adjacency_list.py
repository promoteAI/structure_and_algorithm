"""
基于邻接表的无向图
File: graph_adjacency_list.py
Author: Hanjiang Chen
email:chen_han_jiang@163.com
"""
import sys
from pathlib import Path
from typing import List, Dict

sys.path.append(str(Path(__file__).parent.parent))

from modules import Vertex, list_to_vertex, vertex_to_list


class GraphAdjList:
    """基于邻接表的无向图"""

    def __init__(self, edges: List[List[Vertex]]):
        """构造方法"""
        # 邻接表 key:顶点索引, value:该顶点的所有邻接顶点
        self.adj_list: Dict[Vertex:List[Vertex]] = dict()
        # 初始化邻接表
        for edge in edges:
            self.add_vertex(edge[0])
            self.add_vertex(edge[1])
            self.add_edge(edge[0], edge[1])

    def add_vertex(self, vet: Vertex):
        """添加顶点"""
        if vet in self.adj_list:
            return
        # 添加一个新的链表
        self.adj_list[vet] = []

    def add_edge(self, vet1: Vertex, vet2: Vertex):
        """添加边"""
        # 判断
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1 == vet2:
            raise ValueError("顶点不存在")
        # 添加边 vet1-vet2
        self.adj_list[vet1].append(vet2)
        self.adj_list[vet2].append(vet1)

    def remove_edge(self, vet1: Vertex, vet2: Vertex):
        """删除边"""
        # 判断
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1 == vet2:
            raise ValueError()
        # 删除边 vet1-vet2
        self.adj_list[vet1].remove(vet2)
        self.adj_list[vet2].remove(vet1)

    def remove_vertex(self, vet: Vertex):
        """删除顶点"""
        # 判断
        if vet not in self.adj_list:
            raise ValueError("顶点不存在")
        # 删除顶点
        self.adj_list.pop(vet)
        # 删除所有与该顶点相关的边
        for vertex in self.adj_list:
            if vet in self.adj_list[vertex]:
                self.adj_list[vertex].remove(vet)

    def size(self):
        return len(self.adj_list)

    def print(self):
        """打印邻接表"""
        print("邻接表 =")
        for vertex in self.adj_list:
            tmp = [v.val for v in self.adj_list[vertex]]
            print(f"{vertex.val} -> {tmp}")


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

    # 添加边
    graph.add_edge(v[0], v[2])
    print("\n添加边后的图:")
    graph.print()

    # 删除边
    graph.remove_edge(v[0], v[2])
    print("\n删除边后的图:")
    graph.print()

    # 添加顶点
    graph.add_vertex(Vertex(6))
    print("\n添加顶点后的图:")
    graph.print()

    # 删除顶点
    graph.remove_vertex(v[1])
    print("\n删除顶点后的图:")
    graph.print()
