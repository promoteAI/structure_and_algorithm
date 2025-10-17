"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 

提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
"""

def judge_ch_exist(s:str):
     # 使用hash
     hash:dict={}
     for i in range(len(s)):
          if s[i] in hash:
               return True
          else:
               hash[s[i]]=1 
     return False

# 暴力解法
def longest_substring(s:str):
     # 遍历
     n=len(s)
     max_len=0
     for i in range(n):
          for j in range(i+1,n+1):
               # 子串
               sub_str=s[i:j]
               # 判断子串中是否存在重复字符
               if not judge_ch_exist(sub_str):
                    # 计算子串长度
                    max_len=max(max_len,j-i)
     return max_len

print(longest_substring(s="abcabcbb"))
print(longest_substring(s="bbbbb"))
print(longest_substring(s="pwwkew"))
print(longest_substring(s="au"))
print(longest_substring(s=" "))