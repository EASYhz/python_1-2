print(1 in [1, 2, 3])


#for .. 콜론, 들여쓰기
for i in 'python':
    print(i)

#p y t h o n

#Example  4-1

for i in [1, 2, 3, 4, 5]:
    print('9 x {} = {}' .format(i, 9 * i))

#range() .. 순차적으로 증가하는 리스트를 만들어주는 함수
# ex) range(5) = {0, 1, 2, 3, 4}
# range([start,], stop[, step]) -> start, step은 생략가능
# start : 시작 값, stop: 끝 값, step: 앞의 값과 다음 값의 차이
# range(5) == range(0, 5, 1)

for i in range(1,6):
    print(i)


#Exercise1 10 ~ 1까지 출력

for i in range(10, 0, -1):
    print(i, end = ' ')     #end = ' ' -> 줄바꿈X


print()
#Exercise2

num = int(input('정수 입력: '))
result = 1

for i in range(num, 1, -1): # == range(1, num +1)
    result = result * i 

print('{}! == {}'.format(num, result))


#Example -> 구구단

for i in range(1, 10):
    print('{}단 --------'.format(i))
    for j in range(1, 10):
        print("{} X {} = {}" .format(i, j, i * j))


#Exercise3 -> 피라미드 모양

for i in range(1, 6):
    for j in range(i):
        print('*', end = '')
    print()


#while문.. 

#Example
total = 0
i = 1

while i <= 10:
    total += i
    i += 1

print(total)        # i == 11



#Exercise4
num2 = int(input('정수 입력: '))
total2 = 0
i = 1
while i <= num2:
    total2 += i
    i += 1

print('1부터 {}까지 합 : {}'.format(num2, total2))

#Example 
x = 1

while True:
    print(x)
    if (x == 10):
        break
    x += 1

#Exercise 5

for i in range(1, 1001):
    print(i)
    if (i == 10):
        break

#Example
i = 0
while i < 10:
    i += 1
    if (i % 2 == 0):
        continue
    print(i)

