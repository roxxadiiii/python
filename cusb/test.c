#include<stdio.h>
#include<stdlib.h>
int main()
{
  int a[501],i;
  for(i=0; i<500; i++)
  {
    a[i]=rand();
    printf("a[i]=%d\n",a[i]);
  }
  return 0;

}
