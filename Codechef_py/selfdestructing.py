t=int(input())
for i in range(t):
    s=input()
    zero=0
    ones=0
    if(len(s)%2!=0 ):
        print('-1')
    else:
        for i in range(len(s)):
            if(s[i]=='1'):
                ones+=1
            else:
                zero+=1

        if(ones==zero):
            print(0)
        elif(ones==0 or zero==0):
            print(-1)
        else:
            print(abs(zero-ones)//2)
        
