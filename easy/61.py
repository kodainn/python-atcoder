def strings_rotation(s: str, t: str) -> bool:
    if s == t:
        return True
    
    t2 = t + t
    rotation_find_index = t[1:].find(s[0]) + 1
    if rotation_find_index == -1:
        return False
    
    for i in range(1, len(s)):
        if s[i] != t2[i + rotation_find_index]:
            return False
    
    return True

s = input()
t = input()

if strings_rotation(s, t) or strings_rotation(t, s):
    print("Yes")
else:
    print("No")