#include <stdio.h>

int main()
{
  int first;
  int second;
  int sum;
  printf("Please input first number\n");
  scanf("%d", &first);
  printf("Please input second number\n");
  scanf("%d", &second);
  sum = first + second;
  printf("Sum is %d\n", sum);
  return sum;
}