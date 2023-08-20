# 1 . 📄리스트

<br>

## 1.1. ✨리스트란?

> #### 리스트는 여러 개의 데이터 값을 하나의 변수, 즉 리스트에 담을 수 있는 데이터 구조이다. 리스트는 다음과 같이 요소들을 콤마( , ) 로 분리하고 대괄호 ( [ ] ) 로 둘러싸게 된다.

```py
# ex) score = [90 , 89 , 77 , 95 , 67]
# ex) fruit = []
```

<br>

---

<br>

### 1.1.1. 💡리스트 생성

> 리스트를 생성할 떄는 다음 예제에서와 같이 대괄호 ( [ ] ) 또는 list( ) 함수를 사용한다

```py
list1 = [3 , 15 , -12.5 , '사과' , '딸기']
print(list1)

list2 = list(range(1 , 21 , 2))
print(list2)

# 실행결과
# [3, 15, -12.5, '사과', '딸기']
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```

<br>

---

<br>

### 1.1.2. 💡리스트 요소 추출

```py
color = ['빨강' , '주황' , '노랑' , '초록' , '파랑' , '남색' , '보라']

print(color[0])
print(color[5])
print(color[2 : 6])
print(color[-3])
print(color[-4 : -1])

# 실행결과
# 빨강
# 남색
# ['노랑', '초록', '파랑', '남색']
# 파랑
# ['초록', '파랑', '남색']
```

<br>

---

<br>

## 1.2. ✨반복문과 리스트

> 리스트는 for문이나 while문 같은 반복문과 같이 많이 사용된다. 반복문의 반복 루프에서는 리스트의 각 요소를 반복적으로 읽어 들여 처리함으로써 리스트의 요소들을 효율적으로 다룰 수 있다.

<br>

---

<br>

### 1.2.1. 💡for문에서 리스트 사용 예

```py
colors = ['빨간색' , '파란색' , '노란색' , '검정색' , '초록색']

for color in colors :
    print('나는 %s을 좋아한다' % color)

# 실행결과
# 나는 빨간색을 좋아한다
# 나는 파란색을 좋아한다
# 나는 노란색을 좋아한다
# 나는 검정색을 좋아한다
# 나는 초록색을 좋아한다
```

<br>

---

<br>

### 1.2.2. 💡for문에서 range( ) 함수 예

```py
colors = ['빨간색' , '파란색' , '노란색' , '검정색' , '초록색']

n = len(colors)
for i in range(0 , n) :
    print('나는 %s를 좋아한다' % colors[i])

# 실행결과
# 나는 빨간색을 좋아한다
# 나는 파란색을 좋아한다
# 나는 노란색을 좋아한다
# 나는 검정색을 좋아한다
# 나는 초록색을 좋아한다
```

<br>

---

<br>

## 1.3. ✨리스트 요소 변환

> 리스트 요소 값의 수정 , 리스트에 새로운 리스트 추가 , 리스트에 요소 삽입 , 리스트 요소 위치 찾기 , 그리고 리스트에서 요소를 삭제하는 방법이 있다.
> <br>

---

<br>

### 1.3.1. 💡리스트 요소 수정하기

```py
flowers = ['목련' , '벚꽃' , '장미' , '백일홍']
print(flowers)

flowers[1] = '무궁화'
print(flowers)

# 실행결과
# ['목련', '벚꽃', '장미', '백일홍']
# ['목련', '무궁화', '장미', '백일홍']
```

<br>

---

<br>

### 1.3.2. 💡리스트 요소 추가하기

```py
#리스트 새로운 요소 추가
arr = [5 , 3 , 12 , 9 , 2]
print(arr)


arr.append(10)
print(arr)

# 실행결과
# [5, 3, 12, 9, 2]
# [5, 3, 12, 9, 2, 10]


# 빈 리스트에 요소 추가
scores = []


while True :
    score = int(input('성적을 입력하세요(종료 : -1) :'))


    if score == -1 :
        break
    else :
        scores.append(score)

print(scores)

# 실행결과
# [95, 88, 76]
```

<br>

---

<br>

### 1.3.3. 💡리스트 요소 삽입하기

```py
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
```

<br>

---

<br>

### 1.3.4. 💡리스트 요소 위치 찾기

```py
# index( ) 메소드로 요소의 인덱스 구하기

number = [5 , 20 , 13 , 7 , 8 , 22 , 7 , 17]
print(number)


idx = number.index(7)
print(idx)

# 실행결과
# [5, 20, 13, 7, 8, 22, 7, 17]
# 3
```

