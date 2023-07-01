a = int(input('첫 번쨰 숫자를 입력하세요 :'))
b = int(input('두 번쨰 숫자를 입력하세요 :'))
print('원하는 연산은?')
d = input('+ , - , * , / 중 하나를 선택하세요 : ')

if d == '+' :
    print('%d + %d = %d' % (a , b , a + b))

elif d == '-' :
    print('%d - %d = %d' % (a , b , a - b))

elif d == '*' :
    print('%d * %d = %d' % (a , b , a * b))

elif d == '/' :
    print('%d / %d = %d' % (a , b , a / b))