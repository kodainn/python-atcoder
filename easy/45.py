def isPalindromic(s: str) -> bool:
    isJudgment = True
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            isJudgment = False
    
    return isJudgment


left, right = map(int, input().split())

ans = 0
for num in range(left, right + 1):
    if isPalindromic(str(num)):
        ans += 1

print(ans)