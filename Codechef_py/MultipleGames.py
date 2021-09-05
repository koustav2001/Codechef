t=int(input())
for i in range(t):
    p=[]
    n,q,m=map(int,input().split())
    x=[int(x) for x in input().split()]
    for i in range(q):
        l1=[]
        l,r=map(int,input().split())
        l1.append(x[l-1])
        l1.append(x[r-1])
        #print(x)
        p.append(l1)
    print(p)
    c=0
    for i in range(0,len(p)):
        print(p[i][0],p[i+1][1])
        #if(p[i][0]==p[i+1][0]):
            #c+=1
    print(c)
