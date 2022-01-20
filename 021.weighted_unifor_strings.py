"""
A weighted string is a string of lowercase English letters where each letter has a weight.
Character weights are 1 to 26 from a to z, respectively.

The weight of a string is the sum of the weights of its characters.
For example:
    1. apple: 1 + 16 + 16 + 12 + 5 = 50
    2. hack: 8 + 1 + 3 + 11 = 23
    3. watch: 23 + 1 + 20 + 3 + 8 = 53
    4. ccccc: 3 + 3 + 3 + 3 + 3 = 15
    5. aaa: 1 + 1 + 1 = 3
    6. zzzz: 26 + 26 + 26 + 26 = 104

A uniform string consists of a single character repeated zero or more times.
For example, "ccc" and "a" are uniform strings, but "bcb" and "cd" are not.

Given a string "s", let "U" be the set of weights for all possible uniform contiguous substrings of string "s".\
There will be "n" queries to answer where each query consists of a single integer.

Create a return array where for each query, the value is "Yes" if query[i] ∈ U.
Otherwise, append "No".

NOTE: The ∈ symbol denotes that x[i] is an element of set U.


Example:
s = "abbcccdddd"
queries = [1, 7, 5, 4, 15]

Working from left to right, weights that exist are:

string  weight
a       1
b       2
bb      4
c       3
cc      6
ccc     9
d       4
dd      8
ddd     12
dddd    16

Now, for each value in "queries", see if it exists in the possible string weights.
The return array is ["Yes", "No", "No", "Yes", "No"].


Sample Input 0

abccddde
6
1
3
12
5
9
10

Sample Output 0

Yes
Yes
Yes
Yes
No
No


Sample Input 1

aaabbbbcccddd
5
9
7
8
12
5

Sample Output 1

Yes
No
Yes
Yes
No


What I am going to do is to complete the 'weightedUniformStrings' function below.
The function will return a STRING_ARRAY.

The function will accept following parameters:
 1. STRING "s"
 2. INTEGER_ARRAY "queries"
"""

# Assign the weight from 1 to 26 to the characters from a to z
weight_dict = {chr(i + ord('a')): i + 1 for i in range(26)}
# print(weight_dict)


def weightedUniformStrings(s, queries):
    possible_weight_list = []
    temp_uniform_substr = []

    for i in range(len(s)):
        if i == 0:
            temp_uniform_substr.append(s[i])
            possible_weight_list.append(weight_dict[s[i]])
        else:
            if s[i] == s[i - 1]:
                temp_uniform_substr.append(s[i])
                possible_weight_list.append(weight_dict[s[i]] * (len(temp_uniform_substr)))
            else:
                temp_uniform_substr = [s[i]]
                possible_weight_list.append(weight_dict[s[i]])

    print(possible_weight_list)
    # print(temp_uniform_substr)

    for i in range(len(queries)):
        if queries[i] in possible_weight_list:
            print("Yes")
        else:
            print("No")


s = "abccddde"
queries = [6, 1, 3, 12, 5, 9, 10]

# s = "aaabbbbcccddd"
# queries = [5, 9, 7, 8, 12, 5]

weightedUniformStrings(s, queries)
