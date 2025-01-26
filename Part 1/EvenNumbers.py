"""
Please write a program which prints out all the even numbers between two and thirty, using a loop. Print each number on a separate line.

The beginning of your output should look like this:

Sample output

2
4
6
8
etc...
"""


def main():
    evenNumList = EvenNumber(2, 30)
    for num in evenNumList[:-1]:
        print(num, end=", ")
    print(evenNumList[-1])


def EvenNumber(minimum, maximum) -> [int | float]:
    evenNums = []
    oddNums = []
    for num in range(minimum, maximum):
        if num % 2 == 0:
            evenNums.append(num)
        else:
            oddNums.append(num)
    return evenNums


if __name__ == "__main__":
    main()
