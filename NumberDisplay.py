var = input("Please enter a numbrer: ")

if not var.isdecimal():
    print("Invalid number:",var)
    exit(1)

for var in range(int(var), -1, -2):
    print(var)

