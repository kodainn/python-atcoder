n, m = map(int, input().split())
food_counts = [0] * 30
for i in range(n):
    k_list = list(map(int, input().split()))
    for k in k_list[1:]:
        food_counts[k - 1] += 1

print(food_counts.count(n))