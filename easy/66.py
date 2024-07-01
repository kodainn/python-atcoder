def can_return_home(s):
    d = {"N": 0, "S": 0, "W": 0, "E": 0}
    for direction in s:
        d[direction] = 1
         
    if d["N"] + d["S"] == 1:
        return False
    
    if d["W"] + d["E"] == 1:
        return False

    return True

s = input()

if can_return_home(s):
    print("Yes")
else:
    print("No")