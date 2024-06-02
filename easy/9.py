n = int(input())
k = int(input())
x_list = list(map(int, input().split()))

sum = 0
for x in x_list:
    a = x * 2
    b = abs(k - x) * 2
    min_num = min(a, b)
    sum += min_num

print(sum)