x = input('첫 번째 숫자를 입력하세요 :')
y = input('두 번쨰 숫자를 입력하세요 :')
z = (int(x) + int(y))

if int(z) % 3 != 0 :
    print(z ,'(은)는 3의 배수가 아니다.')

else :
    print(z ,'(은)는 3의 배수가 맞다.')
