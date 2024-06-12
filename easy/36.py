n, m = map(int, input().split())
left = 0
right = float('inf')
for _ in range(m):
    l, r = map(int, input().split())
    left = max(left, l)
    right = min(right, r)

ans = right - left + 1
if ans < 0:
    ans = 0
print(ans)