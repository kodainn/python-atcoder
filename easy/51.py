def digit_computation(num: int) -> int:
    num_str = str(num)
    total = 0
    for c in num_str:
        total += int(c)
    
    return total


ans = 0
n, a, b = map(int, input().split())
for i in range(1, n + 1):
    num = digit_computation(i)
    if num >= a and num <= b:
        ans += i

print(ans)