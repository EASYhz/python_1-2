# if 문
# 0 -> False , 1 -> True

money = True
if money:
    print('택시를 탄다')
else:
    print('걸어간다')

# 들여쓰기 필수


x = int(input('Type the integer: '))

if x > 0:
    print(x, '는 양수이다.')
elif x == 0:
    print(x, '는 0 이다.')
else:
    print(x, '는 음수이다.')


#example
score = int(input('점수를 입력하세요: '))
if score >= 80:
    print('PASS')
else:
    print('FAIL')


#Exercise 1
num1 = int(input('Please type the integer'))

if num1 % 2 == 0:
    print('짝수')
else:
    print('홀수')


#Example
score2 = int(input('점수를 입력하세요: '))
if score2 >= 80 and score2 <= 100: # 80 <= score2 <= 100 도 가능
    print('축하합니다')
else:
    print('장학금을 받을 수 없습니다.')

#Exercise 2
num2 = int(input('정수를 입력하세요: '))
if num2 % 2 == 0 and num2 % 3 == 0:
    print('{}는 2와 3으로 나누어 떨어집니다.'.format(num2))
else:
    print('{}는 2와 3으로 나누어 떨어지지 않습니다.'.format(num2))
