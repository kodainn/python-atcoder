s = input()
alphabet = "abcdefghijkmlnopqrstuvwxyz"
for i in alphabet:
    if s.count(i) > 1:
        print("no")
        exit()

print("yes")