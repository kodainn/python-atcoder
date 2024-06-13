n = int(input())

lucas_numbers = [0] * 90
lucas_numbers[0] = 2
lucas_numbers[1] = 1

for i in range(2, 90):
    lucas_numbers[i] = lucas_numbers[i - 1] + lucas_numbers[i - 2]

print(lucas_numbers[n])