n = 1000000
isPrimes = [True] * n
isPrimes[0], isPrimes[1] = False, False

for i in range(2, int(n**0.5) + 1):
    if isPrimes[i]:
        for j in range(2*i, n, i):
            isPrimes[j] = False

x = int(input())
for i in range(x, n):
    if isPrimes[i]:
        print(i)
        break