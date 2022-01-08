# HackerRank, Circular Array Rotation - https://www.hackerrank.com/challenges/circular-array-rotation/problem?isFullScreen=true

import math
import os
import random
import re
import sys

"""
The 'circular_array_rotation' function below returns a rotated array.
The rotated array must be rotated as much as the given integer 'k'.

With the rotated array, the function must return elements that have an index number
that matches each element of the given array 'queries'.
For example: [3, 4, 5] --> [5, 3, 4] --> [4, 5, 3]

The function is expected to return an INTEGER_ARRAY.

The function accepts following parameters:
    1. INTEGER_ARRAY a
    2. INTEGER k
    3. INTEGER_ARRAY queries


Sample input:
    - a = [3, 4, 5]
    - k = 2  # 'k' is the number of rotations on 'a'.
    - queries = [1, 2]  # 'queries' holds the list of indices to be reported.

    e.g.) 3 2 3  # n, k, q, respectively.
                 # n: the number of elements in 'a'.
                 # k: the rotation count.
                 # q: the number of queries.
          1 2 3  # The array 'a'.
                 # A n-space-separated integers, where each integer 'i' describes array element a[i].
                 # and the range of 'i' is 0 <= i < n.
          0      # queries[0]
          1      # queries[1]
          2      # queries[2]


Sample output:
    - int[q]  # the values in the rotated array 'a' as requested in 'm'.
    
    e.g.) 2  # a[queries[0]]
          3  # a[queries[1]]
          1  # a[queries[2]]
 """


def circular_array_rotation(a, k, queries):
    temp = a
    answer = []

    for i in range(k):
        temp.append(temp.pop())

    print("temp: ", temp)

    for i in queries:
        answer.append(temp[i])
        # print(answer)

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circular_array_rotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
