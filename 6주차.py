#Tuple
#Tuple 명령어 - index, slice, concatenation, repetiton, len()..

#Tuple.. 한번 생성되면 내용 수정 X.. = 읽기 전용 배열
# 리스트는 수정가능
#튜플 .. 동일한 유형의 데이터, 혼합 유형의 데이터 가질 수 있음
'''
중첩 가능
소괄호로 정의
소괄호 생략가능
'''

#빈 튜플
empty_tuple = ()

#여러개의 문자열
tuple1 = ("HI", 1, 2.4)
tuple2 = ("book", [1,2,3])
tuple3 = ((2,3,4), (1,2,"hi"))
tuple4 = (77,)      # 77뒤에 , 없으면 정수형 변수로 취급

'''
튜플은 값 변경 불가.. append나 remove 사용 불가
'''

#index
tu = (12,23,43, 'bar')
tu[1]   # 23
#slice
tu[1:3] #23,43

p = (43,'ff')

t = (tu + p)  # (12, 23, 43, 'bar', 43, 'ff')
print(t) 

print(tu * 3)  #(12,23,43, 'bar', 12,23,43, 'bar', 12,23,43, 'bar')

#음수 인덱싱 가능


#중첩 튜플에서 이중인덱스
tu2 = (1, 'steve', (11,22,33))
print(tu2[1][3])            #v
print(tu2[2][1])               # 22

#len() - 튜플의 길이
# in 키워드 - 지정된 요소가 튜플에 있는지 '여부' 테스트

print('bar' in tu2)         #False


'''
중첩 튜플의 길이 - 모든 개별 튜플의 개수
ex) data = ((2,3,5), (3,4))
len(data) => 2
'''

# zip()  서로를 쌍으로 묶어 새로운 튜플 생성
a = ("H", "dd")
b = ("z", "cc", "dc")  # dc는 쌍을 이루지 못해서 무시 됨
x = zip(a, b)   # (("H", "Z"), ("dd","cc")) 
print(x)

# 언패킹 연산 - 각각의 변수에 순서대로 대입
tud = (12,343)
y, z = tud # y =12  z = 243

# 형변환
st = (12, 20, 30)  # 튜플
li = list(st) # 형변환 -> [12,20,30]
