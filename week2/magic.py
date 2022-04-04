input = input("Please enter a number: ")
number = float(input)
magic = int(((number * 3  + 6) // 3) - number)
print(magic)