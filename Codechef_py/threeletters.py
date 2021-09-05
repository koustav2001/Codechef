t=int(input())
for i in range(t):
    s=input()
    f={}
    p=len(s)//3
    x=0
    for i in range(len(s)):
        if s[i] in f:
            f[s[i]]+=1
        else:
            f[s[i]]=1
    for i in f.values():
        if(i>=2):
            x=x+i//2
            res=min(x,p)
    print(res)
    
