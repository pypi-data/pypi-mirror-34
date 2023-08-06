//
//  Created by Soldoskikh Kirill.
//  Copyright © 2018 Intuition. All rights reserved.
//

#ifndef __ALLOC_QS // header guards
#define __ALLOC_QS

#include <memory>
#include <bitset>
#include <vector>
#include <queue>
#include <map>
#include <array>


namespace qseries {

/*
This file contains definition of single-thread pool allocator template class.
The hierarchy of allocator structure: allocator -> memory chunks -> memory block.
Allocator creates pool of chunks, at the same time each chunk allocates memory blocks
of fixed sizes, then managed allocated memory by itself. 
**/ 

//---------------------------------------------------------------------------------------------------------
// Memory block template class
//---------------------------------------------------------------------------------------------------------
template < class data_type,
           size_t block_size=32 >
class mem_block {

    public:
        // Typedefs
        typedef data_type*       pointer;
        typedef const data_type* const_pointer;

        // friend declaration
        template < class dtype,
                   size_t chunk_size,
                   size_t b_size >
        friend class mem_chunk;

        // Constructors
        mem_block();
        // mem_block(const mem_block&) = delete;
        mem_block(mem_block&&);
        mem_block(pointer);
        ~mem_block();

        // Methods
        bool is_free();
        bool is_reserved();
        void release_block();
        void release_cell(pointer);
        size_t free_size();
        pointer reserve_block();
        pointer get_cell();

        /* Similar to copy constructor, disable assignment operator to 
        only one class instance could own heap allocated block memory.
        **/
        // mem_block& operator=(const mem_block&) = delete;
        // mem_block& operator=(mem_block&&);

    private:
        // Attributes
        pointer                 __address;
        std::bitset<block_size> __status;
};

// Include template class implementation 
#include "mem_block.tpp"      


//---------------------------------------------------------------------------------------------------------
// Memory blocks chunk template class
//---------------------------------------------------------------------------------------------------------
template < class data_type,
           size_t block_size >
struct block_compare {
    typedef mem_block<data_type, block_size>*    block_ptr;

    bool operator()(const block_ptr& block_1, const block_ptr& block_2) { 
        return ( (block_1->free_size)() < (block_2->free_size)() );
    }
};



template < class data_type,
           size_t chunk_size=32,
           size_t block_size=32 >
class mem_chunk {

    public:
        // Typedefs
        typedef data_type*       pointer;
        typedef const data_type* const_pointer;

        // Constructors
        mem_chunk();
        mem_chunk(const mem_chunk&) = delete;
        mem_chunk(mem_chunk&&);
        mem_chunk(pointer);
        ~mem_chunk();

        // Methods
        pointer get_cell();
        void release_cell(pointer&);
        size_t free_size();

    private:
        // Typedefs
        typedef mem_block<data_type, block_size>     block_t;
        typedef std::pair<size_t, block_t>           pair_t;
        typedef std::array<block_t, chunk_size>      array_t;
        typedef mem_block<data_type, block_size>*    block_ptr;
        typedef std::vector<block_ptr>               vec_t;
        typedef block_compare<data_type, block_size> comp_t;

        // Attributes
        size_t                                      __free_size;
        pointer                                     __begin;
        std::array<block_t, chunk_size>             __blocks;
        // std::map<pointer, block_t>                    __blocks_map;
        std::priority_queue<block_ptr, vec_t, comp_t> __blocks_queue;

        // Helpers
        void __update_queue();
};

// Include template class implementation 
#include "mem_chunk.tpp"  



//---------------------------------------------------------------------------------------------------------
// Pool allocator template class
//---------------------------------------------------------------------------------------------------------
template < class data_type,
           size_t chunk_size=32,
           size_t block_size=32 >
class allocator {

    public:
        // Typedefs
        typedef data_type        value_type;
        typedef data_type*       pointer;
        typedef const data_type* const_pointer;
        typedef size_t           size_type; 
        typedef ptrdiff_t        difference_type;
        typedef data_type&       reference;
        typedef const data_type& const_reference;

        // Constructors
        allocator();
        allocator(const allocator&) = delete;
        allocator(allocator&&);
        ~allocator(); 

        // Methods
        pointer allocate(size_type);
        void deallocate(pointer, size_type);
        void construct();
        void destroy();


    private:
        // Typedefs
        typedef mem_chunk<data_type, chunk_size, block_size> chunk_t;

        // Attributes
        std::allocator<data_type> __base;
        std::map<pointer, chunk_t> __chunks;
};

// Include template class implementation 
#include "allocator.tpp"  


} // namespace qseries


#endif // __ALLOC_QS