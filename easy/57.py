A, B = map(int, input().split())
for x in range(1, 10001):
    a = x * 8 // 100
    b = x * 10 // 100
    if a == A and b == B:
        print(x)
        exit()
print(-1)
