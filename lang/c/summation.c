#include <stdio.h>

int main(void) {
	long long var = 0;

	for (long long i = 0; i < 0x40000000; i++) {
		var += i;
	}

	printf("Sum: %lli\n", var);
	return 0;
}