<br>

---

<br>

### 1.3.5. 💡리스트 요소 삭제하기

```py
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
```

<br>

---

<br>

## 1.4. ✨리스트 다루기

> 리스트 다루기에서는 리스트의 병합 , 리스트 요소들의 합계 , 리스트 순서 거꾸로 하기 , 리스트의 요소 정렬 , 그리고 리스트를 복사하는 방법에 대해 설명한다.

<br>

---

<br>

### 1.4.1. 💡리스트 병합하기

```py
#리스트 병합
person1 = ['kim' , 24 , 'kim@naver.com']
person2 = ['lee' , 35 , 'lee@hanmail.net']

person = person1 + person2

print(person)

# 실행결과
# ['kim', 24, 'kim@naver.com', 'lee', 35, 'lee@hanmail.net']
```

<br>

---

<br>

### 1.4.2. 💡리스트 합계 구하기

```py
# 리스트 요소의 합계와 평균
scores = [80 , 90 , 85 , 95 , 100]

sm = sum(scores)
avg = sm / len(scores)

print('합계 :' , sm)
print('평균 :' , avg)

# 실행결과
# 합계 : 450
# 평균 : 90.0
```

<br>

---

<br>

### 1.4.3. 💡리스트 순서 반대로 하기

```py
# reverse( ) 메소드로 리스트 순서 반대로 하기
data = [10 , 20 , 30 , 40 , 50]
print(data)

data.reverse()
print(data)

# 실행결과
# [10, 20, 30, 40, 50]
# [50, 40, 30, 20, 10]
```

<br>

---

<br>

### 1.4.4. 💡리스트 복사하기

```py
# copy( ) 메소드로 리스트 복사하기
fruits = ['apple' , 'banana' , 'orange']
print(fruits)

x = fruits.copy()
print(x)

# 실행결과
# ['apple', 'banana', 'orange']
# ['apple', 'banana', 'orange']
```

<br>

---

<br>

### 1.4.5. 💡리스트 정렬하기

```py
#sort( ) 메소드로 리스트 정렬하기
data = [12 , 8 , 15 , 32 , -3 , -20 , 15 , 34 , 6]
print(data)

data.sort()
print(data)

data.sort(reverse = True)
print(data)

# 실행결과
# [12, 8, 15, 32, -3, -20, 15, 34, 6]
# [-20, -3, 6, 8, 12, 15, 15, 32, 34]
# [34, 32, 15, 15, 12, 8, 6, -3, -20]
```

<br>

---

<br>

## 1.5. ✨문자열과 리스트

> 문자열과 리스트에서는 문자열에서 특정 문자열 찾기 , 문자열 치환 , 문자열 쪼개기등에 사용되는 메소드와 리스트에서 문자열을 처리하는 방법에 대해 설명한다

<br>

---

<br>

### 1.5.1. 💡문자열 찾기

```py
string1 = 'Python is fun!'
print(string1)

x = string1.find('fun')
print(x)

# 실행결과
# Python is fun!
# 10
```

<br>

---

<br>

### 1.5.2. 💡문자열 치환하기

```py
# replace( ) 메소드로 문자열 치환하기
string1 = '사과는 맛있다. 나는 사과를 제일 좋아한다.'
print(string1)

x = string1.replace('사과' , '딸기')
print(x)

# 실행결과
# 사과는 맛있다. 나는 사과를 제일 좋아한다.
# 딸기는 맛있다. 나는 딸기를 제일 좋아한다.

# 전화번호에서 하이픈 삭제하기
phone1 = '010-3523-1629'
print(phone1)

phone2 = phone1.replace('-' , "")
print(phone2)

# 실행결과
# 010-3523-1629
# 01035231629
```

<br>

---

<br>

### 1.5.3. 💡문자열 쪼개기

```py
hello = 'have a nice day'
print(hello)

list1 = hello.split(' ')
print(list1)
print(type(list1))

for i in range(0 , len(list1)) :
    print('list1[%d] : %s' %(i , list1[i]))

# 실행결과
# have a nice day
# ['have', 'a', 'nice', 'day']
# <class 'list'>
# list1[0] : have
# list1[1] : a
# list1[2] : nice
# list1[3] : day
```

<br>

---

<br>

### 1.5.4. 💡리스트 문자열로 변환하기

