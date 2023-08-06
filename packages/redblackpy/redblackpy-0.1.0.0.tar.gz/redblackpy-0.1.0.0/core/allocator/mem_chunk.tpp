//
//  Created by Soldoskikh Kirill.
//  Copyright © 2018 Intuition. All rights reserved.
//

#ifndef __CHUNK_TPP // header guards
#define __CHUNK_TPP


//---------------------------------------------------------------------------------------------------------
// Memory chunk template class implementation
//---------------------------------------------------------------------------------------------------------

// Constructors
//---------------------------------------------------------------------------------------------------------
template < class data_type,
           size_t chunk_size,
           size_t block_size >
mem_chunk<data_type, chunk_size, block_size>::mem_chunk() {

    __free_size = chunk_size*block_size;
}


template < class data_type,
           size_t chunk_size,
           size_t block_size >
mem_chunk<data_type, chunk_size, block_size>::mem_chunk(mem_chunk&& other) {

    std::swap(__blocks, other.__blocks);
    std::swap(__blocks_queue, other.__blocks_queue);
}


template < class data_type,
           size_t chunk_size,
           size_t block_size >
mem_chunk<data_type, chunk_size, block_size>::mem_chunk(pointer address) {

    pointer current_address = address;
    pointer end = address + block_size*chunk_size;
    block_ptr inserted;

    for(size_t i = 0; current_address != end; i++, current_address+=block_size) {
        __blocks[i].__address = current_address;
        // inserted = __blocks_map.emplace( std::move(current_address), 
        //                                  std::move( block_t(block_t(current_address)) ) 
        //                                ).first;
        __blocks_queue.push(&__blocks[i]);
    }
}


template < class data_type,
           size_t chunk_size,
           size_t block_size >
mem_chunk<data_type, chunk_size, block_size>::~mem_chunk() {}


// Public Methods
//---------------------------------------------------------------------------------------------------------
template < class data_type,
           size_t chunk_size,
           size_t block_size >
typename mem_chunk<data_type, chunk_size, block_size>::pointer
mem_chunk<data_type, chunk_size, block_size>::get_cell() {

    if ( !(__blocks_queue.top()->free_size)() )
        __update_queue();

    block_ptr top_queue = __blocks_queue.top();
    __free_size--;

    return (top_queue->get_cell)();
}


template < class data_type,
           size_t chunk_size,
           size_t block_size >
inline void mem_chunk<data_type, chunk_size, block_size>::release_cell(pointer& address) {

    size_t index = (address - __blocks[0].__address) / block_size;

    __blocks[index].release_cell(address);
    __free_size++;
}


// Private Methods
//---------------------------------------------------------------------------------------------------------
template < class data_type,
           size_t chunk_size,
           size_t block_size >
void mem_chunk<data_type, chunk_size, block_size>::__update_queue() {

    block_ptr updated_block = __blocks_queue.top();

    __blocks_queue.pop();
    __blocks_queue.push(updated_block);
}


#endif // __CHUNK_TPP