n = int(input())
d = dict()
for _ in range(n):
    s = input()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1

d = sorted(d.items(), key=lambda x: (-x[1], x[0]))

maxCnt = d[0][1]
for i in d:
    if i[1] == maxCnt:
        print(i[0])