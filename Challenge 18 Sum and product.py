'''Input 3 numbers and if '''
numbers = input("Input 3 numbers separated by commas: ")
# x = input("Input the value of x: ")
# y = input("Input the value of y: ")


def thrice(numbers):
    value = numbers.split(",")

    if value[0] == value[1] and value[1] == value[2]:
        result = (int(value[0]) + int(value[1]) + int(value[2]))*2
    else:
        result = int(value[0]) + int(value[1]) + int(value[2])
    return result


print(thrice(numbers))
