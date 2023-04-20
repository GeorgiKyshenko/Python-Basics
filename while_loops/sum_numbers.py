number = int(input())
sum_numbers = 0

# Solution #1
while True:
    current_number = int(input())
    sum_numbers += current_number
    if sum_numbers >= number:
        break
print(sum_numbers)

# Solution #2
while sum_numbers < number:
    current_number = int(input())
    sum_numbers += current_number
print(sum_numbers)