# 优化空间复杂度O(n)-->O(1),使用指针
def is_valid(s:str):
    # 判断是否为空
    if len(s)==0:
        return True
    # 创建变量，记录遇到（的数量
    p=0
    # 遍历
    for i in range(len(s)):
        if s[i]=="(":
            p+=1
        elif s[i]==")":
            if p==0:
                return False
            else:
                p-=1
    # 判断栈是否为空
    if p!=0:
        return False
    else:
        return True


# 测试
print(is_valid(s="(())"))
print(is_valid(s="())("))