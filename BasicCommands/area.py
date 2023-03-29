print("1.Rectangle Area")
a = int(input("Side 1: "))
b = int(input("Side 2: "))
rectangle_area = a * b
print(rectangle_area)

#
print()
print("2.Convert inches to centimeters")
inch = float(input("Enter a number in inches: "))
one_inch_in_cm = 2.54
inches_to_cm = one_inch_in_cm * inch
print(inches_to_cm)

#
print("3.Print numbers on one line")
for num in range(1, 11):
    print(num, end=" ")
