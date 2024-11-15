N=int(input())
arr=list(map(int, input().split()))
arr.reverse()
for _ in arr:
    print(_,end=' ')
