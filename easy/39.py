n = int(input())
a_list = [int(input()) for _ in range(n)]
first = sorted(a_list, reverse=True)[0]
second = sorted(a_list, reverse=True)[1]
first_index = a_list.index(first)

for i in range(n):
    if i == first_index:
        print(second)
    else:
        print(first)