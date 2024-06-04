def f(n: int) -> int:
    result = 0
    if n % 2 == 0:
        result = n // 2
    else:
        result = n * 3 + 1
    
    return result

limit = 1000010
a = [0] * limit
exitst_list = []
s = int(input())
for i in range(1, limit):
    if i == 1:
        a[i] = s
    else:
        a[i] = f(a[i - 1])
    
    if a[i] in exitst_list:
        print(i)
        break
    exitst_list.append(a[i])
