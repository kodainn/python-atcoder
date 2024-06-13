w = input()
find_strings = dict()

for c in w:
    if c in find_strings:
        find_strings[c] += 1
    else:
        find_strings[c] = 1


isBeautiful = True
for count in find_strings.values():
    if count % 2 != 0:
        isBeautiful = False

if isBeautiful:
    print("Yes")
else:
    print("No")