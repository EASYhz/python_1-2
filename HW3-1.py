num1 = int(input('첫번째 정수 입력: '))
num2 = int(input('두번째 정수 입력: '))
num3 = int(input('세번째 정수 입력: '))

max = 0

if num1 < num2:
    if num2 < num3:
        max = num3
    elif num3 < num2:
        max = num2        
elif num2 < num1:
    if num1 < num3:
        max = num3
    elif num3 < num1:
        max = num1

print('{}, {}, {} 중 제일 큰 수는 {}'.format(num1, num2, num3, max))