file_name = ("x-file.txt")
fd = open(file_name)         # r is implicit

# another way is to read it line by line
print("here are the contents of the file:")
print(fd.read())

fd.close()

with open(file_name) as fd:
    print()