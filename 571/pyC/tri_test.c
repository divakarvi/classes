#include <stdio.h>
#include <stdlib.h>
#include "tri_copy.h"
#define n 4

int main(){
	double a[n] = {1, 2, 3, 4};
	double b[n*(n+1)/2]; 
	tri_copy(a, n, b);
	
	printf("a = ");
	for(int i=0; i < n; i++){
		printf("%.1f", a[i]);
		if(i < n-1)
			printf(", ");
	}
	printf("\nb = ");
	for(int i=0; i < n*(n+1)/2; i++){
		printf("%.1f", b[i]);
		if(i < n*(n+1)/2-1)
			printf(", ");
	}
	printf("\n");
}
