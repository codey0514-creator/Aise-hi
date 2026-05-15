def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    l1 = arr[:]
    bloc = 0
    for i in range(n-2, -1, -1):
        if l1[i] > l1[i+1]:
            d = l1[i] - l1[i+1]
            l1[i+1] += d
            l1[i] -= d
            bloc += d
    last_occ = [-1] * (n + 2)
    for j in range(n):
        last_occ[arr[j]] = j
    last_below = [-1] * (n + 2)
    for v in range(1, n + 2):
        last_below[v] = max(last_below[v-1], last_occ[v-1])
    ans = bloc
    for i in range(n):
        h = arr[i]
        lb = last_below[h]
        if lb < i:
            bonus = i - 1 - lb
            ans = max(ans, bloc + bonus)
    print(ans)
t = int(input())
for _ in range(t):
    solve()