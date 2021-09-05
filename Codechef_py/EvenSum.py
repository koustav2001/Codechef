t=int(input())
for i in range(t):
    lst=[]
    n=int(input())
    sum=0
    sum1=0
    for i in range(n):
        num=int(input())
        lst.append(num)
        sum+=i
    for i in range(n):
        if(i%2==0):
            sum1+=i
    if((sum-sum1)%2==0):
        print(1)
    else:
        print(2)
            
    
