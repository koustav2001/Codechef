
def binarytodecimal(binary):
    decimal=0
    for digit in binary:
        decimal=decimal*2+int(digit)
    return decimal
for t in range(int(input())):
    n=int(input())
    s=input()
    s1=""
    s2=""
    for i in range(0,len(s),4):
        s1=s1+s[i:i+4]
        bin=binarytodecimal(s1)
        s2=s2+chr(97+bin)
        s1=""
    print(s2)   


