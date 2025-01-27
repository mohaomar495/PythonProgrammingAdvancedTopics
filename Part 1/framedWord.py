"""
Please write a program which asks the user for a string and then prints out a frame of * characters with the word
in the centre. The width of the frame should be 30 characters.
You may assume the input string will always fit inside the frame.

If the length of the input string is an odd number, you may print out the word in either of the two possible
centre locations.

Sample output
Word: testing
******************************
*          testing           *
******************************
Sample output
Word: python
******************************
*           python           *
******************************
"""


def main():
    word = "Mohamed"
    result = WordFraming(word)
    print(result)


def WordFraming(word) -> str:
    return f"{'*' * 30}\n*{' ' * ((28 - len(word)) // 2)}{word}{' ' * ((28 - len(word) + 1) // 2)}*\n{'*' * 30}"


if __name__ == "__main__":
    main()
