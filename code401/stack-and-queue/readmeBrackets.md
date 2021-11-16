# Challenge Summary

    Write a function called validate brackets
    Arguments: string
    Return: boolean
        representing whether or not the brackets in the string are balanced

There are 3 types of brackets:

    Round Brackets : ()
    Square Brackets : []
    Curly Brackets : {}

## Whiteboard Process

![whiteboard](/code401/stack-and-queue/bracket.png)

## Approach & Efficiency

The approach was looping through the string to check if there are an any brackets in the string (opening one), if so push it to the stack, then checking if there are a brackets but closing bracket then pop them.

Big o is O(n)