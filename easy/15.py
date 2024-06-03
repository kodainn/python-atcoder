# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))

# 正の数、負の数、0の数を数える
plus = sum(1 for x in A if x > 0)
minus = sum(1 for x in A if x < 0)
zero = N - plus - minus

# 答えの初期化
ans = 0

# 条件に応じて操作を行う
if minus % 2 == 0:
    ans = sum(map(abs, A))
elif zero > 0:
    ans = sum(map(abs, A))
else:
    mi = min(abs(x) for x in A)
    ans = sum(map(abs, A)) - 2 * mi

# 答えを出力する
print(ans)