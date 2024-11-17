N=int(input())
Matrix=[]
for i in range(N):
    X=list(map(int, input().split()))
    Matrix.append(X)
for i in range(N):
    for j in range(N-1,-1,-1):
        print(Matrix[i][j],end=' ')
    print()
