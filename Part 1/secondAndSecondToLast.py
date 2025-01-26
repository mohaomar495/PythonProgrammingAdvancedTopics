"""
Please write a program which asks the user for a string. The program then prints out a message based on whether
the second character and the second to last character are the same or not. See the examples below.

Sample output
Please type in a string: python
The second and the second to last characters are different
Sample output
Please type in a string: pascal
The second and the second to last characters are a
"""


def main():
    string = "pascal"
    result = SecondAndSecondToLast(string)
    print(result)


def SecondAndSecondToLast(string) -> str:
    if string == "":
        return "Please provide string i.e 'Hello'."
    if string[1] == string[-2]:
        return f"The second and the second to last characters are '{string[1]}'"
    return "The second and the second to last characters are different"


if __name__ == "__main__":
    main()
