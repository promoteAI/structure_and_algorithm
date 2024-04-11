"""
广度优先遍历
BFS 通常借助队列来实现
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


class GraphBFS:
    """
    BFS是一种由近及远的遍历方式，从某个节点出发，始终优先访问距离最近的顶点，并一层层向外扩张。
    主要思路:
        将遍历起始顶点 startVet 加入队列，并开启循环。
        在循环的每轮迭代中，弹出队首顶点并记录访问，然后将该顶点的所有邻接顶点加入到队列尾部。
        循环步骤 2. ，直到所有顶点被访问完毕后结束。
    """

    def __init__(self, graph: GraphAdjList, start_vet: Vertex):
        self.graph = graph
        # 初始化队列,并加入开始顶点
        self.queue = deque([start_vet])
        # 记录最终遍历顶点序列
        self.res = []
        # 记录访问过的顶点,并加入开始顶点
        self.visited = set([start_vet])

    def bfs(self) -> List[Vertex]:
        """广度优先遍历"""
        while self.queue:
            # 首顶点出队
            vet = self.queue.popleft()
            self.res.append(vet.val)
            # 将vet所有邻接顶点入队
            for adj_vet in self.graph.adj_list[vet]:
                # 判断当前是否访问过
                if adj_vet in self.visited:
                    continue
                self.queue.append(adj_vet)
                self.visited.add(adj_vet)

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

    # 广度优先遍历
    res = GraphBFS(graph, start_vet=v[4]).bfs()
    print("广度优先遍历结果:",res)
