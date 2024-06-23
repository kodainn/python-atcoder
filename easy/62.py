x = [["" for _ in range(1000) ] for _ in range(2000)]

h, w = map(int, input().split())
for i in range(0, 2 * h, 2):
    c = input()
    for j in range(w):
        x[i][j] = c[j]
        x[i + 1][j] = c[j]


for i in range(2 * h):
    for j in range(w):
        print(x[i][j], end="")
    print()