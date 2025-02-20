"""
Please write a program which asks the user to type in a number. The program then prints out all the positive integer
values from 1 up to the number. However, the order of the numbers is changed so that each pair or numbers is flipped.
That is, 2 comes before 1, 4 before 3 and so forth. See the examples below for details.

Sample output
Please type in a number: 5
2
1
4
3
5
Sample output
Please type in a number: 6
2
1
4
3
6
5
"""


def main():
    number = 6
    result = FlipThePairs(number)
    for i in result:
        print(i)


def FlipThePairs(number):
    numbers = [num for num in range(1, number + 1)]
    for i in range(0, number, 2):
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    return numbers


if __name__ == "__main__":
    main()
