n, m, x = map(int, input().split())
a = list(map(int, input().split()))

mass = [0] * (n + 1)
for i in a:
    mass[i] = 1
mass[x] = 0
ans = min(sum(mass[x:]), sum(mass[:x+1]))
print(ans)