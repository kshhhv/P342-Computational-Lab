#include <stdio.h>

int main(){
	
	int vec_A[3];
	vec_A[0] = 1;
	vec_A[1] = 2;
	vec_A[2] = 3;

	int mat_M[3][3], mat_N[3][3];

	//import matrix
	FILE *m, *n;
	m = fopen("m.txt", "r");
	n = fopen("n.txt", "r");

	for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            fscanf(m, "%d", &mat_M[i][j]);
            fscanf(n, "%d", &mat_N[i][j]);
        }
    }

    fclose(m);
    fclose(n);

    //print vector and matrix
    printf("Vector A is [");
    for(int i=0; i<3; i++){
        printf("%d ", vec_A[i]);
    }
    printf("]\n");

    printf("Matrix M is: \n");
    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            printf("%d\t", mat_M[i][j]);
        }
        printf("\n");
    }

    printf("Matrix N is: \n");
    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            printf("%d\t", mat_N[i][j]);
        }
        printf("\n");
    }

    //Matrix operation on vector A
    int vec_B[3] = {0};

	for(int i=0; i<3; i++){
		for(int j=0; j<3; j++){
        	vec_B[i] += mat_M[i][j]*vec_A[j];
		}
	}

	//Matrix product
	int mat_C[3][3] = {0};
	for(int i=0; i<3; i++){
		for(int j=0; j<3; j++){
			for(int k=0; k<3; k++){
        	    mat_C[i][j] += mat_N[k][j] * mat_M[i][k];
        	}
      	}
    }


    //print the output
	printf("Vector B = M x A = [");
    for(int i=0; i<3; i++){
        printf("%d ", vec_B[i]);
    }
    printf("]\n");

    printf("Matrix C = M x N is: \n");
    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            printf("%d\t", mat_C[i][j]);
        }
        printf("\n");
    }
    return 0;

}

/*
Output:
Vector A is [1 2 3 ]
Matrix M is:
1       2       3
4       5       6
7       8       9
Matrix N is:
2       1       1
1       2       1
1       1       2
Vector B = M x A = [14 32 50 ]
Matrix C = M x N is:
7       8       9
19      20      21
31      32      33
*/
