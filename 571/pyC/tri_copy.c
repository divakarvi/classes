void tri_copy(double *a, int n, double *b){
	for(int i=0; i < n; i++)
		for(int j=0; j<=i; j++)
			b[j + i*(i+1)/2] = a[i];
}
