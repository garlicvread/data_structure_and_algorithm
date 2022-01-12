"""
The average of streaming data

Assume that some integer form of data is given one at a time.
What you are going to do is to calculate the average of the data in the range of data transmitted given.

The class 'MovingAvg' will be initiated as the range of average transmission is given.
The function 'nextVal(num) will receive integer data and has to return the average transmitted data received.

e.g.) Let's assume that
      The input: 2, 8, 19, 37, 4, 5
      The average range of  transmission: 3

      In this case, the class 'MovingAvg' will be used as follows:

      ma = MovingAvg(3)
      print(ma.nextVal(2))
      # The only value inputted up to this point is 2, thus 2 will be returned.

      print(ma.nextVal(8))
      # The inputted values are 2 and 8. Thus, (2 + 8) / 2 = 5 will be returned.

      print(ma.nextVal(19))
      # (2 + 8 + 19) / 3 = 9.666666666666666 will be returned.

      print(ma.nextVal(37))
      # The range of transmission is 3, thus (8 + 19 + 37) / 3 = 21.333333333333332 will be returned.
      # The returned value is the average value of last three months.

      print(ma.nextVal(4))
      # (19 + 37 + 4) / 3 = 20 will be returned.

      print(ma.nextVal(5))
      # (37 + 4 + 5) / 3 = 15.333333333333334 will be returned.
"""


import queue


class MovingAvg():
    def __init__(self, size):
        self.size = size
        self.q = queue.Queue()
        self.sum = 0

    def nextVal(self, num):
        """
        If the size of the queue is smaller than the size of the average range,
        calculate the average of the queue by dividing 'self.sum' by the size of the queue, 'self.q.qsize()'.

        If the size of the queue is greater than the size which is set as the average range,
        remove the first element of the queue and calculate the average of the queue
        by dividing 'self.sum' by the size of the queue, 'self.q.qsize()'.

        Note that self.q.qsize() is the same with 'self.size' with the second condition
        because we will remove the oldest element of the queue.

        The size of the average range will be given through the 'size' parameter of 'MovingAvg' class,
        and it is 3 in this case.
        """
        if self.q.qsize() < self.size:
            self.q.put(num)
            self.sum += num
            return self.sum / self.q.qsize()
        else:
            self.sum -= self.q.get()
            self.q.put(num)
            self.sum += num
            return self.sum / self.q.qsize()  # self.size() works as the same.


def queueExample():
    q = queue.Queue()
    q.put(1)
    q.put(2)
    print(q.qsize())
    print(q.get())
    print(q.qsize())
    print(q.get())


def main():
    queueExample()

    nums = [2, 8, 19, 37, 4, 5]
    ma = MovingAvg(3)
    results = []

    for num in nums:
        avg = ma.nextVal(num)
        results.append(avg)

    print(results)  # [2.0, 5.0, 9.666666666666666, 21.333333333333332, 20.0, 15.333333333333334]


if __name__ == "__main__":
    main()
