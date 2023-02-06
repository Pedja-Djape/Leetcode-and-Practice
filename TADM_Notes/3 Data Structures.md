# Data Structures

## 3.1  Contiguous vs. Linked Data Structures

**Contiguously allocated structures** are composed of single slabs of memory. For example, arrays, matrices, heaps, and hashtables.
**Linked data structures** are composed of distinct chunks of memory bound by pointers, and include lists, trees, and graph adjacency lists.

### 3.1.1 Arrays

* Are of fixed size and each element is of the same type. 
* Advantages:
    * *Constant-time access given the index* -- Index of each element maps directly to a particular memory address.
    * *Space efficiency* -- Arrays consist purely of data, hence no space is wasted with links or other formatting information.
    * *Memory locality* -- Many programming tasks require iterating theough elements of a data structure. Arrays have good memory
    locality --> physical continuity between successive data accesses helps exploit the high-speed cache memory on computer architectures.
* However, can;t adjust their size in the middle of a programs excecution. 

### 3.1.2 Pointers and Linked Structures

*Pointers* are the connections that hold the pieces of linked structures together. Pointers represent the address of a location in memory. A variable storing a pointer to a given data item can provide more freedom than storing a copy of the item itself.
A pointer ${p}$ is assumed to give the address in memory where a particular chunk of data is located. Use $*p$ to denote the item that is pointed to by pointer $p$, and &x to denote the address of (i.e., pointer to) a particular variable. 