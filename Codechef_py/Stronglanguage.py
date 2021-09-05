t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    s=input()
    c=0
    f=0
    for i in range(0,len(s)):
        if(s[i]=='*'):
            c+=1
            if(c==k):
                f=1
                break
            else:
                continue
        else:
            c=0
    
    if(f==1):
        print("YES")
    else:
        print("NO")
