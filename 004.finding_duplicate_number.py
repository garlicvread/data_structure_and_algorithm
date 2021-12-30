from collections import Counter


def findDuplicate(nums):
    result = Counter(nums)
    
    for key, value in result.items():
        if value >= 2:
            return key


def main():
    print(findDuplicate([1, 5, 2, 4, 5, 6, 3]))


if __name__ == "__main__":
    main()
