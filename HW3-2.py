id = 'lovePython!'
pw = 'p12345'

inputId = input('아이디 입력: ')
inputPw = input('비밀번호 입력: ')

if (inputId == id):
    if (inputPw == pw):
        print('{} 님 환영합니다~!!'.format(id))
    else:
        print('비밀번호가 틀립니다.')
else:
    print('아이디를 찾을 수 없습니다.')
    