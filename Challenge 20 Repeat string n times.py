'''Copies the inputted string n times '''
raw_str = input("Input a string: ")


def copy(str, n):
    result = ""
    for i in range(n):
        result += str
    return result


f = copy(raw_str, 4)
print(f)