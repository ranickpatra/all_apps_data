#include <stdio.h>

int gcd(int a, int b)
{
  if(a%b == 0)
    return b;
  else
    gcd(b, a%b);
} 


void main()
{
  int x;
  int ff, qq;
  scanf("%d", &x);
  while(x--)
  {
    scanf("%d%d", &ff, &qq);
    int m = (ff > qq) ? ff : qq;
    int n = (ff < qq) ? ff: qq;
    printf("%d\n", gcd(m, n));
  }
}