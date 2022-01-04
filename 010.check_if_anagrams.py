"""
Anagram explanation: https://en.wikipedia.org/wiki/Anagram

With the two strings given, check if they are anagrams of each other.
1. When the two strings are anagram of each other, return True.
2. When the two strings are not anagram of each other, return False.

e.g.) "abcd" and "dcba" are anagrams of each other. Return True.
      "cat" and "cap" are not anagrams of each other. Return False.
"""

"""
# Solution 1: time complexity O(n^2), space complexity O(n)

def isAnagram(str1, str2):
    str1_list = list(str1)
    str2_list = list(str2)
    
    str1_list.sort()
    str2_list.sort()
    
    if str1_list == str2_list:
        return True
    else:
        return False
"""


"""
# Solution 2: time complexity O(n), space complexity O(n)

def isAnagram(str1, str2):
    str1_list = list(str1)
    str2_list = list(str2)

    str1_list.sort()
    str2_list.sort()
    
    return str1_list == str2_list
"""


"""
# Solution 3: time complexity O(n), space complexity O(n)

def isAnagram(str1, str2):
    if len(str1) != len(str2):
        return False

        for i in range(len(str1)):
            if str1[i] in str2:
                continue
            else:
                return False
    return True
"""


# Solution 4: Using dictionary type. time complexity O(n), space complexity O(n)

def isAnagram(str1, str2):
    dic1 = {}  # Declare a dictionary to store the keys and values for each character of the first string.

    for char in str1:
        """
        If the character is already in the dictionary, add 1 to the value for the character (key).
        If the character is not in the dictionary, load the default value of 0 then add 1.
        For the second case, the value of a character that was not in the dictionary is set to 1.
        """
        dic1[char] = dic1.get(char, 0) + 1

    for char in str2:
        if char in dic1:
            if dic1[char] == 0:
                return False
            else:
                dic1[char] -= 1
        else:
            return False

    return True


def main():
    print(isAnagram('iamlordvoldemort', 'tommarvoloriddle'))  # should return True.
    print(isAnagram('cat', 'cap'))  # should return False.


if __name__ == "__main__":
    main()
