"""
Detecting words patterns

A string that is about the pattern of characters and an array made of strings are given.
Each character of the string (hereinafter 'the first input') can correspond with each string from the array (hereinafter 'the second input').

For example, you will be given 'abab' as the first input, and then ['strawberry', 'blueberry', 'strawberry', 'blueberry'] as the second input.
In this case, 'a' from the first input can correspond with 'strawberry' from the second input,
'b' from the first input can correspond with 'blueberry' from the second input.

With this correspondence, let's say that the first input is the pattern of the strings from the second input.
Check if the pattern of the first input matches the second input or not.

e.g.) 'abab', ['strawberry', 'blueberry', 'strawberry', 'blueberry'] --> True
      'aabb', ['strawberry', 'blueberry', 'strawberry', 'blueberry'] --> False

Note that every character is in lower case.
"""

import re

def wordPattern(pattern, strList):
    number_of_patterns = len(set(pattern))
    # print(number_of_patterns)

    patterns = {}

    for i in range(0, len(pattern) - 1, 1):
        if strList[i] = strList[i+1]:
            patterns

    return True


def main():
    print(wordPattern('abab', ['strawberry', 'blueberry', 'strawberry', 'blueberry']))  # should return True
    print(wordPattern('aabb', ['strawberry', 'blueberry', 'strawberry', 'blueberry']))  # should return False


if __name__ == "__main__":
    main()
