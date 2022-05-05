# 백준 10845
import sys
q = []
def push(q,a):
    q.append(a)
def pop(q):
    if len(q) == 0:
        print(-1)
    else : print(q.pop(0))
def size(q):
    print(len(q))
def empty(q):
    if len(q) == 0 : print(1)
    else : print(0)
def front(q):
    if len(q) == 0: print(-1)
    else : print(q[0])
def back(q):
    if len(q) == 0 : print(-1)
    else : print(q[-1])

n = int(sys.stdin.readline())
for i in range(n):
    word = sys.stdin.readline().split()
    if word[0] == 'push':
        push(q, word[1])
    if word[0] == 'pop':
        pop(q)
    if word[0] == 'size':
        size(q)
    if word[0] == 'empty':
        empty(q)
    if word[0] == 'front':
        front(q)
    if word[0] == 'back':
        back(q)