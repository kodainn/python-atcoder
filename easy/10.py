n = int(input())
a_list = list(map(int, input().split()))

a_list.sort(reverse=True)

alice = 0
bob = 0
for i in range(n):
    if(i % 2 == 0):
        alice += a_list[i]
    else:
        bob += a_list[i]


print(alice - bob)