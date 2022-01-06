"""
Finding Different character

You are given two strings.
The second string is a string that has one more character than the first string.
Find the different character from the first string which is included in the second string.

e.g.) When the first string is "apple" and the second string is "azlppe", then the added character to the second string is "z".
      The added character is only one character.
      The added character does not have to be different from the characters from the first string.
"""


def findDifference(str1, str2):
    temp_dict_1 = {}
    temp_dict_2 = {}

    for char in str1:
        temp_dict_1[char] = temp_dict_1.get(char, 0) + 1
    # print(temp_dict_1)

    for char in str2:
        temp_dict_2[char] = temp_dict_2.get(char, 0) + 1
    # print(temp_dict_2)

"""
    # With the next code, a test case error occurs.
    
    for i in range(len(temp_dict_2)):
        if temp_dict_2[str2[i]] == temp_dict_1.get(str2[i], 0):
            continue
        else:
            return str2[i]
"""

    # This is a better solution.

    for key, value in temp_dict_2.items():
        if value == temp_dict_1.get(key, 0):
            continue
        else:
            return key


def main():
    print(findDifference("apple", "azlppe"))


if __name__ == "__main__":
    main()
