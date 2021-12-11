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
Space Complexity:

## API

- ```add```: hash the key and add the value to the table.
- ```get```: return the value associated with the key.
- ```contains```: return boolean if the key exists in the table.
- ```hash```: return index in the collection for the key.

## Solution

- [Code implementation](/code401/hash-table/hash_table/hash_table.py)

- [Test implementation](/code401/hash-table/tests/test_hash_table.py)
