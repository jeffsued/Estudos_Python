num = int(input())
for i in range(1, num):
    if i % 2 == 0 and num % i == 0  :
        print(i)