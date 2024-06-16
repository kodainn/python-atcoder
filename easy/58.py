n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

ansIndex = -1
nearOnTarget = float('inf')
for i in range(n):
    temperature = t - h[i] * 0.006
    if abs(a - temperature) < nearOnTarget:
        ansIndex = i
        nearOnTarget = abs(a - temperature)

print(ansIndex + 1)