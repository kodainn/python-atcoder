n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
for i in range(n):
    if a[i] > x:
        break
    x -= a[i]
    a[i] = 0

if x > 0:
    a[n - 1] += x


ans = 0
for i in a:
    if i == 0:
        ans += 1

print(ans)