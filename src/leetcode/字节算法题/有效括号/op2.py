"""
题目更改：对应leetcode-32题
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
"""

# 利用栈存储下标：枚举所有子串并判断有效性
def longestValidParentheses(s: str) -> int:
    stack=[-1] # 开始将-1入栈，初始化，避免无法计算max_len
    max_len = 0
    n = len(s)
    for i in range(n):
        if s[i]=="(":
            stack.append(i)
        else:
            stack.pop()
            # 看栈顶是否为空，为空的话就不能作差了
            if not stack:
                stack.append(i);
            else:
                max_len=max(max_len,i-stack[-1])
                
    return max_len

# 测试
print(longestValidParentheses("(()"))      # 输出: 2
print(longestValidParentheses(")()())"))   # 输出: 4