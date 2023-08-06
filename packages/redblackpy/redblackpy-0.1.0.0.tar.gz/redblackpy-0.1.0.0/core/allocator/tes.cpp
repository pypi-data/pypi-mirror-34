#include <iostream>
#include <cstdlib>

int main() {

                                     
	double* mem = (double*)malloc(10*sizeof(double));
	double* const& ref = mem;
	double d = 4;
	const double& g = d;
	const double* h = &g;
	h[0] = 1;
	*ref = 1;
	std::cout << d << std::endl;
	float* mem_2 = (float*)malloc(20*sizeof(float));
	size_t mem_int_1 = reinterpret_cast<size_t>(mem + 2);
	size_t mem_int_2 = reinterpret_cast<size_t>(mem_2 + 3);
	std::cout << ((void*)&mem[2] < (void*)&mem[3]) << " " << ((void*)&mem[2] < (void*)&mem_2[3]) << " " << mem_int_1 << " " << mem_int_2  << std::endl;
	
	return 0;
}
