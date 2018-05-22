n = int(input("Enter an integer: "))


def check(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"


print(check(n))

