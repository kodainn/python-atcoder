def acCepted(s: str) -> bool:
    if s[0] != "A":
        return False
    
    if s[2:-1].count("C") != 1:
        return False
    
    lowerCnt = 0
    for c in s:
        if c.islower():
            lowerCnt += 1
    
    if lowerCnt != len(s) - 2:
        return False

    return True

s = input()
if acCepted(s):
    print("AC")
else:
    print("WA")