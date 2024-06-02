k, n = map(int, input().split())
a_list = list(map(int, input().split()))

ans = a_list[n - 1] - a_list[0]
for i in range(1, n):
    i_to_start = k - a_list[i]
    start_to_i1 = a_list[i - 1]
    ans = min(ans, i_to_start + start_to_i1)

print(ans)