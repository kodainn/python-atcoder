s = input()
alphabet = "abcdefghijkmlnopqrstuvwxyz"
isNone = True
for c in alphabet:
    cnt = s.count(c)
    if cnt == 0:
        isNone = False
        print(c)
        break

if isNone: print("None")