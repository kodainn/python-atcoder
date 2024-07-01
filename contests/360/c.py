n = int(input())
a = list(map(int, input().split()))
w = list(map(int, input().split()))

boxs = dict()
total_cost = 0
for i in range(n):
    if a[i] in boxs.keys():
        boxs[a[i]].append(w[i])
    else:
        boxs[a[i]] = [w[i]]

for box in boxs.values():
    if(len(box) > 1):
        sorted_box = sorted(box, reverse=True)
        popBox = sorted_box[1:]
        for i in popBox:
            total_cost += i

print(total_cost)