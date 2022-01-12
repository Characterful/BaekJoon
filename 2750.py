n = int(input())

number = []

for i in range(n) : 
    number.append(int(input()))
k = 0
for i in range(len(number)):
    for j in range(len(number)):
        if(number[i] < number[j]):
            number[i], number[j] = number[j], number[i]

for i in number : 
    print(i)