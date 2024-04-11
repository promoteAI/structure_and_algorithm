"""
哈希表
File: hash_map.py
Author: Hanjiang Chen
email:chen_han_jiang@163.com
"""

if __name__ == '__main__':
    # 初始化哈希表
    hmap={}
    # 添加
    hmap[1]="赵丽颖"
    hmap[2]="娜扎"
    hmap[3]="袁冰妍"
    hmap[4]="迪丽热巴"
    hmap[5]="杨幂"
    print(hmap)
    # 修改
    hmap[2]="鞠婧祎"
    print(hmap)
    # 查询
    name=hmap[3]
    print(name)
    # 删除
    hmap.pop(1)
    print(hmap)

    # 遍历哈希表
    # 遍历键值对
    for k,v in hmap.items():
        print(k,"-->",v)
    # 遍历键
    for k in hmap.keys():
        print(k)
    # 遍历值
    for v in hmap.values():
        print(v)
