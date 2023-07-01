# 1. 🧑‍💻조건문

<br>

## 💡1.1 조건문이란

> #### 파이썬의 조건문인 if문은 다음의 예시에와 같이 조건식의 참 또는 거짓에 따라 실행되는 코드가 달라 질때 사용한다.

<br>

```py
if x > 0
print("양수이다!")

else :
    print("음수 또는 0이다!")
```

---

<br>

## 💡1.2 비교 연산자와 논리 연산자

> #### 비교 연산자와 논리 연산자는 if문(또는 뒤에서 배우는 for문 , while문)의 조건식에 사용되어 조건이 참(True)인지 거짓(false)인지를 판정하는 데 사용한다.

 <br>

| 연산자      |           종류            |
| :---------- | :-----------------------: |
| 비교 연산자 | > , < , == , != , <= , >= |
| 논리 연산자 |      and , or , not       |

## ✨비교 연산자
<br>

```py
print(5 == 5)
# true

print(10 > 20)
# false

print(8 <= 8)
# true


a = 10
b = 20
print(a == b)
# false

print(a != b)
# true

print(a % b >= 10)
# true
```
<br>

## ✨논리 연산자
<br>

```py
score1 = 75
score2 = 90
print(score1 >= 80 and score2 >= 80)
# false

score1 = 85
score2 = 95
print(score1 >= 80 and score2 >= 80)
# true

x = 10
print(x % 2 == 0 or x % 6 == 0)
# true

x = 16
print(x % 3 == 0 or x % 5 == 0)
# false

x = 25
print(not x % 2 == 0)
# true

print(not x > 10)
# false
```