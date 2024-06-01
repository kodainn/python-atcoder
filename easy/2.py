n = int(input())
x_list = list(map(int, input().split()))
x_list_max = max(x_list)
x_list_min = min(x_list)
ans = 99999999

for i in range(x_list_min, x_list_max + 1):
    total = 0
    for x in x_list:
        total += abs((x - i)**2)
    ans = min(ans, total)

print(ans)