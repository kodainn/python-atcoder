n = int(input())
a = list(map(int, input().split()))
cnt = 0
is_break = False
while True:
    for i in range(len(a)):
        if a[i] % 2 != 0:
            is_break = True
            break
        a[i] //= 2
    if is_break: break
    cnt += 1

print(cnt)