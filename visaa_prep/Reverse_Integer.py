N=int(input())
sign=-1 if N<0 else 1
N=abs(N)
X=int(str(N)[::-1])*sign
if -2**31<=X and X<=2**31+1:
    print(X)
else:
    print('0')
