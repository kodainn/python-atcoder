find_str = []
n = int(input())
ans = "Yes"
prev_w = input()
for i in range(n - 1):
    w = input()
    if w[0] != prev_w[-1]:
        ans = "No"
    
    if w in find_str:
        ans = "No"
    
    find_str.append(w)
    prev_w = w
print(ans)