#include <stdio.h>
#include <stdlib.h>

__global__ void holaMundo() {
	printf("Te hablo desde la GPU!\n");
}

int main() {
	printf("Te hablo desde la CPU\n");
	holaMundo<<<1,1>>>();
	cudaDeviceSynchronize();
	return 0;
}

