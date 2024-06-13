h, w = map(int, input().split())
ans = [""] * (h + 2)
ans[0] = "#" * (w + 2)
ans[-1] = "#" * (w + 2)

for i in range(h):
    a = input()
    ans[i + 1] = "#" + a + "#"

for i in ans:
    print(i)