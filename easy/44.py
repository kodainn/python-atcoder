s = input()
ans = float('inf')

cnt = 0
for i in range(len(s)):
    if(int(s[i]) == i % 2): cnt+=1
ans = min(ans, cnt)

cnt = 0
for i in range(len(s)):
    if(int(s[i]) != i % 2): cnt+=1
ans = min(ans, cnt)

print(ans)