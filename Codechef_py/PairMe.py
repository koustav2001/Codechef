t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    m=max(x,y,z)
    if(x+y==m or x+z==m or y+z==m):
        print("YES")
    else:
        print("NO")
    
