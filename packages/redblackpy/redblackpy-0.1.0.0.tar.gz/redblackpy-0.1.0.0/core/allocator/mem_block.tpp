//
//  Created by Soldoskikh Kirill.
//  Copyright © 2018 Intuition. All rights reserved.
//

#ifndef __BLOCK_TPP // header guards
#define __BLOCK_TPP


//---------------------------------------------------------------------------------------------------------
// Memory block template class implementation
//---------------------------------------------------------------------------------------------------------

// Constructors
//---------------------------------------------------------------------------------------------------------
template < class data_type,
           size_t block_size >
mem_block<data_type, block_size>::mem_block()
    : __address(nullptr)
    , __status() { }


template < class data_type,
           size_t block_size >
mem_block<data_type, block_size>::mem_block(mem_block&& other) {

    if (__address != nullptr)
        std::allocator<data_type>().deallocate(__address, block_size);

    __status = other.__status;
    std::swap(__address, other.__address);
}


template < class data_type,
           size_t block_size >
mem_block<data_type, block_size>::mem_block(pointer address) {

    __address = address;
}


template < class data_type,
           size_t block_size >
mem_block<data_type, block_size>::~mem_block() {

    // if (__address != nullptr)
    //     std::allocator<data_type>().deallocate(__address, block_size);
}


// Methods
//---------------------------------------------------------------------------------------------------------
template < class data_type,
           size_t block_size >
inline bool mem_block<data_type, block_size>::is_free() {

    return __status.none();
}


template < class data_type,
           size_t block_size >
inline bool mem_block<data_type, block_size>::is_reserved() {
    
    return __status.all();
}


template < class data_type,
           size_t block_size >
inline typename mem_block<data_type, block_size>::pointer 
mem_block<data_type, block_size>::reserve_block() {
    
    __status.set();

    return __address;
}


template < class data_type,
           size_t block_size >
inline void mem_block<data_type, block_size>::release_block() {
    
    __status.reset();
}


template < class data_type,
           size_t block_size >
inline size_t mem_block<data_type, block_size>::free_size() {
    
    return block_size - __status.count();
}


template < class data_type,
           size_t block_size >
inline typename mem_block<data_type, block_size>::pointer 
mem_block<data_type, block_size>::get_cell() {
    
    for(size_t i = 0; i < block_size; i++)
        if (!__status[i])
            return __address + i;
}


template < class data_type,
           size_t block_size >
inline void mem_block<data_type, block_size>::release_cell(pointer address) {
    
    __status.flip(address - __address);
}


#endif // __BLOCK_TPP
