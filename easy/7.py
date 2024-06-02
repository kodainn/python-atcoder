bingo_list = [[False, False, False] for _ in range(3)]
a_dict = dict()
for i in range(3):
    tmp = list(map(int, input().split()))
    for j in range(3):
        a_dict[tmp[j]] = (i, j)

n = int(input())
for _ in range(n):
    b = int(input()) 
    if b in a_dict:
        bingo_list[a_dict[b][0]][a_dict[b][1]] = True

ans = "No"
for i in range(3):
    if bingo_list[i][0] and bingo_list[i][1] and bingo_list[i][2] == True:
        ans = "Yes"
    if bingo_list[0][i] and bingo_list[1][i] and bingo_list[2][i] == True:
        ans = "Yes"
if bingo_list[0][0] and bingo_list[1][1] and bingo_list[2][2] == True:
    ans = "Yes"
if bingo_list[0][2] and bingo_list[1][1] and bingo_list[2][0] == True:
    ans = "Yes"

print(ans)