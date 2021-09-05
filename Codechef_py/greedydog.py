t=int(input())
for i in range(t):
    m=0
    n,k=map(int,input().split())
    data=[]
    for i in range(1,k+1):
        data.append(n%i)
    print(max(data))
