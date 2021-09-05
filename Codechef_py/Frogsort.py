import math
t=int(input())
for i in range(t):
    n=int(input())
    wt=list(map(int,input().split()))
    length=list(map(int,input().split()))
    ind={}
    s=0
    for i in range(1,n+1):
        ind[i]=wt.index(i)
    for i in range(2,n+1):
        temp1=ind[i]
        temp2=ind[i-1]
        temp=0
        if temp1<=temp2:
            temp=(math.ceil((temp2+1-temp1)/length[temp1]))
        s+=temp
        ind[i]+=temp*(length[temp1])
    print(s)
