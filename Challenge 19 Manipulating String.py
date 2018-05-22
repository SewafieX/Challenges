'''If is is not in the string then it will be appended'''
raw_string = input("Type string here: ")


def add_is(str):
    if "is" in str:  # from the beginning till 2
        return str
    return "is"+str


'''Another way would be to check if the first 2 characters of the string
are i and s such as:
(line 6): if str[:2] == "is": return str  # from beginning till 2'''

r = add_is(raw_string)
print(r)
