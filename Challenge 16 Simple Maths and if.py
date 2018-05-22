number = int(input("Choose a number: "))
compared = 17
result = number - 17
if number > 17:
    print("Number is greater than 17; the result is doubled: %d" % (abs(result)*2))
else:
    print("Number is less than 17; the result remains the same: %d" % (abs(result)))
