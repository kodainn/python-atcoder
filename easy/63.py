n = int(input())
a = list(map(int, input().split()))

cu = 1
for i in a:
    if i == cu: cu += 1

if cu == 1:
    print(-1)
else:
    print(n - cu + 1)