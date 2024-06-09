h = int(input())
ans = 0
cnt = 1
while h > 0:
    ans += cnt
    cnt *= 2
    h //= 2

print(ans)