# 키워드 global 개념 익히기
def func() :
    global x
    x = 200
    print(x)

x = 100
print(x)
func()
print(x)


# 키워드 global을 이용한 면적과 둘레 구하기
def cir_area() :
    global r
    result = r * r * 3.14
    return result

def cir_length() :
    global r
    result = 2 * 3.14 * r
    return result

r = float(input('반지름을 입력하세요 :'))
area = cir_area()
length = cir_length()

print('원의 면적 : %.1f , 원주의 길이 : %.1f' % (area , length))


# 매개변수를 이용한 원의 면적과 둘레 구하기
def cir_area(r) :
    result = r * r * 3.14
    return result

def cir_length(r) :
    result = 2 * 3.14 * r
    return result

r = float(input('반지름을 입력하세요 :'))
area = cir_area(r)
length = cir_length(r)
print('원의 면적 : %.1f , 원주의 길이 : %.1f' % (area , length))