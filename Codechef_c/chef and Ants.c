#include<stdio.h>
int main()
{
	long long t,n,i,j,m;
	scanf("%lld",&t);
	while(t--)
	{
		scanf("%lld",&n);
		long long cn=0,cp=0;
		while(n--)
		{
			scanf("%lld",&m);
			long long a[m+1];
			for(i=0;i<m;i++)
			{
				scanf("%lld",&a[i]);	
				if(a[i]<0)
				cn++;
				else
				cp++;
			}
		}
		long long result=cn*cp;
		printf("%lld",result);
	}
}
