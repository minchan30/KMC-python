# 매개변수에서 리스트 전달하기
def func(food) :
    for x in food :
        print(x)

fruits = ['사과' , '오렌지' , '바나나']

func(fruits)


# func() 함수에서 리스트 요소 추가하기
def func(food) :
    food.append('딸기')
    food.append('수박')

fruits = ['사과' , '오렌지' , '바나나']

print(fruits)
func(fruits)
print(fruits)