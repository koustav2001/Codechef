t=int(input())
for i in range(t):
    s=input()
    #print(s1)
    a=[0]*26
    for i in s:
        a[ord(i)-97]+=1
    pairs=0
    singles=0
    for i in range(26):
        if(a[i]==1):
            singles+=1
        else:
            pairs+=a[i]//2
            singles+=a[i]%2
    #print(pairs,singles)
    if(pairs>=singles):
        print("YES")
    else:
        print("NO")
