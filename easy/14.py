n = int(input())

min_digits = float('inf')
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        A = i
        B = n // i
        max_digits = max(len(str(A)), len(str(B)))
        min_digits = min(min_digits, max_digits)

print(min_digits)