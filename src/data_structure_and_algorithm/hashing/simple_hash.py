"""
简易哈希实现:
File: simple_hash.py
Author: Hanjiang Chen
email:chen_han_jiang@163.com
"""


def add_hash(key: str) -> int:
    """加法哈希:对输入的每个字符的 ASCII 码进行相加，将得到的总和作为哈希值。"""
    hash = 0
    m = 1000000007
    for c in key:
        hash += ord(c)
    return hash % m


def multiply_hash(key: str) -> int:
    """乘法哈希:利用乘法的不相关性，每轮乘以一个常数，将各个字符的 ASCII 码累积到哈希值中。"""
    hash = 0
    m = 1000000007
    a = 263
    for c in key:
        hash = a * hash + ord(c)
    return hash % m


def xor_hash(key: str) -> int:
    """异或哈希:将输入数据的每个元素通过异或操作累积到一个哈希值中。"""
    hash = 0
    m = 1000000007
    for c in key:
        hash ^= ord(c)
    return hash % m


def rot_hash(key: str) -> int:
    """旋转哈希:将每个字符的 ASCII 码累积到一个哈希值中，每次累积之前都会对哈希值进行旋转操作。"""
    hash = 0
    m = 1000000007
    for c in key:
        hash = (hash << 4) ^ (hash >> 28) ^ ord(c)
    return hash % m


if __name__ == '__main__':
    key = "鞠婧祎,我爱你"
    # 加法哈希
    h = add_hash(key)
    print(h)
    # 乘法哈希
    h = multiply_hash(key)
    print(h)
    # 异或哈希
    h = xor_hash(key)
    print(h)
    # 旋转哈希
    h = rot_hash(key)
    print(h)
