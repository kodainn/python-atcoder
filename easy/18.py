acgt = "ACGT"
s = input()

ans = 0
max_len = 0
for c in s:
    if c not in acgt:
        ans = max(ans, max_len)
        max_len = 0
    else:
        max_len += 1

ans = max(ans, max_len)

print(ans)