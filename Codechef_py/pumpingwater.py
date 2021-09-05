t=int(input())
for i in range(t):
    n=int(input())
    c=0
    x=[int(x) for x in input().split()]
    j=0
    for i in range(j,n,1):
        if(i>i+1):
            c+=1
            j=i+1
        else:
            continue
            print(c)
            
    #print(c)
