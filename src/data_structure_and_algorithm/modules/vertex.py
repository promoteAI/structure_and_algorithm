from typing import List


class Vertex:
    """顶点类"""

    def __init__(self, val: int):
        self.val = val


def list_to_vertex(vals: List[int]) -> List[Vertex]:
    """
    将列表转换为顶点列表
    """
    return [Vertex(val) for val in vals]


def vertex_to_list(vets: List[Vertex]) -> List[int]:
    """
    将顶点列表转换为列表
    """
    return [vet.val for vet in vets]
