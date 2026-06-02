n = int(input())

# Please write your code here.
num = [i for i in range(1,10)]
now = 0
for i in range(n):
    for j in range(n):
        print(num[now],end=' ')
        now = (now+1) % 9
    print()
