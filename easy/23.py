n = int(input())
d, x = map(int, input().split())

eat_total = 0
for _ in range(n):
    a = int(input())
    eat_total += 1
    i = 1
    while i*a + 1 <= d:
        eat_total += 1
        i += 1

ans = eat_total + x
print(ans)