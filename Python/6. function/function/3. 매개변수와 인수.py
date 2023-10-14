# 매개변수와 인수의 개수 일치
def print_name(first_name , last_name) :
    name = first_name + last_name
    print('이름 :' , name)

print_name('홍' , '정원')


# 매개변수에서의 오류 발생
def print_name(first_name , last_name) :
    name = first_name + last_name
    print('이름 :' , name)

print_name('최')