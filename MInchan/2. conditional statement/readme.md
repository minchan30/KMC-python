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

---

<br>

## 💡1.3. If ~ 구문

<br>

> #### if~ 구문의 사용 서식은 다음과 같다.

<br>

```
if 조건식:
(tab) 문장 1
(tab) 문장 2
...
```

> #### if의 조건식이 참이면 콜론( : ) 다음 줄에 들여쓰기(tab) 되어 있는 문장 1 , 문장 2 , ... 을 수행한다.
>
> <br>

### 🔥1.3.1. if문의 동작 원리

```py
age = int(input('나이는? '))
ticket = 2000

if age >= 65 :
    ticket = 0

print('나이 : %d세' % age)
print('입장료 : %d원' % ticket)

# 실행결과 1
# (나이가 64세 이하일 경우)
# 나이는? 64
# 나이 : 64세
# 입장료 : 2000원

#실행결과 2
# (나이가 65세 이상일 경우)
# 나이는? 65
# 나이 : 65
# 입장료 : 0원
```

---

<br>

### 🔥1.3.2. 배수 판별하기

```py
num = int(input('양의 정수를 입력하세요 : '))
result = '3의 배수도 4의 배수도 아니다.'

if num % 3 == 0 :
    result = '3의 배수이다.'

if num % 4 == 0 :
        result = '4의 배수이다.'

if num % 3 == 0 and num % 4 == 0 :
        result = '3의 배수이면서 4의 배수이다.'

print('%d은(는) %s' %(num , result))

# 실행결과 1
# 양의 정수를 입력하세요 : 9
# 9은(는) 3의 배수이다.

# 실행결과 2
# 양의 정수를 입력하세요 : 16
# 16은(는) 4의 배수이다.

# 실행결과 3
# 양의 정수를 입력하세요 : 12
# 12은(는) 3의 배수이면서 4의 배수이다.

# 실행결과 4
#양의 정수를 입력하세요 : 29
# 29은(는) 3의 배수도 4의 배수도 아니다.
```

---

<br>

### 🔥1.3.3. 영어 단어 퀴즈 만들기

```py
ans1 = input("'사자'의 영어 단어는 무엇일까요? :")
result = "땡! 틀렸습니다."
if ans1 == 'lion' :
     result = '딩동댕! 참 잘했어요~~~'
print(result)

ans2 = input("'오렌지'의 영어단어는 무엇일까요? :")
result = "땡! 틀렸습니다."
if ans2 == 'orange' :
    result = '딩동댕! 참 잘했어요~~~'
print(result)

ans3 = input("'기차'의 영어단어는 무엇일까요? :")
result = "땡! 틀렸습니다."
if ans3 == 'train' :
    result = '딩동댕! 참 잘했어요~~~'
print(result)

#실행결과
#'사자'의 영어 단어는 무엇일까요? : lion
#딩동댕 참 잘했어요~~~
#'오렌지'의 영어 단어는 무엇일까요? : orange
#딩동댕 참 잘했어요~~~
#'기차'의 영어 단어는 무엇일까요? : drain
#땡! 틀렸습니다.
```

---

<br>

## 💡1.4. if ~ else ~ 구문

<br>

> if ~ else ~ 구문은 짝수 / 홀수 , 남성 / 여성 , 합격 / 불합격 , 수신 / 비수신 , 동의 / 비동의 ,가입 / 미가입 등.. 에서와 같이 두 조건 만이 존재할 경우 사용한다.

---

<br>

### 🔥1.4.1. 짝수 / 홀수 판별하기

```py
x = int(input('양의 정수를 입력하세요 : '))

if x % 2 == 0 :
    print('짝수이다!')

else :
    print('홀수이다!')

# 실행결과 1 (홀수가 입력된 경우)
# 양의 정수를 입력하세요 : 15
# 홀수이다!

#실행결과 2 (짝수가 입력된 경우)
#약의 정수를 입력하세요 : 8
# 짝수이다!
```

---

<br>

### 🔥1.4.2. 자격증 시험 합격 / 불합격 판정하기

```py
pilgi = int(input('필기시험 점수는? '))
silgi = int(input('실기시험 점수는? '))

if pilgi >=80 and silgi >= 80 :
    result = '합격'
else :
    result = '불합격'

print('- 필기시험 점수 : %d' % pilgi)
print('- 실기시험 점수 : %d' % silgi)
print('- 판정 : %s' % result)

# 실행결과 1 (필기 85 , 실기 90이 입력된 경우)
# 필기시험 점수는? 85
# 실기시험 점수는? 90
# - 필기시험 점수 : 85
# - 실기시험 점수 : 90

# 실행결과 2 (필기 95 , 실기 79이 입력된 경우)
# 필기시험 점수는? 95
# 실기시험 점수는? 79
# - 필기시험 점수 : 95
# - 실기시험 점수 : 79
```

