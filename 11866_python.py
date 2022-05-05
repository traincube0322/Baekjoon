# 백준 11866
n, k = input().split()
n = int(n)
k = int(k)
L = [i for i in range(1,n+1)]
answer = []
index = -1
for i in range(n):
    cnt = 0
    while 1:
        index += 1
        if index >= n:
            index -= n
        if L[index] != 0:
            cnt += 1
        if cnt == k: break

    answer.append(L[index])
    L[index] = 0

print("<",end='')
print(answer[0],end='')
for i in range(1,n):
    print(",",answer[i],end='')
print(">",end='')