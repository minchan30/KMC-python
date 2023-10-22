# 전역변수 사용 예
def func() :
    print(x)

x = 100
func()
print(x)


# 동일한 이름의 전역 지역 변수 사용 예
def func() :
    x = 200
    print(x)

x = 100
func()
print(x)