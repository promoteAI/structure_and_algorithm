#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     :2024/4/17 17:30
# @Author   :Hanjiang Chen
# @Email    :chen_han_jiang@163.com
# @Project  :code 
# @File     :count_line.py
# @Software :PyCharm

def count_lines(filename:str):
    """计算不同行出现的次数"""
    # 不能使用map/dict/set/hash结构存储，使用指针法计数
    pre_line=None
    count=0

    # 存储当前行的内容
    cur_line=""

    # 打开文件读取
    with open(filename,'r') as file:
        # 遍历文件
        for line in file:
            # 读取第一行
            if pre_line is None:
                pre_line=line
                count+=1
                continue

            # 比较当前行与上一行是否相等
            if line==pre_line:
                # 如果相等则增加计数
                count+=1
            else:
                # 如果不相等,将上一行的数量输出到终端，当然也可以使用将所有不同行拼接成一个大字符串输出
                print(f"{pre_line.strip()}:{count}")
                # 将当前行设置为新的上一行，并将数量置为1
                pre_line=line
                count=1
        # 处理最后一行
        if pre_line is not None:
            print(f"{pre_line.strip()}:{count}")

# 调用
count_lines("filename.txt")