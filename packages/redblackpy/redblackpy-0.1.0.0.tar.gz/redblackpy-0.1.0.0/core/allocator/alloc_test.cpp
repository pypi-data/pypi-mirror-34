#include <iostream>
#include <list>
#include <memory>
#include <cstdlib>
#include "allocator.hpp"
#include "../timer/timer.hpp"
#include "../tree/tree.hpp"

template <class T>
int __std_equal(const T& a, const T& b) { 

    return (a == b);
}


template <class T>
int __std_compare(const T& a, const T& b) { 

    return (a < b);
}


int main() {

    auto timer = qseries::nano_timer();
    auto tree = qseries::rb_tree<qseries::rb_node_valued<int, int>, int>();
    tree.set_compare(__std_compare);
    tree.set_equal(__std_equal);
    qseries::rb_node_valued<int, int>* mem = new qseries::rb_node_valued<int, int>[65536];
    qseries::mem_chunk<qseries::rb_node_valued<int, int>, 4096, 16> allocator(mem);
    std::allocator<qseries::rb_node_valued<int, int>> alloc;
    timer.start();
    for(size_t i = 0; i < 65536; i++) {
        // auto cell = allocator.get_cell();
        // allocator.release_cell(cell);
        // auto cell = alloc.allocate(1);
        // alloc.deallocate(cell, 1);
        auto cell = malloc(sizeof(qseries::rb_node_valued<int, int>));
        // free(cell);
    }
    auto tie = timer.stop();

    std::cout << "Time " << tie << std::endl;
    delete[] mem;

}
