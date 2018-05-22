'''Ask the user to input a list of numbers and count the recurrences of a certain
number, n, in that list'''

raw_list = input("Input list of numbers separated by commas: ")
n = int(input("Input the value you're counting: "))

# if the split attribute is left blank then entries should be separated by a space
numbers = list(map(int, raw_list.split(",")))


def count(lis):
    counts = 0
    for i in lis:
        if i == n:
            counts = counts + 1

    return counts


print(count(numbers))


