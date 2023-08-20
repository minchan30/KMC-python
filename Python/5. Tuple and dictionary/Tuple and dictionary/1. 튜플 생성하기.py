# 튜플 생성
animals = ('토끼' , '거북이' , '사자' , '여우') # 튜플 animals 생성
print(animals)

numbers = tuple(range(10)) # tuple( ) 을 이용한 튜플 생성
print(numbers)


# 실행결과
# ('토끼', '거북이', '사자', '여우')
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


# 튜플 요소 수정 시 오류 발생
animals = ('토끼' , '거북이' , '사자' , '여우')

animals[2] = '호랑이'


# 실행결과
# Traceback (most recent call last):
#   File "c:\Users\kmcjj\OneDrive\문서\dev\ChanK-python\Python\5. Tuple and dictionary\Tuple and dictionary\1. 튜플 생성하기.py", line 17, in <module>
#     animals[2] = '호랑이'
#     ~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment