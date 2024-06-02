n, m, c = map(int, input().split())
b_list = list(map(int, input().split()))
a_list = []
for _ in range(n):
    a_list.append(list(map(int, input().split())))
    
ans = 0
for i in range(n):
    sum = 0
    for j in range(m):
        sum += a_list[i][j] * b_list[j]
    sum += c
    
    if sum > 0:
        ans += 1

print(ans)