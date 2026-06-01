a,b = map(int,input().split())
print(a,b,end=' ')
for _ in range(8):
    print((a+b)%10,end=' ')
    temp = a
    a = b
    b = b+temp