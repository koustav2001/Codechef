t=int(input())
for t in range(t):
    n=int(input())
    s=input().split()
    d={}
    for i in s:
        p=i[1:]
        if p in d:
            d[p].append(i[0])
        else:
            d[p]=[i[0]]
    #print(d)
    d1=list(d.keys())
    print(d1)
    
