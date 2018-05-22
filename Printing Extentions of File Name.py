
filename = input("Input your file name with its extension: ")
separator = filename.split(".")

print("The Extension of the file is: " + repr(separator[-1]))  # 0 first term; -1 last term
