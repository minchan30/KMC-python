# 지역변수 사용 예
def func() :
    x = 100
    print(x)

func()


# 메인 루틴에서 지역 변수 사용시 오류
def func() :
    x = 100
    print(x)

func()
print#(x)