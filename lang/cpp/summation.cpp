#include <iostream>
#include <cstdlib>

int main() {
	long long var = 0;

	for (long long i = 0; i < 0x40000000; i++) {
		var += i;
	}

	std::cout << "Sum: " << var << "\n";
	return 0;
}
