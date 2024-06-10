a, b = map(int, input().split())
s = input()
if len(s) != a + b + 1:
    print("No")
    exit()

for i in range(len(s)):
    if i == a:
        if s[i] != "-":
            print("No")
            exit()
    else:
        if not s[i].isdigit():
            print("No")
            exit()

print("Yes")