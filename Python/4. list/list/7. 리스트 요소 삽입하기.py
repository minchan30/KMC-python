# insert( ) 메소드로 요소 삽입하기
fruits = ['apple' , 'orange' , 'banana' , 'cherry']
print(fruits)


fruits.insert(1 , 'melon')
print(fruits)


fruits.insert(2 , 'strawberry')
print(fruits)
# 실행결과
# ['apple', 'orange', 'banana', 'cherry']
# ['apple', 'melon', 'orange', 'banana', 'cherry']
# ['apple', 'melon', 'strawberry', 'orange', 'banana', 'cherry']