// add 1+2+3+ ... +n WITHOUT using the formula n(n+1)/2

//include required librarires
#include <stdio.h>

int main(){
  //declare the variables
  int sum, n;
  sum = 0;
  //take input from user
  printf("Enter a number: ");
  scanf("%d", &n);
  //intitiate a for loop
  for (int i = 1; i < n + 1; i++){
    sum = sum + i;
  }
  //print the output
  printf("The sum is %d", sum);
  return 0;
}
