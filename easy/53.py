n, m = map(int, input().split())
citys = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    citys[a - 1] += 1
    citys[b - 1] += 1

for city in citys:
    print(city)