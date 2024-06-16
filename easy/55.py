import math

n, d = map(int, input().split())
distance = []
for i in range(n):
    x = list(map(int, input().split()))
    distance.append(x)

results = []
ans = 0
for i in range(n):
    total = 0
    for j in range(i + 1, n):
        dd = 0
        for k in range(d):
            dd += abs(distance[i][k] - distance[j][k]) ** 2
        sqrt_num = math.sqrt(dd)
        if sqrt_num - int(sqrt_num) == 0:
            ans += 1

print(ans)