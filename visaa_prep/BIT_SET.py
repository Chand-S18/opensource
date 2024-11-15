N=int(input())
k=int(input())
b_bit=str(0*k)+bin(N)[2:]
if len(b_bit)>=k and b_bit[-k]=='1':
    print("true")
else:
    print("false").
