n = int(input())
t = list(map(int, input().split()))
m = int(input())

totals = []
for _ in range(m):
    p, x = map(int, input().split())
    total = 0
    for i in range(len(t)):
        if i + 1 == p:
            total += x
        else:
            total += t[i]
    totals.append(total)

for total in totals:
    print(total)