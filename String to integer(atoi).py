class Solution:
    def myAtoi(self, s: str) -> int:  
        s=s.strip()
        if not s:
            return 0
        res=0
        sign=1
        if s[0]=="-":
            sign=-1
        elif s[0]=="+":
            sign=1
        elif not s[0].isdigit():
            return 0
        else:
            res=ord(s[0])-ord("0")
        for i in range(1,len(s)):
            if s[i].isdigit():
                res=res*10+(ord(s[i])-ord("0"))
            else:
                break
        res=res*sign
        if res<=-2**31:
            return -2**31
        elif res>=(2**31)-1:
            return (2**31)-1
        return res
