for _ in range(int(input())):
    s=input()
    length=False
    small=False
    large=False
    digit=False
    spec=False
    if len(s)>=10:
        length=True
        for i in range(len(s)):
            if (s[i]>='a' and s[i]<='z'):
                small=True
            if(i!=0 and i!=(len(s)-1)):
                if (s[i]>='A' and s[i]<='Z'):
                    large=True
                if (s[i]>='0' and s[i]<='9'):
                    digit=True
                if (s[i]=='@' or s[i]=='#' or s[i]=='%' or s[i]=='&' or s[i]=='?'):
                    spec=True
    #print(length,small,large,digit,spec)
    if (length and small and large and digit and spec):
        print('YES')
    else:
        print('NO')
