#include <stdio.h>
int subtractProductAndSum(int n){
    int res,muti,sum;
    muti=1;
    sum=0;
    while (n>=10)
    {
        muti*=(n%10);
        sum+=(n%10);
        n/=10;
    }
    muti*=n;
    sum+=n;
    res=muti-sum;
    return res;
}

void main()
{
    int res;
    res=subtractProductAndSum(234);
    printf("%d",res);
}
