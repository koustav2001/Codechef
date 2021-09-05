t=int(input())
for i in range(t):
    s=input()
    cl,cu,cs,cd=0,0,0,0
    if(len(s)>=10):
        for i in range(len(s)):
            if(s[i]>='a' and s[i]<='z'):
                cl=1
            if(s[i]>='A' and s[i]<='Z' and i!=0 and i!=len(s)-1):
                cu=1
            if(s[i]>='0' and s[i]<='9' and i!=0 and i!=len(s)-1):
                cd=1
            if((s[i]=='@' or s[i]=='#' or s[i]=='%' or s[i]=='&' or s[i]=='?')and i!=0 and i!=len(s)-1):
                cs=1
        if(cs and cd and cu and cl):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
           
