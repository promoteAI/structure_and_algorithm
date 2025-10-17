"""
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

示例：

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
"""

class DLinkNode:
    def __init__(self,k=0,v=0):
        self.k = k
        self.v = v
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        # 伪头部和尾部node，构造初始缓存双向链表
        self.head = DLinkNode()
        self.tail = DLinkNode()
        # 指针关系
        self.head.next = self.tail
        self.tail.pre = self.head
        # 大小
        self.size = 0

    def moveToHead(self,node:DLinkNode):
        self.removeNode(node)
        # 添加到头部
        self.addToHead(node)

    def addToHead(self,node:DLinkNode):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

    def removeNode(self,node:DLinkNode):
        # 移除node
        node.pre.next = node.next
        node.next.pre = node.pre
    
    def removeTail(self):
        # 移除靠近链表尾部的节点
        node = self.tail.pre
        self.removeNode(node)
        return node

    # 获取
    def get(self, k: int) -> int:
        """
        对于 get 操作，首先判断 k 是否存在：

        如果 k 不存在，则返回 −1；

        如果 k 存在，则 k 对应的节点是最近被使用的节点。
        通过哈希表定位到该节点在双向链表中的位置，并将其移动到双向链表的头部，最后返回该节点的值。
        """
        if k not in self.cache:
            return -1
        # 定位
        node = self.cache[k]
        # 移动
        self.moveToHead(node)
        return node.v
    # 添加
    def put(self, k: int, v: int) -> None:
        """
        对于put操作，首先判断k是否存在
        - 如果k不存在，使用k，v创建，添加到双向链表头部，并将k添加在=到cache，
        然后判断节点数是否超出容量，超出则删除双向链表尾部节点，并删除cache中的k
        - 如果k存在，则更新v值，并将其移到头部
        """
        if k not in self.cache:
            # 创建node
            node = DLinkNode(k,v)
            # 添加到头部
            self.addToHead(node)
            self.cache[k]=node
            self.size +=1
            if self.size > self.capacity:
                node=self.removeTail()
                print(node.k)
                self.cache.pop(node.k)
                self.size -=1
        else:
            # 更新cache的v值
            node=self.cache[k]
            node.v = v
            self.moveToHead(node)
        


if __name__ == "__main__":
    lru_cache = LRUCache(2)
    print(lru_cache.put(1, 1))    # 缓存是 {1=1}
    print(lru_cache.put(2, 2))    # 缓存是 {1=1, 2=2}
    print(lru_cache.get(1))       # 返回 1
    print(lru_cache.put(3, 3))    # 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
    print(lru_cache.get(2))       # 返回 -1 (未找到)
    print(lru_cache.put(4, 4))    # 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
    print(lru_cache.get(1))       # 返回 -1 (未找到)
    print(lru_cache.get(3))       # 返回 3
    print(lru_cache.get(4))       # 返回 4