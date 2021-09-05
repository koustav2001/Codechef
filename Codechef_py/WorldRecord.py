t=int(input())
for i in range(t):
    k1,k2,k3,v=map(float,input().split())
    #print(k1,k2,k3,v)
    num=float(k1*k2*k3*v)
    wr=round(100/num,2)
    if(wr<9.58):
        print("YES")
    else:
        print("NO")

