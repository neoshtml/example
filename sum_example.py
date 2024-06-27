# The sum function counts down from the given number to 1, prints each number, and returns the sum of all these numbers.

def sum(num):
    result = 0
    for i in range(num):
        current = num - i
        print(current)
        result += current
    return print("Sum:", result)


sum(15)