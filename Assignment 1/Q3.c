// Sum over 1+1/2+1/3+... till the sume does not change by more than 0.001
#include <stdio.h>
#include <stdlib.h>

int main()
{
	//declare the variables
    float add = 0;
    float sum = 0;

    //intitiate a for loop
    for(double n=1; n>0; n++){
	add = 1/n;

		//check if increment is significant
        if(add <= 0.001){
        	//print the output
            printf("The sum is %2f", sum);
            exit(0);
        }
        
    //update the sum
	sum += add;        
    }
return 0;
}