# 1. 🧑‍💻조건문

<br>

## 💡1.1. 조건문이란

<br>

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

### 🔥1.1.1. if문의 동작 원리

```py
x = int(input('정수를 입력하세요 : '))

if x > 0 :
    print('입력된 수는 양수입니다.')
    print('입력된 수는 양수입니다.')


# 실행결과 1
# 정수를 입력세요 : 25
# 입력된 수는 양수입니다.
# 입력된 수는 양수입니다.

# 실핼결과 2
# 정수를 입력하세요 : -5
```

---

<br>

## 💡1.2. 비교 연산자와 논리 연산자

<br>

> #### 비교 연산자와 논리 연산자는 if문(또는 뒤에서 배우는 for문 , while문)의 조건식에 사용되어 조건이 참(True)인지 거짓(false)인지를 판정하는 데 사용한다.

 <br>

| 연산자      |           종류            |
| :---------- | :-----------------------: |
| 비교 연산자 | > , < , == , != , <= , >= |
| 논리 연산자 |      and , or , not       |

---

<br>

### ✨1.2.1. 비교 연산자

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

---

<br>

### ✨1.2.2. 논리 연산자

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

## 💡1.3. If ~ 구문

<br>

> #### if~ 구문의 사용 형식
>
> <br>

```
if 조건식:
(tab) 문장 1
(tab) 문장 2
...
```

> #### if의 조건식이 참이면 콜론( : ) 다음 줄에 들여쓰기(tab) 되어 있는 문장 1 , 문장 2 , ... 을 수행한다.
