numbers = int(input())
current_sum = 0

for _ in range(numbers):
    current_number = int(input())
    current_sum += current_number
print(current_sum)