#include <stdio.h>
#include<stdlib.h>

int main(){
	
	int size;
	printf("Enter the number of linear equidistant points:");
	scanf("%d", &size);

	float tot_dist = 0;
	int tot_pairs = size*size;

	for (int i = 0; i < size; i++){
		for (int j = 0; j < size; j++){
			tot_dist += abs(j - i);
		}
	}

	float avg_dist = tot_dist/tot_pairs;

	printf("The average distance between two points is %.4f", avg_dist);

	return 0;
}
/*
Output:
Enter the number of linear equidistant points:6
The average distance between two points is 1.9444
*/