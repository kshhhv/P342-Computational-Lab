#include <stdio.h>

int main(){

    int vec_A[3], vec_B[3];  

    vec_A[0] = 1;
    vec_A[1] = 2;
    vec_A[2] = 3;

    vec_B[0] = 2;
    vec_B[1] = 4;
    vec_B[2] = 6;


    // print the vectors
    printf("First vector is [");
    for(int i=0; i<3; i++){
        printf("%d,", vec_A[i]);
    }
    printf("]\n");

    printf("Second vector is [");
    for(int j=0; j<3; j++){
        printf("%d,", vec_B[j]);
    }
    printf("]\n");


    // sum of vectors
    int sum[3];
    for(int i=0; i<3; i++){
        sum[i] = vec_A[i] + vec_B[i];
    }

    // calculates the dot product i.e., A.B
    int in_pro = 0;
    for(int l=0; l<3; l++)
    {
        in_pro += vec_A[l]*vec_B[l];
    }

    // displays the sum and dot product
    printf("The vector sum is [");
    for(int i=0; i<3; i++)
    {
        printf("%d,", sum[i]);
    }

    printf("]\n");
    printf("The dot product is %d", in_pro);
    return 0;
}