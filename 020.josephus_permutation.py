"""
Josephus permutation

Assume that 'n' and 'k' are natural numbers and k < n.
When n persons are gathered in a circle, the k-th person from a random person will be removed from the circle.

Within the n-1 persons in the circle, the k-th person from the next person who is removed will be removed again.
This process continues until nobody is left in the circle.

The order of persons who are removed from the circle is called (n, k) Josephus permutation,
and to find the last person who is left in the circle is called Josephus problem.

e.g.) Where n = 7 and k = 3, the (7, 3) Josephus permutation is {3, 6, 2, 7, 5, 1, 4}.

      Sample input: josephus(7, 3)

      Sample output:[3, 6, 2, 7, 5, 1, 4]

      1 2 3 4 5 6 7
      1 2   4 5   7  |  3 6
      1     4 5      |  3 6 2 7
      1     4        |  3 6 2 7 5
            4        |  3 6 2 7 5 1
                     |  3 6 2 7 5 1 4

NOTE: Use queue.

----------------------------------------------------------------------------------------------------------------------
Solution for the number to be removed and the order of removal
n개의 수를 저장하는 배열을 [1, 1, ..., 1]과 같이 선언해서, 왼쪽부터 직접 k개씩 세어가며 수가 제거될 때 해당 위치에서 배열의 값을 0으로 바꾸는 방법이다. 사람에게 손으로 직접 문제를 풀으라고 할 때 가장 먼저 떠올릴 만한 방법을 선형으로 펼친 형태이다.
n개의 1을 저장하는 배열 live = [1, 1, ..., 1]를 선언한다. 이후 live[x]=1이면 x는 아직 제거되지 않은 것이고, live[x]=0이면 x는 제거된 것이다.
변수 x=1을 선언한다. 이후 과정에서 x가 제거될 수인지 아닌지 판단하는 과정을 반복적으로 거치게 된다.
다음을 n-1회 반복한다.
변수 c=1을 선언한다. c는 제거할 수를 고르기 위한 변수로, 지금 보는 수 x가 최근에 제거한 수로부터 몇 번째 수인지를 의미한다.
다음을 하나의 수가 제거될 때까지 반복한다.
live[x]=0이라면 그대로 둔다.
live[x]=1이라면,
c=k라면 live[x]=0으로 바꾼다. 이는 다음으로 제거되는 수가 x라는 의미이므로, ans에 x를 추가한다. c!=k라면 그대로 둔다.
이후 c에 1을 더한다. live[x]=0이라면 c에 1을 더하지 않음에 유의한다.
이후 x에 1을 더한다. 더한 후 x=n+1이라면 x=1로 바꾼다.
live[x]=1인 남은 x가 마지막으로 남는 수이다.

수를 제거하는 과정에서 남은 수의 개수가 k보다 작아진다면 위 알고리즘의 3번 과정은 배열을 여러 차례 돌게 된다.
이를 방지하기 위해 수를 세는 횟수를 k가 아닌 (k-1)%(남은 수의 개수)+1로 바꿔서 최적화할 수 있다.

아래 코드에서 수를 세는 횟수를 바꾼 값이 변수 t에 저장된다.
"""

import queue


def josephus(num, k):
    current = [1] * (num + 1)  # num + 1: this is because the index number starts from 0 in python.
    current[0] = 0
    rmv = 1  # The number to be removed.
    answer = []

    for i in range(num-1):
        c = 1  # How many times the number in the current focus is away from the lastly removed number.
        t = (k-1) % (num-i) + 1  # t: the count for the changes in counting numbers.
        prev = len(answer)  # This is to capture the removal of a number from the circle.

        # The while loop will stop when the length of current 'answer' becomes longer than that of previous 'answer'.
        while len(answer) == prev:
            if current[rmv] == 1:
                if c == t:
                    current[rmv] = 0
                    answer.append(rmv)
                c += 1
            rmv += 1
            if rmv == num + 1:
                rmv = 1

    last = current.index(1)  # The remained last number.
    answer.append(last)

    return answer


def main():
    print(josephus(7, 3))  # [3, 6, 2, 7, 5, 1, 4]이 반환되어야 합니다


if __name__ == "__main__":
    main()


"""
Solution only for the last number:
1. O(n) time complexity

When we assume n = 1, the first argument is f(1, k) = 1.

The relationship between 'n' and 'k' is:
    f(n, k) = (f(n-1, k) + k mod n) + 1
    
If the order of persons starts from 0 instead of 1,
the relationship between 'n' and 'k' can be simplified as:
    g(n, k) = (g(n-1, k) + k) mod n, g(1, k) = 0
    
When n is a super-duper large number and k is a relatively small number,
it is known that the Josephus problem can be solved in a very short time: O(k log n).

See the link below for more details of the algorithm.
https://stackoverflow.com/questions/4845260/josephus-for-large-n-facebook-hacker-cup

For more information about 'mod', check out the modular calculation.
https://www.crocus.co.kr/1231
"""
