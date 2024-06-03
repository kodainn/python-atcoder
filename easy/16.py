n, x, y = map(int, input().split())
x -= 1
y -= 1

ans = [0] * 2010

for i in range(n):
    for j in range(i+1, n):
        k = 2009

        k = min(k, j - i)

        k = min(k, abs(x - i) + abs(y - j) + 1)

        ans[k] += 1

for i in range(1, n):
    print(ans[i])