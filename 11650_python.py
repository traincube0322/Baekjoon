# 백준 11650

n = int(input())
L = []
for i in range(n):
    t = input().split()
    t = list(map(int, t))
    L.append(t)
5
L.sort()
for i in range(n):
    print(L[i][0], L[i][1])
