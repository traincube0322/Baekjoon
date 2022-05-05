#백준 2839

n = int(input())
cnt = 0
while n:
    if n < 2:
        cnt = -1
        break
    if n % 5 == 0:
        cnt += n // 5
        break
    else : 
        n -= 3
        cnt += 1
print(cnt)