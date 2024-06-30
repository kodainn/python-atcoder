def vertical_reading(s, t):
    n = len(s)
    for w in range(1, n):
        splitStrList = [s[i:i+w] for i in range(0, len(s), w)]
        for i in range(len(splitStrList[0])):
            splitStr = ""
            for subStr in splitStrList:
                if(i < len(subStr)):
                    splitStr += subStr[i]
            if(splitStr == t):
                return True

    return False

s, t = input().split()
if(vertical_reading(s, t)):
    print("Yes")
else:
    print("No")