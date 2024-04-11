"""
栈：先入后出
File: stack.py
Author: Hanjiang Chen
email:chen_han_jiang@163.com
"""
from typing import List

if __name__ == '__main__':
    # 初始化栈
    # python中无内置的栈类，可以把list当做栈来使用
    stack: List[int] = []

    # 入栈
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    print("栈stack=", stack)
    # 访问栈顶元素
    top: int = stack[-1]
    print("栈顶元素top=", top)
    # 出栈
    pop: int = stack.pop()
    print("出栈元素pop=", pop)
    print("出栈后栈stack=", stack)

    # 获取栈的长度
    size: int = len(stack)
    print("栈的长度size=", size)

    # 判断是否为空
    is_empty: bool = len(stack) == 0
    print("栈是否为空=", is_empty)
