t=int(input())
for i in range(t):
    n=int(input())
    c=0
    lst1=[]
    x=[int(x) for x in input().split()] 
    x.sort()
    print(x)
    for i in x:
        if i not in lst1:
            lst1.append(i)
    print(lst1)
    print(n-len(lst1))
