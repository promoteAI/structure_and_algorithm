"""
python 内置列表
File:list.py
Author: Hanjiang Chen
email:chen_han_jiang@163.com
"""

if __name__=="__main__":
    #初始化
    nums=[1,2,5,4,3]
    print(nums)
    # 索引访问
    x:int=nums[2]
    print(x)
    # 更新
    nums[2]=10
    print(nums)
    # 清空
    nums.clear()
    print(nums)
    # 尾部添加
    nums.append(11)
    nums.append(23)
    nums.append(56)
    nums.append(33)
    nums.append(18)
    print(nums)
    # 中间插入
    nums.insert(3,100)
    print(nums)
    # 删除
    nums.pop(3)
    print(nums)
    # 索引遍历
    count=0
    for i in range(len(nums)):
        count+=nums[i]
    # 直接遍历
    for num in nums:
        count+=num
    print(count)

    # 拼接列表
    nums1=[1,2,3]
    nums+=nums1
    print(nums)
    # 排序
    nums.sort()
    print(nums)