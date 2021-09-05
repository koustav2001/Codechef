n=int(input())
m=0
for i in range(1,11):
    if(n%i==0):
        m=max(m,i)
print(m)
        
