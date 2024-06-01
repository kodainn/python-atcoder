n, a, b = map(int, input().split())
s = input()

a_path_count = 0
b_path_count = 0

for i in s:
    if i == "a" and (a_path_count + b_path_count + 1) <= (a + b):
        print("Yes")
        a_path_count += 1
    elif i == "b" and (a_path_count + b_path_count + 1) <= (a + b) and b_path_count + 1 <= b:
        print("Yes")
        b_path_count += 1
    elif i == "c":
        print("No")
    else:
        print("No")