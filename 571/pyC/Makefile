tri_copy.o: tri_copy.c
	gcc -fPIC -std=c99 -O3 -c tri_copy.c
tri_test.o: tri_test.c
	gcc -fPIC -std=c99 -O3 -c tri_test.c
test.exe: tri_test.o tri_copy.o
	gcc -o $@ $^
tri_copy.so: tri_copy.o
	gcc -shared tri_copy.o -o tri_copy.so
