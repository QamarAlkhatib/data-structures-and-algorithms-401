# Hashmap LEFT JOIN
<!-- Short summary or background information -->

## Challenge

Write a function that LEFT JOINs two hashmaps into a single data structure.

    Write a function called left join
    Arguments: two hash maps
        The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
        The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
    Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic

## Whiteboard

![Whiteboard](/code401/hashmap-left-join/left_join.png)

## Approach & Efficiency

Time: O(n) where n is the keys in the first hash table

## Solution

- [Code implementation](/code401/hashmap-left-join/hashmap_left_join/left_join.py)

- [Test implementation](/code401/hashmap-left-join/tests/test_hashmap_left_join.py)
