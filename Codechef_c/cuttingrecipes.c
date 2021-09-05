#include<stdio.h>
int main()
{
	int t,n,min,i;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		int ar[n];
		for(i=0;i<n;i++)
		scanf("%d",&ar[i]);
		min=ar[0];
		for(i=1;i<n;i++)	
		{
			min=gcd(min,ar[i]);
		}
		for(i=0;i<n;i++)
		printf("%d ",ar[i]/min);
	}
}
int gcd(int a,int b)
{
	if(b==0)
	return a;
	else
	return gcd(b,a%b);
}
