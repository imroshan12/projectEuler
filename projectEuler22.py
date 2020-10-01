n = int(input())
names = []
for i in range(n):
    names.append(input())
names.sort()
q = int(input())
for j in range(q):
    worth = 0
    query = input()
    for position in query:
        worth += ord(position) - 64
    print((names.index(query)+1) * worth)

