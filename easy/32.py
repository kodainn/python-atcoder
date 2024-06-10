x = 0
n = int(input())
s = input()
max_num = 0
for i in s:
    if i == "I":
        x += 1
    else:
        x -= 1
    max_num = max(max_num, x)

print(max_num)