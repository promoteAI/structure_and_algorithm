"""
基础题目：对应leetcode-20题
给定一个只包括 '('，')'的字符串，判断字符串是否有效。注：空字符串属于有效字符串
示例 1:
输入: "(())"
输出: true

 实例 2：
 输入: "())("
输出: false
"""
# 解题思路：使用栈

# 基础解法，时间复杂度O(n)，空间复杂度O(n)
def is_valid(s:str):
    # 判断是否为空
    if len(s)==0:
        return True
    # 创建空栈
    stack:list=[]
    # 遍历
    for i in range(len(s)):
        if s[i]=="(":
            stack.append(s[i])
        elif s[i]==")":
            if len(stack)==0:
                return False
            else:
                stack.pop(-1)
    # 判断栈是否为空
    if len(stack)!=0:
        return False
    else:
        return True


# 测试
print(is_valid(s="(())"))
print(is_valid(s="())("))