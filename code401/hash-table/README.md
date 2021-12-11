# Hashtables

the Hash table is a type of data structure that maps keys to its value pairs. It makes accessing data faster as the index value behaves as a key for data value.

## Challenge

Features

Implement a Hashtable Class with the following methods:

    add
        Arguments: key, value
        Returns: nothing
        This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
    get
        Arguments: key
        Returns: Value associated with that key in the table
    contains
        Arguments: key
        Returns: Boolean, indicating if the key exists in the table already.
    hash
        Arguments: key
        Returns: Index in the collection for that key

## Approach & Efficiency

Time Complexity:

- because I used the changing the time and space for the add method is :
  - Time: o(1)
  - Space: O(m+n)
  where m is the size of the hash table and n is the number of items inserted. This is because linked nodes are allocated memory outside the hash map.
- add: o(1), because we insert the key according to the hashed key with out going through the hash table.

- hash: o(n), where n is the number of the characters in a key, space: o(1)

- get: o(n): where n is the  number of the keys in the hash table

- contains: o(1)

## API

- ```add```: hash the key and add the value to the table.
- ```get```: return the value associated with the key.
- ```contains```: return boolean if the key exists in the table.
- ```hash```: return index in the collection for the key.

## Solution

- [Code implementation](/code401/hash-table/hash_table/hash_table.py)

- [Test implementation](/code401/hash-table/tests/test_hash_table.py)
