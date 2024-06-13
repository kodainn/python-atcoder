n = int(input())
p = list(map(int, input().split()))

ans = 0
mi = float('inf')
for i in p:
    mi = min(mi, i)
    if i == mi:
        ans += 1

print(ans)