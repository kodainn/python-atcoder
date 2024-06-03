a, b, c = map(int, input().split())

ans = 0
while a%2 == 0 and b%2 == 0 and c%2 == 0:
    ans += 1
    tmp_a = a / 2
    tmp_b = b / 2
    tmp_c = c / 2
    a = tmp_b + tmp_c
    b = tmp_a + tmp_c
    c = tmp_a + tmp_b

    if(ans > 100000):
        print(-1)
        exit()


print(ans)