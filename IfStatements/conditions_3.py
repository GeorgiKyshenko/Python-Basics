def separator():
    print("------")


first_number, second_number = int(input()), int(input())

if first_number > second_number:
    print(first_number)
else:
    print(second_number)

separator()

number = int(input())

if number % 2 == 0:
    print("even")
else:
    print("odd")

