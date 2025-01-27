"""
Please write a program which asks the user to type in a number. The program then prints out the positive integers
between 1 and the number itself, alternating between the two ends of the range as in the examples below.

Sample output
Please type in a number: 5
1
5
2
4
3
Sample output
Please type in a number: 6
1
6
2
5
3
4
"""


def main():
    number = 5
    result = TakingTurns(number)
    for i in result:
        print(i)


def TakingTurns(number) -> list:
    altList = []  # Alternating list numbers
    numbers = [num for num in range(1, number + 1)]

    while numbers[1]<numbers[-1]:
        altList[numbers] =
    return altList
