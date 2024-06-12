n, k, q = map(int, input().split())
joiner = [0] * n
for _ in range(q):
    a = int(input())
    joiner[a - 1] += 1

for i in range(n):
    ans = joiner[i] - q + k
    if ans > 0:
        print("Yes")
    else:
        print("No")