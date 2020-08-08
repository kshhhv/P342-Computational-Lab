//factorial n! say for n=10 or 15, check and trap negative integers, say for -5!

//include required librarires
#include <stdio.h>
#include <stdlib.h>


int main(){
  //declare the variables
  int fact, n;
  fact = 1;
  //take input from user
  printf("Enter a number: ");
  scanf("%d", &n);
  //trap negative input
  if (n < 0){
    printf("Product of negative number is undefined.");
    exit(0);
  }
  //intitiate a for loop
  for (int i = n; i > 0; i--){
    fact = fact*i;
  }
  //print the output
  printf("The factorial of the number is  %d", fact);
  return 0;
}
