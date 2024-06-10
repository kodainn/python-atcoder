s = input()
ans = float('inf')

for i in range(len(s) - 2):
    num = (int(s[i]) * 100) + (int(s[i + 1]) * 10) + int(s[i + 2])
    ans = min(ans, abs(num - 753))

print(ans)