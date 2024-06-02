n = int(input())
max_split_count = 0
ans = 1

for i in range(1, n + 1):
    split_count = 0
    split_num = i
    while split_num % 2 == 0:
        split_count += 1
        split_num //= 2
    
    if split_count > max_split_count:
        ans = i
        max_split_count = split_count

print(ans)