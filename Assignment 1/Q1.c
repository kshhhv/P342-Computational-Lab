// add 1+2+3+ ... 100 WITHOUT using the formula n(n+1)/2

#include <stdio.h>

int main(){
  int sum, n;
  sum = 0;
  printf("Enter a number: ");
  scanf("%d", &n);
  for (int i = 1; i < n + 1; i++){
    sum = sum + i;
  }
  printf("The sum is %d", sum);
  return 0;
}
