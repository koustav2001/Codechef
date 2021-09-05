t=int(input())
for i in range(t):
    a=""
    b=""
    n=int(input())
    s=str(bin(n).replace("0b",""))
    #print(s)
    if(s[0]=='1'):
        a=a+'1'
        b=b+'0'
    for i in range(1,len(s)):
        if(s[i]=='1'):
            a=a+'0'
            b=b+'1'
        elif(s[i]=='0'):
            a=a+'1'
            b=b+'1'
    dec_a=int(a,2)
    dec_b=int(b,2)
    print(dec_a*dec_b)
        
