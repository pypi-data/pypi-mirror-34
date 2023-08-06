
#include "tree.hpp"
#include <iostream>
#include <vector>
#include <cstdlib>
#include <utility>
#include <string>
#include "../exceptions/qs_exceptions.hpp"
#include "../trees_iterator/iterator.hpp"
#include "../timer/timer.hpp"
#include "thread"

using namespace qseries;

template <class tree_type>
int __comp( const std::pair<tree_type*, typename tree_type::iterator>& a, 
			 const std::pair<tree_type*, typename tree_type::iterator>& b) {

	return ( (*a.second)->key < (*b.second)->key );
}

template <class T>
int __std_equal(const T& a, const T& b) { 

	return (a == b);
}


template <class T>
int __std_compare(const T& a, const T& b) { 

	return (a < b);
}


template <class tree_type>
int __equal( const std::pair<tree_type*, typename tree_type::iterator>& a, 
			  const std::pair<tree_type*, typename tree_type::iterator>& b) {

	return ( (*a.second)->key == (*b.second)->key );
}

int main() {


	std::vector< rb_tree<rb_node_valued<int,int>, int>* > trees = std::vector< rb_tree<rb_node_valued<int,int>, int>* >(2);
	auto iter = trees_iterator<rb_tree<rb_node_valued<int,int>, int>, rb_node_valued<int,int> >();
	iter.set_equal(__equal);
	iter.set_compare(__comp);

	auto tree = rb_tree<rb_node_valued<int,int>, int>();
	tree.set_compare(__std_compare);
	tree.set_equal(__std_equal);

	auto tree_2 = rb_tree<rb_node_valued<int,int>, int>();
	tree_2.set_compare(__std_compare);
	tree_2.set_equal(__std_equal);

	tree.insert(rb_node_valued<int, int>(1,1));
	tree.insert(rb_node_valued<int, int>(10,5));
	tree_2.insert(rb_node_valued<int, int>(4,1));
	tree_2.insert(rb_node_valued<int, int>(3,5));

	std::cout << " Get item " << std::endl;
	std::cout << tree.tree_search(1).first->key << std::endl;

	trees[0] = &tree;
	trees[1] = &tree_2;

	iter.set_iterator(trees, "forward");
	auto timer = nano_timer();
	timer.start();
	std::this_thread::sleep_for(std::chrono::nanoseconds(1000));
	while (!iter.empty()) {

		std::cout << (*iter).key << std::endl;
		iter++;
	}
	double _time = timer.stop();
	std::string s = "bggb";
	std::swap(s[0], s[2]);
	std::cout << "Time: " << _time << std::endl;

	// for(auto &el: tree)
	// 	std::cout << el->key << std::endl;
}