#ifndef TRICOPY_14DEC2016
#define TRICOPY_14DEC2016
/*
 * a[0...n-1]
 * b[0...n(n+1)/2-1]
 * copies a --> b as a[0] a[1] a[1] a[2] a[2] a[2] ...
 */
void tri_copy(double *a, int n, double *b);
#endif
