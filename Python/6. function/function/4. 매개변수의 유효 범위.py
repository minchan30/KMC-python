# 매개변수의 사용 예 : 짝수 홀수 판별
def even_odd(n) :
    if n % 2 == 0 :
        print("%d은(는) 짝수이다" %n)
    else :
        print('%d은(는) 홀수이다' %n)

x = int(input('양의 정수를 입력하세요 :'))
even_odd(x)


# 매개변수를 메인 루틴에서 사용하는 경우
def even_odd(n) :
    if n % 2 == 0 :
        print("%d은(는) 짝수이다" %n)
    else :
        print('%d은(는) 홀수이다' %n)

x = int(input('양의 정수를 입력하세요 :'))
even_odd(x)
#print(n)