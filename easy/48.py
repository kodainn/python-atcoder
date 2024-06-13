n = int(input())
h = list(map(int, input().split()))

moves = []
for i in range(0, len(h) - 1):
    isMove = 1 if h[i] - h[i + 1] >= 0 else 0
    moves.append(isMove)

ans = 0
move_cnt = 0
for move in moves:
    if move == 1:
        move_cnt += 1
    else:
        ans = max(move_cnt, ans)
        move_cnt = 0

ans = max(ans, move_cnt)

print(ans)