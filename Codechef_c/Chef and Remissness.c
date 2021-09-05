#include<stdio.h>
int max(int  ,int );
int main()
{
	int a,b,t,sum,maximum;
	scanf("%d",&t);
	while(t--)
	{
	scanf("%d %d",&a,&b);
	maximum=max(a,b);
	sum=a+b;
	printf("%d %d",maximum,sum);
	}
}
int max(int x,int y)
{
	if(x>y)
	return x;
	else
	return y;
}
