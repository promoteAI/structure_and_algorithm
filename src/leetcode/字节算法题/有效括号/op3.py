# op2中栈可以使用变量存储，空间复杂度降低
def longestValidParentheses(s: str) -> int:
    l=0 # 记录"("的数量
    r=0 # 记录")"的数量
    max_len = 0
    n = len(s)
    # 从左往右遍历
    for i in range(n):
        if s[i]=="(":
            l+=1
        else:
            r+=1
        if l==r:
            max_len=max(max_len,2*r)
        elif r>l:
            l=r=0
    l=r=0
    # 从右往左遍历
    for i in range(n-1,-1,-1):
        if s[i]=="(":
            l+=1
        else:
            r+=1
        if l==r:
            max_len=max(max_len,2*r)
        elif r<l:
            l=r=0
    return max_len

# 测试
print(longestValidParentheses("(()"))      # 输出: 2
print(longestValidParentheses(")()())"))   # 输出: 4
