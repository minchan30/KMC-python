#remove( ) 메소드로 리스트의 요소 삭제
member = ['홍지웅' , 20 , '경기도 김포시' , 'jiwoong@naver.com' , '010-1234-5678']
print(member)


member.remove(20)
print(member)

#실행결과
# ['홍지웅', 20, '경기도 김포시', 'jiwoong@naver.com', '010-1234-5678']
# ['홍지웅', '경기도 김포시', 'jiwoong@naver.com', '010-1234-5678']


#pop( ) 메소드로 리스트의 요소 삭제
date = [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80]
print(date)


x = date.pop(2)
print(x)
print(date)


x = date.pop(3)
print(x)
print(date)

#실행결과
# [10, 20, 30, 40, 50, 60, 70, 80]
# 30
# [10, 20, 40, 50, 60, 70, 80]
# 50
# [10, 20, 40, 60, 70, 80]

#리스트의 모든 요소 삭제
data = [3 , 12 , 7 , -3 , -9]
print(data)

data.clear()
print(data)

# 실행결과
# [3, 12, 7, -3, -9]
# []