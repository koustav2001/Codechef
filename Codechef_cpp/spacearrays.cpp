#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        int N;
        cin >> N;
        int A[N];
        for (int i = 0; i < N; i++)
        {
            cin >> A[i];
        }
        sort(A, A + N);
        int count = 0;
        int flag=0;
        for (int i = 0; i < N; i++)
        {
            if (A[i] > (i + 1))
            {
                flag=1;
                break;
            }
            else
            {
                count = count + (i + 1) - A[i];
            }
        }
        if(flag==1)
        {
            cout<<"Second"<<endl;
        }
        else
        {
        if (count % 2 != 0)
            cout << "First" << endl;
        else
            cout << "Second" << endl;
        }
    }
    return 0;
}