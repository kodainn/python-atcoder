n, a, b = map(int, input().split())
cnt = n // (a + b)
m = cnt * (a + b)
print(cnt*a + min(a, n - m))