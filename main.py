def add_binary(a, b):
    # your code here
    total = a + b
    remainder = []
    while total > 0:
        remainder.append(total % 2)
        total = total // 2
    return "".join([str(i) for i in remainder[::-1]])

print(add_binary(1, 1))
print(13 // 2)
