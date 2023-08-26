# 딕셔너리 요소 삭제
car = {'brand' : '현대' , 'model' : '아반떼' , 'start' : 1990 , 'year' : 2021}
print(car)

x = car.pop('start')
print(x)

print(car)

# 실행결과
# {'brand': '현대', 'model': '아반떼', 'start': 1990, 'year': 2021}
# 1990
# {'brand': '현대', 'model': '아반떼', 'year': 2021}


#딕셔너리 전체 요소 삭제
car = {'brand' : '현대' , 'model' : '아반떼' , 'start' : 1990 , 'year' : 2021}
print(car)

car.clear()
print(car)

# 실행결과
# {'brand': '현대', 'model': '아반떼', 'start': 1990, 'year': 2021}
# {}