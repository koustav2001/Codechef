#include<stdio.h>
int main()
{
	int t,n,k,d,i;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d %d %d",&n,&k,&d);
		int a[n];
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
		}
		int sum=0;
		for(i=0;i<n;i++)
		sum+=a[i];
		if(sum<k)
		printf("0\n");
		else
		{
			int result=sum/k;
			if(result<=d)
			printf("%d\n",result);
			else
			printf("%d\n",d);
		}
	}
}
