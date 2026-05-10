def solve():
    n = int(input())
    l = list(map(int, input().split()))
    def shift(l1):
        bloc = 0
        for i in range(len(l1)-2 , -1 , -1 ):
            if l1[i] > l1[i+1]:
                d = l1[i] - l1[i+1]
                l1[i+1] += d
                l1[i] -= d
                bloc += d
        return bloc
    bloc = 0

for i in range(len(l) - 1, 0, -1):   # iterate from end to start
    temp = l[:]                       # copy list
    temp[i] -= 1                      # subtract 1 from current index

    bloc = max(bloc, shift(temp))
i = int(input())
for _ in range(i):
    solve()
