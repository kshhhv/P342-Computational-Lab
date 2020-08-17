#include <stdio.h>
#include<stdlib.h>

int main(){
	
	int size;
	printf("Enter the length of square grid:");
	scanf("%d", &size);

	float tot_dist = 0;
	int tot_points = size * size;
	int tot_pairs = tot_points * tot_points;

	//create a list of point coordinates

	int points[tot_points][2];
	int position = 0;

	for (int i = 0; i < size; i++){
		for (int j = 0; j < size; j++){
			points [position][0] = i;
			points [position][1] = j;
			position++;

		}
	}

	//calculate the distance
	
	for (int i = 0; i < tot_points; i++){
		int x1 = points[i][0];
		int y1 = points[i][1] ;
		for (int j = 0; j < tot_points; j++){
			int x2 = points[j][0];
			int y2 = points[j][1] ;
			tot_dist += abs(x2-x1)+abs(y2-y1);
		}
	}

	float avg_dist = tot_dist/tot_pairs;

	printf("The average distance between two points is %.4f", avg_dist);
}
/*
Output:
Enter the number of linear equidistant points:6
The average distance between two points is 1.9444
*/