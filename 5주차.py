#List Method
# range, append, insert, del, clear, pop
# count, sort, reverse, index, slice,
# concatenation, repetition, length, memebership test


# append(), insert(), len()
name = ['John', 'Rosa', 'Maria']
name.append('Danny') # 마지막에 추가
print(name)
name.insert(2, 'Alex')  #n번째에 ''넣기
print(name)
name[1] = 'Selly'
print(name)
print(len(name))

#remove(), del, pop(), clear()
name.remove('Alex')
print(name)
del name[1]
print(name)
name.pop()  #마지막 거 삭제
print(name)
name.clear() #빈 리스트로 만듦
print(name)

# Example
bucketList = ['서울', '대구', '부산']
bucketList.append('제주')
print(bucketList)
print(len(bucketList))
bucketList.insert(1, '대전')
print(bucketList)
bucketList.remove('서울')
print(bucketList)
bucketList.pop()
print(bucketList)
bucketList.clear()
print(bucketList)


#slice - 시퀀스 자료 중 특정 범위를 지정하여 특정 요소를 가져오는 방법
List1 = ['홍길동', 22, '서울', '속초', '부산', '제주']
print(List1[0:6:2])     # 0부터 6개 .. 2만큼 증가 출력
print(List1[2:6])       # 인덱스 2부터 5까지 출력
print(List1[3:])        # 인덱스 3부터 끝까지 출력
print(List1[:2])        # 처음부터 인덱스 2까지 출력


# 음수 인덱싱 .. 인덱스 -1은 리스트 마지막 요소를 가리킴. -2는 끝에서 두번째..
List2 = ['A', 'B', 'C', 'D']
print(List2[-1])       # D
print(List2[-3])       # B
print(List2[-4])       # A

# 문자열 slice
a = 'Life is short'
print(a[0:4])       #Life
print(a[-6:])       # short


# 리스트 연산
goodPlace = ['Rome', 'Paris', 'Hanoi']
city = ['Tokyo', 'Danang']
print(goodPlace + city)  # ['Rome', 'Paris', 'Hanoi', 'Tokyo', 'Danang']
print(city * 3) #['Tokyo', 'Danang','Tokyo', 'Danang', 'Tokyo', 'Danang']


# index() .. 몇번째 요소인지 인덱스 번호를 반환 ***대소문자 판별***
goodPlace = ['Rome', 'Paris', 'Hanoi']
num1 = goodPlace.index('Paris')
print(num1)

'Rome' in goodPlace         #True
'New York' in goodPlace     #False

# count().. 리스트에 해당 항목이 몇번 포함 되어있는지 반환
goodPlace2 = ['Rome', 'Paris', 'Hanoi', 'Rome']  
print(goodPlace2.count('Rome'))     #2


# sort().. 오름차순
# reverse().. 리스트 거꾸로 뒤집기
name = [1, 6, 3]
name.sort()
print(name)
name.reverse()
print(name)

# 문자열과 정수 요소 사이에서는 관계 연산자 사용 X -> 정렬 X, 비교 X

'''
for i in 리스트:
    print(i)
'''

'''
while i < 리스트:
    print(리스트[i])
    i += 1
'''


#Exercise
temp = []
for i in range(1, 6):
    temperature = int(input("온도 입력: "))
    temp.append(temperature)

print("평균 온도: {}".format(sum(temp) / len(temp)))


# split() .. 
# split([separator], [max])
# seperator: 문자열을 분할하는 기호, 생략하면 기본값은 공백
# max : 구분자로 사용할 개수

# split() : string
quiz = 'python.program.good'
sp = quiz.split('.')        # ['python', 'program', 'good']
print(sp)           
sp = quiz.split('.', 1)     # ['python', 'program.good']

quiz = 'python program good'
sp = quiz.split(' ')         # ['python', 'program', 'good']
print(sp)

quiz = 'python/program/good'
sp = quiz.split('/')        # ['python', 'program', 'good']
print(sp)

# split() : List.. 리스트는 split()이 없다 .. 
# 하나의 항목으로 묶여있으면 쉼표로 구분하여 리스트 요소로 나눌 수 있음
List3 = ['부산, 제주, 속초, 대전']
for i in List3:
    sp2 = i.split(',')          # ['부산', '제주', '속초', '대전']
print(sp2) 


# join() : string, List
# joint()은 리스트 내 구분자로 구분되어진 요소를 추가하여
# 합쳐서 문자열로 만듦

sp = ['python', 'program', 'good']
sp2 = ['부산', '제주', '속초', '대전']
quiz = ','.join(sp)         # 'python,program,good'
print(quiz)
List4 = '/'.join(sp2)       # '부산/제주/속초/대전'
print(List4)
List5 = ': '.join('abcd')           # 'a: b: c: d'
print(List5)
List6 = '/'.join('abcd')            # 'a/b/c/d'
print(List6)
List7 = '\n'.join('123')
print(List7)

# enumerate() .. 
# 순서가 있는 자료형(리스트, 튜플, 딕셔너리 등)을 입력 받아
# 인덱스와 요소를 반환
'''
    for i, value in enumerate(시퀀스 자료형 이름, [sequence]):
        print(i, value)
'''
# 2개의 매개 변수가 필요함
# 시퀀스 자료형 이름: 리스트, 튜플 딕셔너리 등
# [sequence]는 인덱스 시작 번호 지정, 생략하면 기본값 => 0
# i는 인덱스 번호, value는 요소

#example
List8 = ['부산', '제주', '속초', '대전']
for i, value in enumerate(List8, 1):
    print(i, value)

'''
result>
1 부산
2 제주
3 속초
4 대전
'''


#Exercise 1
test = [57, 99, 78, 85, 60]
for i, value in enumerate(test, 1):
    if value >= 70:
        print('{}. 학생의 점수: {}  합격!'.format(i, value))
    else:
        print('{}. 학생의 점수: {}  불합격!'.format(i, value))

# max() 최대
# min() 최소
# sum() 합

# 단독으로 쓰임. 함수.. 메소드 X

# 구구단 만들기
for dan in range(2,10):
    for i in range(1, 10):
         print('{} x {} = {}'.format(dan, i, dan *i))
    print()
