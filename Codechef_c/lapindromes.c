#include<stdio.h>
int main()
{	
	int t,i,flag;
	scanf("%d",&t);
	while(t--)
	{
	char s[1000];
	int a[26]={0},b[26]={0};
	scanf("%s",s);
		if(strlen(s)%2==0)
		{
			for(i=0;i<strlen(s)/2;i++)
			{
				a[s[i]-'a']++;
			}
			for(i=strlen(s)/2;i<strlen(s);i++)
			{
				b[s[i]-'a']++;
			}
		}
		else
		{
			for(i=0;i<strlen(s)/2;i++)
			{
				a[s[i]-'a']++;
		
			}
			for(i=strlen(s)/2+1;i<strlen(s);i++)
			{
				b[s[i]-'a']++;
			
			}
		}
		flag=0;
		for(i=0;i<26;i++)
		{
			if(a[i]!=b[i])
			{
			flag=1;
			break;
			}
		}
		if(flag==1)
		printf("NO\n");
		else
		printf("YES\n");
	}
}
