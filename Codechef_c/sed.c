#include<stdio.h>
int main()
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
		int n,k,i,s=0;
		scanf("%d %d",&n,&k);
		int ar[n];
		for(i=0;i<n;i++)
		{
			scanf("%d",&ar[i]);
		}
		for(i=0;i<n;i++)
		{
			s=s+ar[i];
		}
		if(s%k==0)
		printf("0\n");
		else
		printf("1\n");
	}
}
