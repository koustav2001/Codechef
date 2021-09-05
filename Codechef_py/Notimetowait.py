n,h,x=map(int,input().split())
a=list(map(int,input().split()))
for i in a:
    time=i+x
    if(time>=h):
        s="YES"
        break
    elif(time<h):
        s="NO"
print(s)
