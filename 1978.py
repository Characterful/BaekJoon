n = int(input())
number = map(int, input().split())
answer = 0
for num in number:
    error = 0
    if num > 1:
        for i in range(2,num):
            if num % i==0:
                error+=1
                break
        if error==0:
            answer+=1

print(answer)