a, b = map(int, input().split())
tap_count = 1
ans_count = 0
while tap_count < b:
    tap_count += a - 1
    ans_count += 1

print(ans_count)