---

<br>

### 🔥1.4.2. 영문 소문자 자음 / 모음 판별하기

```py
char = input('영문 소문자 하나를 입력하세요 :')

if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' :
    print('%s은(는) 모음이다.' % char)
else :
    print('%s은(는) 자음이다.' % char)

# 실행결과 1
# 영문 소문자 하나를 입력하세요 : e
# e 은(는) 모음이다.

# 실행결과 2
# 영문 소문자 하나를 입력하세요 : t
# t 은(는) 자ㅔ음이다.
```

---

<br>

## 💡1.5. if ~ elif ~ else ~ 구문

<br>

> if ~ elif ~ 구문은 하나의 if 때문에 하나의 if문에 2개 이상의 조건식이 필요할떄 사용되는데 사용 서식은 다음과 같다.
> <br>

```
if 조건식:
(tab) 문장 1
(tab) 문장 2
     ...
elif 조건식:
(tab) 문장 A
(tab) 문장 B
     ...

...
else:
(tab) 문장 i
(tab) 문장 ii
     ...
```

> if의 저건식이 참이면 들여쓰기 되어있는 문장1 , 문장2 , ... 를 수행하고 , 그렇지 않고 elif의 조건식이 참이면 문장A , 문장B , ... 를 수행하고 , 그렇지 않고 앞의 조건식들이 모두 거짓이면 else 다음의 문장i , 문장ii , ... 를 수식한다.

> if ~ elif ~ else 에서 사용되는 'elif'는 'else if' 의 약어로서 '그렇지 않고 만약' 이라는 의미이다.

---

<br>

### 🔥1.5.1. 점수에 따라 학점 판별하기

```py
score = int(input('점수는?'))

if score >= 90 :
    grade = 'A'
elif score >=80 :
    grade = 'B'
elif score >= 70 :
    grade = 'C'
elif score >= 60 :
    grade = 'D'
else :
    grade = 'F'

print('등급 :' , grade)
```

---

<br>

### 🔥1.5.2. 간단 계산기 만들기

```py
print('기능 선택')
print('1. 더하기')
print('2. 빼기')
print('3. 곱하기')
print('4. 나누기')
print()

s = input('계산기 기능을 선택하세요(1/2/3/4): ')

num1 = int(input('첫 번쨰 숫자를 입력하세요: '))
num2 = int(input('두 번쨰 숫자를 입력하세요: '))

if s == '1':
    print('%d + %d = %d'% (num1 , num2 , num1 + num2))
elif s == '2':
    print('%d - %d = %d'% (num1 , num2 , num1 - num2))
elif s == '3':
    print('%d * %d = %d'% (num1 , num2 , num1 * num2))
elif s == '4':
    print('%d / %d = %d'% (num1 , num2 , num1 / num2))
else:
    print('입력 숫자가 잘못되었습니다!')
```

---

<br>

## 💡1.6. if문의 중첩

<br>

> 앞의 1.3 , 1.4 , 1.5절을 통해 if문의 세가지 구문을 배웠다. 이 구문들이 단독으로 사용되기도 하지만 경우에 따라서는 중첩해서 사용한븐 경우도 있다.

> if ~ elif~ else~ 구문과 if ~ else~ 구문이 중첩되어 사용된 서식은 다음과 같다.
> <br>

```
if조건식 :
(tab) <문장들>

elif 조건식 :
(tab) if 조건식:
(tab)(tab) <문장들>

(tab) else :
(tab)(tab)<문장들>

else :
(tab) 문장들
```

---

<br>

### 🔥1.5.2. 간단 계산기 만들기

```py
print('=' * 50)
now_year = int(input('현재년은?'))
now_month = int(input('현재월은?'))
now_day = int(input('현재일은?'))

birth_year = int(input('출생년은?'))
birth_month = int(input('출생월은?'))
birth_day = int(input('현재일은?'))

if birth_month < now_month :
    age = now_year - birth_year
elif birth_month == now_month :
    if birth_day < now_day :
        age = now_year - birth_year
    else :
        age = now_year - birth_year - 1
else :
    age = now_year - birth_year - 1

print('=' * 50)
print('오늘날짜 : %d년 %d월 %d일' % (now_year , now_month  , now_day))
print('생년월일 : %d년 %d월 %d일' % (birth_year , birth_month  , birth_day))
print('-' * 50)
print('만 나이 : %d세' % age)
print('=' * 50)
```

---
