import math

n = int(input())

no_tax = math.ceil(n / 1.08)
if(n == math.floor(no_tax * 1.08)):
    print(no_tax)
else:
    print(":(")