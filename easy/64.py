o = input()
e = input()

oIndex = 0
eIndex = 0
cnt = 0
while cnt != len(o) + len(e):
    if cnt % 2 == 0:
        print(o[oIndex], end="")
        oIndex += 1
    else:
        print(e[eIndex], end="")
        eIndex += 1
    cnt += 1