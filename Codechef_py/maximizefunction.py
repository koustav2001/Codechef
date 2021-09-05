t=int(input())
for i in range(t):
    n=int(input())
    x = [int(x) for x in input().split()]
    m=max(x)
    n=min(x)
ans=m-n
print(ans*2)
