# 滑动窗口
def longest_substring(s:str):
     # 遍历
     l=0
     r=0
     n=len(s)
     max_len=0
     hash:dict={}
     while l<n and r<n:
        if s[r] not in hash: # 不存在重复字符时将字符存储入hash，并将右边指针向后移动一位
            hash[s[r]]=1
            r+=1
            max_len=max(max_len,r-l)
        else: # 存在重复元素，则将左边指针向右移动一位(删除与当前相同的字符)
            hash.pop(s[l])
            l+=1
     return max_len

print(longest_substring(s="abcabcbb"))
print(longest_substring(s="bbbbb"))
print(longest_substring(s="pwwkew"))
print(longest_substring(s="au"))
print(longest_substring(s=" "))