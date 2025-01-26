"""
Please write a program which asks the user for a string. The program then prints out the input string in reversed order,
 from end to beginning. Each character should be on a separate line.

An example of expected behaviour:

Sample output
Please type in a string: hiya
a
y
i
h
"""


def main():
    string = "Hell0"
    reversedString = ReverseString(string)
    for c in reversedString:
        print(c)


def ReverseString(string) -> list:
    reversedStr = [string[i] for i in range(len(string) - 1, -1, -1)]
    return reversedStr


if __name__ == "__main__":
    main()