```py
# join( ) 메소드로 리스트를 문자열로 변환하기
names = ['황예린' , '홍지수' , '안진영']
print(names)

x = '/'.join(names)
print(x)

# 실행결과
# ['황예린', '홍지수', '안진영']
# 황예린/홍지수/안진영

# 전화번호에 하이픈(-) 삽입된 문자열로 변환하기
phone1 = ['010' , '1234' , '5678']
print(phone1)

phone2 = '-'.join(phone1)
print(phone2)

# 실행결과
# ['010', '1234', '5678']
# 010-1234-5678
```

<br>

---

<br>

### 1.5.5. 💡리스트 문자열에서 하이픈 삭제하기

```py
# 리스트 문자열에서 하이픈('-') 삭제하기
phone_list1 = ['010-3523-1629' , '010-6276-0905' , '010-8663-1628' , '010-8345-3378']
print(phone_list1)

phone_list2 = []
for number in phone_list1 :
    x = number.replace('-' , "")

    phone_list2.append(x)

print(phone_list2)

# 실행결과
# ['010-3523-1629', '010-6276-0905', '010-8663-1628', '010-8345-3378']
# ['01035231629', '01062760905', '01086631628', '01083453378']
```

<br>

---

<br>

### 1.5.6. 💡리스트에서 문자열 치환하기

```py
# 리스트 문자열에서 문자 치환하기
sentences = ['Love me, love my dog.' , 'No news is good news.' ,
            'Blood is thicker than water']

for sentence in sentences :
    x = sentence.replace(" " , "_")
    print(x)

# 실행결과
# Love_me,_love_my_dog.
# No_news_is_good_news.
# Blood_is_thicker_than_water
```

<br>

---

<br>

## 1.6. ✨2차원 리스트

> 2차원 리스트는 리스트의 각 요소에 있는 데이터의 형이 리스트인 경우이다. 2차원 리스트에서는 2차원 리스트의 기본 구조와 2차원 리스트를 반복문에서 활용하는 방법을 설명한다

<br>

---

<br>

### 1.6.1. 💡2차원 리스트의 구조

```py
# 2차원 리스트의 구조
numbers = [[10 , 20 , 30] , [40 , 50 , 60 , 70 , 80]]

print(numbers[0][0])
print(numbers[0][1])
print(numbers[0][2])
print(numbers[1][0])
print(numbers[1][1])
print(numbers[1][2])
print(numbers[1][3])
print(numbers[1][4])

# 실행결과
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
```

<br>

---

<br>

### 1.6.2. 💡2차원 리스트와 이중 for문

```py
# 2차원 리스트의 이중 for문
data = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]

for i in range(4) :
    for j in range(2) :
        print('data[%d][%d] = %d' % (i , j , data[i][j]))

# 실행결과
# data[0][0] = 10
# data[0][1] = 20
# data[1][0] = 30
# data[1][1] = 40
# data[2][0] = 50
# data[2][1] = 60
# data[3][0] = 70
# data[3][1] = 80
```

<br>

---

<br>

### 1.6.3. 💡2차원 리스트로 합계와 평균 구하기

```py
# 2차원 리스트로 성적 합계와 평균 구하기
scores = [[75 , 83 , 90] , [86 , 86 , 73] , [76 , 95 , 83] , [89 , 96 , 69] , [86 , 79 , 93]]

for i in range(len(scores)) :
    sum = 0
    for j in range(len(scores[i])) :
        sum = sum + scores[i][j]

    avg = sum / len(scores[i])

    print('%d번쨰 학생의 합계 : %d , 평균 : %.2f' % (i + 1 , sum , avg))

# 실행결과
# 1번쨰 학생의 합계 : 248 , 평균 : 82.67
# 2번쨰 학생의 합계 : 245 , 평균 : 81.67
# 3번쨰 학생의 합계 : 254 , 평균 : 84.67
# 4번쨰 학생의 합계 : 254 , 평균 : 84.67
# 5번쨰 학생의 합계 : 258 , 평균 : 86.00
```

<br>

---

<br>

### 1.6.4. 💡2차원 리스트로 문자열 다루기

```py
# 2차원 리스트로 문자열 다루기
strings = [['원두커피' , '라떼' , '콜라'] , ['우동' , '국수' , '피자' , '파스타']]

for i in range(len(strings)) :
    for j in range(len(strings[i])) :
        print(strings[i][j])

# 실행결과
# 원두커피
# 라떼
# 콜라
# 우동
# 국수
# 피자
# 파스타
```
