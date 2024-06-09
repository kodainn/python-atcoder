import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

perms = list(itertools.permutations(range(1, N + 1)))

rank_P = perms.index(P)
rank_Q = perms.index(Q)

result = abs(rank_P - rank_Q)

print(result)