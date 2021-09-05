t=int(input())
for i in range(t):
    x=list(map(int,input().split()))
    k=int(input())
    i=9
    while(x[i]>=k):
        k=k-x[i]
        i=i-1
    print(i+1)
