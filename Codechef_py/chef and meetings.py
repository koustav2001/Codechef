def time_to_float(time):
    #print(((time[len(time)-2])+(time[len(time)-2])))
    if(((time[len(time)-2])+(time[len(time)-1]))=="PM"):
        if(time[0]+time[1]=="12"):
            t=t=float(time[0]+time[1]+"."+time[3]+time[4])
        else:
            #print("Yes")
            t=float(str(int(time[0]+time[1])+12)+"."+time[3]+time[4])
    else:
        if(time[0]+time[1]=="12"):
            t=float("00."+time[3]+time[4])
        else:
            t=float(time[0]+time[1]+"."+time[3]+time[4])
    return t

n=int(input())
for i in range(0,n):
    s1=""
    time=input()
    n1=int(input())
    for k in range(0,n1):
        l=[]
        s=input()
        time_1=""
        time_2=""
        j=0
        while(j<len(s)):
            if(s[j]!='M'):
                time_1=time_1+s[j]
            else:
                time_1=time_1+s[j]
                break
            j=j+1
        j=j+2
        while(j<len(s)):
            time_2=time_2+s[j]
            j=j+1
        #print(time_to_float(time_1),time_to_float(time_2))
        friend_time=time_to_float(time)
        timef_1=time_to_float(time_1)
        timef_2=time_to_float(time_2)
        #print(friend_time,timef_1,timef_2)
        if(friend_time>=timef_1 and friend_time<=timef_2):
            s1=s1+"1"
        else:
            s1=s1+"0"
    print(s1)
    s1=""
