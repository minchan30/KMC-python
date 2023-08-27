# 1. 🧑‍💻튜플과 딕셔너리

## 1.1 💥튜플이란?

> 튜플이란 리스트와 많은 부분이 유사하고 사용법도 거의 비슷하다. 튜플과 리스트의 차이점은 두 가지로 볼 수 있다.

```py
1. 튜플에서는 리스트의 대괄호( [] ) 대신에 소괄호( () )를 사용한다.
2. 튜플에서는 리스트와 달리 요소의 수정과 추가가 불가능 하다.
```

<br>

---

### 1.1.1. 💡튜플 생성하기

> 튜풀은 생성하려면 다음과 같이 소괄호 , ( )를 이용하거나 tuple( )함수를 사용한다.

```py
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
```
