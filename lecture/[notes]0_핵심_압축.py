"""
파이썬 기초 프로그래밍 완전 정리
=================================================

[1단계] 기본 개념 및 연산
=================================================

1. 변수와 자료형
-------------------------------------------------
변수 = 데이터를 저장하는 상자
프로그램이 실행되면서 값을 저장했다가 필요할 때 꺼내서 사용한다.

자료형의 종류:
① int(정수): 10, -5, 0 (소수점 없음)
② float(실수): 3.14, -2.5, 0.1 (소수점 있음)
③ str(문자): 'hello', "world" (따옴표로 감싼 텍스트)
④ bool(논리): True, False (참/거짓)

type(값) → 자료형 확인
"""

x = 10
y = 3.14
name = 'Alice'
is_valid = True

print(f'{x} ({type(x).__name__})')
print(f'{y} ({type(y).__name__})')
print(f'{name} ({type(name).__name__})')

"""
출력 결과:
10 (int)
3.14 (float)
Alice (str)

변수의 의미:
x = 10은 '상자 x에 숫자 10을 넣는다'는 뜻이다.
나중에 x를 사용하면 그 상자에서 10을 꺼낸다.


2. 타입 변환 (자료형 변환)
-------------------------------------------------
어떤 자료형을 다른 자료형으로 변환하는 것이다.

int(값)   → 정수로 변환
float(값) → 실수로 변환
str(값)   → 문자로 변환
"""

str_num = '10'
int_num = int(str_num)

print(f'변환 전: {str_num} ({type(str_num).__name__})')
print(f'변환 후: {int_num} ({type(int_num).__name__})')

int_val = 10
float_val = float(int_val)

print(f'{int_val} → {float_val}')

"""
출력 결과:
변환 전: 10 (str)
변환 후: 10 (int)
10 → 10.0

타입 변환이 필요한 이유:
사용자가 input()으로 숫자를 입력하면 문자열이다.
계산하려면 정수나 실수로 변환해야 한다.


3. 핵심 연산자
-------------------------------------------------

산술 연산자 (계산):
① +  : 덧셈
② -  : 뺄셈
③ *  : 곱셈
④ /  : 나눗셈 (결과는 항상 실수)
⑤ // : 정수 나눗셈 (나눈 몫만)
⑥ %  : 나머지
⑦ ** : 거듭제곱

비교 연산자 (비교):
① == : 같은가?
② != : 다른가?
③ >  : 초과 (크다)
④ <  : 미만 (작다)
⑤ >= : 이상 (크거나 같다)
⑥ <= : 이하 (작거나 같다)

논리 연산자 (논리):
① and : 그리고 (둘 다 참이면 참)
② or  : 또는 (하나라도 참이면 참)
③ not : 아니다 (참↔거짓)

할당 연산자 (저장):
① =  : 값 저장
② += : 더해서 저장
③ -= : 빼서 저장
④ *= : 곱해서 저장
⑤ /= : 나눠서 저장
"""

print('=== 산술 연산 ===')
print(f'10 + 3 = {10 + 3}')
print(f'10 - 3 = {10 - 3}')
print(f'10 * 3 = {10 * 3}')
print(f'10 / 3 = {10 / 3}')
print(f'10 // 3 = {10 // 3}')
print(f'10 % 3 = {10 % 3}')
print(f'2 ** 3 = {2 ** 3}')

"""
출력 결과:
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.333...
10 // 3 = 3
10 % 3 = 1
2 ** 3 = 8

산술의 의미:
10 ÷ 3 = 3 나머지 1
즉, 10 = 3 × 3 + 1
"""

print('\n=== 비교 연산 ===')
print(f'10 > 5: {10 > 5}')
print(f'10 == 10: {10 == 10}')
print(f'10 != 5: {10 != 5}')
print(f'10 < 5: {10 < 5}')

"""
출력 결과:
10 > 5: True
10 == 10: True
10 != 5: True
10 < 5: False

비교 연산자는 항상 True 또는 False를 반환한다.
조건문에서 많이 사용된다.
"""

print('\n=== 논리 연산 ===')
print(f'True and True: {True and True}')
print(f'True and False: {True and False}')
print(f'True or False: {True or False}')
print(f'False or False: {False or False}')
print(f'not True: {not True}')
print(f'not False: {not False}')

"""
출력 결과:
True and True: True
True and False: False
True or False: True
False or False: False
not True: False
not False: True
"""

print('\n=== 할당 연산 ===')
num = 10
print(f'처음: {num}')
num += 5
print(f'num += 5: {num}')
num -= 3
print(f'num -= 3: {num}')
num *= 2
print(f'num *= 2: {num}')

"""
출력 결과:
처음: 10
num += 5: 15
num -= 3: 12
num *= 2: 24

num += 5는 num = num + 5와 같다.
기존 값에 5를 더한 결과를 다시 num에 저장한다.


4. 입출력과 포맷팅
-------------------------------------------------
input(): 사용자 입력 받기 (반환값은 항상 문자열!)
print(): 화면에 출력하기

포맷팅:
:,   → 천 단위 쉼표
:.1f → 소수점 1자리
:.0f → 소수점 없이
"""

price = 50000
score = 95.5
rate = 0.25

print(f'가격: {price:,}원')
print(f'점수: {score:.1f}점')
print(f'할인율: {rate * 100:.0f}%')

"""
출력 결과:
가격: 50,000원
점수: 95.5점
할인율: 25%


=================================================
[2단계] 조건문
=================================================

1. if 문
-------------------------------------------------
조건이 참이면 실행한다.

형태:
if 조건:
    실행할 코드
"""

score = 85

if score >= 60:
    print('합격입니다')

"""
출력 결과:
합격입니다


2. if ~ else 문
-------------------------------------------------
참이면 A, 거짓이면 B를 실행한다.

형태:
if 조건:
    참일 때 실행
else:
    거짓일 때 실행
"""

score = 50

if score >= 60:
    print('합격')
else:
    print('불합격')

"""
출력 결과:
불합격


3. if ~ elif ~ else 문
-------------------------------------------------
여러 조건을 확인한다.

형태:
if 조건1:
    조건1이 참일 때
elif 조건2:
    조건2가 참일 때
else:
    모든 조건이 거짓일 때
"""

score = 85

if score >= 90:
    print('A학점')
elif score >= 80:
    print('B학점')
elif score >= 70:
    print('C학점')
else:
    print('F학점')

"""
출력 결과:
B학점

위에서부터 순서대로 확인하고, 첫 번째로 참인 조건만 실행된다.


4. 중첩 조건문
-------------------------------------------------
조건문 안에 또 다른 조건문을 넣을 수 있다.
"""

num = 7

if num > 0:
    if num % 2 == 0:
        print('양의 짝수')
    else:
        print('양의 홀수')
else:
    print('음수 또는 0')

"""
출력 결과:
양의 홀수


=================================================
[3단계] 루프 (반복)
=================================================

1. for 루프
-------------------------------------------------
정해진 횟수만큼 반복한다.

형태:
for 변수 in 범위:
    반복할 코드

range() 사용법:
range(끝)          → 0부터 끝-1까지
range(시작, 끝)    → 시작부터 끝-1까지
range(시작, 끝, 스텝) → 스텝만큼 증가
"""

print('=== 1부터 5까지 ===')
for i in range(1, 6):
    print(i)

"""
출력 결과:
1
2
3
4
5
"""

print('\n=== 1부터 10까지 2칸씩 ===')
for i in range(1, 11, 2):
    print(i)

"""
출력 결과:
1
3
5
7
9
"""

print('\n=== 리스트 순회 ===')
fruits = ['사과', '포도', '수박']

for fruit in fruits:
    print(f'과일: {fruit}')

"""
출력 결과:
과일: 사과
과일: 포도
과일: 수박
"""

print('\n=== 인덱스와 함께 ===')
for idx, fruit in enumerate(fruits):
    print(f'{idx}: {fruit}')

"""
출력 결과:
0: 사과
1: 포도
2: 수박

enumerate()는 인덱스와 값을 동시에 얻을 수 있다.
"""

print('\n=== 문자 순회 ===')
for char in 'hello':
    print(char)

"""
출력 결과:
h
e
l
l
o


2. while 루프
-------------------------------------------------
조건이 참인 동안 반복한다.

형태:
while 조건:
    반복할 코드
    조건을 거짓으로 만드는 코드 ← 중요!
"""

print('\n=== while 루프 ===')
count = 0
while count < 5:
    print(f'count: {count}')
    count += 1

"""
출력 결과:
count: 0
count: 1
count: 2
count: 3
count: 4

무한 루프 주의!
while True:
    print('무한 반복')
← 이렇게 쓰면 계속 반복된다.


3. 루프 제어
-------------------------------------------------
break    → 루프를 완전히 탈출
continue → 현재 반복만 건너뛰고 다음으로
pass     → 아무것도 하지 않음 (나중에 코드 추가할 때)
"""

print('\n=== break ===')
for i in range(1, 11):
    if i == 5:
        break
    print(i)

"""
출력 결과:
1
2
3
4
"""

print('\n=== continue ===')
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

"""
출력 결과:
1
2
4
5
"""

print('\n=== pass ===')
for i in range(3):
    pass

print('pass는 아무것도 하지 않음')

"""
출력 결과:
pass는 아무것도 하지 않음


=================================================
[4단계] 컨테이너 (자료구조)
=================================================

1. 리스트 (List)
-------------------------------------------------
여러 데이터를 순서대로 저장한다.
데이터를 추가/삭제/수정할 수 있다.

형태:
변수 = [데이터1, 데이터2, ...]

인덱스:
0부터 시작한다. (첫 번째 요소는 [0])
음수 인덱스는 뒤에서부터 센다. ([-1]은 마지막)
"""

fruits = ['사과', '포도', '수박']

print(f'리스트: {fruits}')
print(f'길이: {len(fruits)}')
print(f'첫 번째: {fruits[0]}')
print(f'두 번째: {fruits[1]}')
print(f'마지막: {fruits[-1]}')

"""
출력 결과:
리스트: ['사과', '포도', '수박']
길이: 3
첫 번째: 사과
두 번째: 포도
마지막: 수박

추가:
append(값)       → 맨 끝에 추가
insert(위치, 값) → 특정 위치에 삽입
"""

fruits.append('망고')
print(f'append 후: {fruits}')

fruits.insert(1, '딸기')
print(f'insert 후: {fruits}')

"""
출력 결과:
append 후: ['사과', '포도', '수박', '망고']
insert 후: ['사과', '딸기', '포도', '수박', '망고']

삭제:
pop()              → 마지막 삭제
remove(값)         → 값으로 찾아서 삭제
del 리스트[인덱스] → 인덱스로 삭제
"""

fruits.pop()
print(f'pop() 후: {fruits}')

fruits.remove('포도')
print(f'remove() 후: {fruits}')

del fruits[0]
print(f'del 후: {fruits}')

"""
출력 결과:
pop() 후: ['사과', '딸기', '포도', '수박']
remove() 후: ['사과', '딸기', '수박']
del 후: ['딸기', '수박']

정렬:
sort()              → 오름차순 정렬
sort(reverse=True)  → 내림차순 정렬
"""

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

numbers.sort()
print(f'오름차순: {numbers}')

numbers.sort(reverse=True)
print(f'내림차순: {numbers}')

"""
출력 결과:
오름차순: [1, 1, 2, 3, 4, 5, 6, 9]
내림차순: [9, 6, 5, 4, 3, 2, 1, 1]

reverse():
정렬하지 않고 순서만 반대로 뒤집는다.
"""

data = [1, 2, 3, 4, 5]
data.reverse()
print(f'역순: {data}')

"""
출력 결과:
역순: [5, 4, 3, 2, 1]

슬라이싱:
list[시작:끝]  → 시작부터 (끝-1)까지
시작 생략      → 처음부터
끝 생략        → 끝까지
::스텝         → 스텝만큼 건너뛰기

주의! 끝 인덱스는 포함되지 않는다.
"""

print('\n=== 슬라이싱 ===')
data = [0, 1, 2, 3, 4, 5]

print(f'data[1:4]: {data[1:4]}')
print(f'data[:3]: {data[:3]}')
print(f'data[3:]: {data[3:]}')
print(f'data[-2:]: {data[-2:]}')
print(f'data[::2]: {data[::2]}')
print(f'data[::-1]: {data[::-1]}')

"""
출력 결과:
data[1:4]: [1, 2, 3]
data[:3]: [0, 1, 2]
data[3:]: [3, 4, 5]
data[-2:]: [4, 5]
data[::2]: [0, 2, 4]
data[::-1]: [5, 4, 3, 2, 1, 0]

리스트 연결:
extend()  → 원본 리스트에 붙인다
+         → 새로운 리스트를 만든다
"""

print('\n=== 리스트 연결 ===')
list1 = [1, 2, 3]
list2 = [10, 20, 30]

list1.extend(list2)
print(f'extend 후: {list1}')

list3 = [1, 2] + [3, 4]
print(f'+ 연산자: {list3}')

"""
출력 결과:
extend 후: [1, 2, 3, 10, 20, 30]
+ 연산자: [1, 2, 3, 4]

split() 함수:
문자열을 특정 구분자로 나누어 리스트로 만든다.
"""

print('\n=== split() 함수 ===')

str_data = '박찬호 이승엽 박세리 박지성 이순철 선동열 손흥민 김연아'
splited_str = str_data.split(' ')

print(f'splited_str: {splited_str}')
print(f'splited_str type: {type(splited_str)}')

splited_str = tuple(splited_str)
print(f'splited_str: {splited_str}')
print(f'splited_str type: {type(splited_str)}')

"""
출력 결과:
splited_str: ['박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아']
splited_str type: <class 'list'>
splited_str: ('박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아')
splited_str type: <class 'tuple'>

split(' ')는 공백을 기준으로 문자열을 나누어 리스트로 반환한다.
리스트를 tuple()로 변환하면 튜플이 된다.


2. 튜플 (Tuple)
-------------------------------------------------
리스트와 비슷하지만 데이터 변동이 불가능하다.
한 번 만들면 요소를 추가/삭제/수정할 수 없다.

형태:
변수 = (데이터1, 데이터2, ...)

리스트 vs 튜플:
리스트 = []  → 수정 가능
튜플 = ()    → 수정 불가능
"""

fruits = ('사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나')

print(f'fruits: {fruits}')
print(f'fruits type: {type(fruits)}')

"""
출력 결과:
fruits: ('사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나')
fruits type: <class 'tuple'>

튜플 조회:
튜플은 아이템의 수정이 불가능하기 때문에
아이템의 삽입, 삭제, 정렬 등의 기능은 없고
조회하는 기능을 주로 사용한다.
"""

fruits = ('사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나')
print(f'{fruits[3]}')

"""
출력 결과:
참외

인덱스가 홀수인 아이템 조회하기:
"""

sports = ('태권도', '야구', '농구', '축구', '배구', '권투', '양궁')

for idx, item in enumerate(sports):
    if idx % 2 == 1:
        print(f'idx: {idx}, item: {item}')

"""
출력 결과:
idx: 1, item: 야구
idx: 3, item: 축구
idx: 5, item: 권투

index() 함수:
튜플 내 특정 아이템의 인덱스를 확인할 때 사용한다.
"""

fruits = ('사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나')
print(f'idx: {fruits.index("바나나")}')

"""
출력 결과:
idx: 7

in / not in 키워드:
튜플 안에 특정 아이템의 존재 유/무를 확인한다.
"""

colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
print(f'{"Green" in colors}')

if 'Green' in colors:
    print('colors 에는 Green이 있습니다')
else:
    print('colors 에는 Green이 없습니다')

if 'Green' not in colors:
    print('colors 에는 Green이 없습니다')
else:
    print('colors 에는 Green이 있습니다')

"""
출력 결과:
True
colors 에는 Green이 있습니다
colors 에는 Green이 있습니다

학점 경고 프로그램:
F 학점이 있으면 '경고'를 출력한다.
"""

scores = ('A', 'A+', 'B', 'B-', 'F')

if 'F' in scores:
    print('경고!')
else:
    print('경고 없음')

"""
출력 결과:
경고!

count() 함수:
특정 아이템의 개수를 센다.
"""

scores = ('A', 'A+', 'B', 'B-', 'F')
fCnt = scores.count('F')
print(f'F학점 개수: {fCnt}')

"""
출력 결과:
F학점 개수: 1

튜플 결합:
+ 연산자로 튜플을 결합한다.
"""

nums1 = (1, 2, 3)
nums2 = (10, 20, 30)

result = nums1 + nums2
print(f'result: {result}')

"""
출력 결과:
result: (1, 2, 3, 10, 20, 30)

얕은 복사 vs 깊은 복사:
얕은 복사 → 메모리 주소만 복사 (같은 데이터를 가리킴)
깊은 복사 → 실제 데이터까지 복사 (독립적인 데이터)
"""

import copy

a = [1, 2, 3, 4, 5]
b = a.copy()

b[0] = 100

print(f'a: {a}')
print(f'b: {b}')

"""
출력 결과:
a: [1, 2, 3, 4, 5]
b: [100, 2, 3, 4, 5]

튜플 슬라이싱:
리스트와 동일하게 슬라이싱할 수 있다.
"""

animals = ('호랑이', '사자', '곰', '여우', '늑대')

print(f'animals: {animals}')
print(f'animals[:3]: {animals[:3]}')
print(f'animals[1:4]: {animals[1:4]}')
print(f'animals[:-2]: {animals[:-2]}')
print(f'animals[-3:-1]: {animals[-3:-1]}')

"""
출력 결과:
animals: ('호랑이', '사자', '곰', '여우', '늑대')
animals[:3]: ('호랑이', '사자', '곰')
animals[1:4]: ('사자', '곰', '여우')
animals[:-2]: ('호랑이', '사자', '곰')
animals[-3:-1]: ('곰', '여우')

슬라이싱 연습:
"""

fruits = ('apple', 'banana', 'plum', 'watermelon', 'peach')

print(f'fruits[2:5]: {fruits[2:5]}')
print(f'fruits[:4]: {fruits[:4]}')
print(f'fruits[3:]: {fruits[3:]}')

"""
출력 결과:
fruits[2:5]: ('plum', 'watermelon', 'peach')
fruits[:4]: ('apple', 'banana', 'plum', 'watermelon')
fruits[3:]: ('watermelon', 'peach')

리스트와 튜플 간 변환 (형변환):
불가피하게 튜플의 아이템을 수정하려면 리스트로 변환해야 한다.
또한 리스트로 선언된 데이터를 수정이 안 되게 하려면 튜플로 변환해야 한다.
"""

colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

colors = list(colors)
print(f'colors type: {type(colors)}')

colors[1] = '오렌지'

colors = tuple(colors)
print(f'colors: {colors}')
print(f'colors type: {type(colors)}')

"""
출력 결과:
colors type: <class 'list'>
colors: ('Red', '오렌지', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
colors type: <class 'tuple'>

튜플 정렬:
튜플은 sort()가 없으므로 리스트로 변환하거나
sorted()를 사용한다.
"""

colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

colors = list(colors)
colors.sort()
colors = tuple(colors)

print(f'colors: {colors}')
print(f'colors type: {type(colors)}')

"""
출력 결과:
colors: ('Blue', 'Green', 'Indigo', 'Orange', 'Purple', 'Red', 'Yellow')
colors type: <class 'tuple'>

sorted() 함수 사용:
sorted()는 정렬된 리스트를 반환하므로 tuple()로 변환한다.
"""

colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
cs = tuple(sorted(colors))
print(f'cs: {cs}')

"""
출력 결과:
cs: ('Blue', 'Green', 'Indigo', 'Orange', 'Purple', 'Red', 'Yellow')


3. 딕셔너리 (Dictionary)
-------------------------------------------------
딕셔너리는 리스트와 함께 파이썬 프로그램에서 많이 사용하는 컨테이너 자료형이다.
리스트가 인덱스를 이용하여 아이템을 참조한다면,
딕셔너리는 인덱스 대신 키(key)를 이용하여 아이템을 참조(관리)한다.

형태:
변수 = {키1: 값1, 키2: 값2, ...}

딕셔너리는 {}로 정의한다.
키(key)는 절대 중복되면 안 된다.
값(value)은 중복되어도 상관없다.
"""

ages = {'박찬호': 48, '박지성': 40, '박세리': 50, '이승엽': 43, '박찌성': 50}

print(f'ages: {ages}')
print(f'ages type: {type(ages)}')

"""
출력 결과:
ages: {'박찬호': 48, '박지성': 40, '박세리': 50, '이승엽': 43, '박찌성': 50}
ages type: <class 'dict'>
"""

scores = {
    'c/c++': 'A',
    'java': 'B+',
    '네트워킹': 'C',
    '보안': 'A+',
    '해킹': 'F',
    '시스템': 'C+'
}

print(f'scores: {scores}')

"""
출력 결과:
scores: {'c/c++': 'A', 'java': 'B+', '네트워킹': 'C', '보안': 'A+', '해킹': 'F', '시스템': 'C+'}

딕셔너리 값 조회:
딕셔너리[키]로 값에 접근한다.
"""

print(f'박찬호 나이: {ages["박찬호"]}')
print(f'java 점수: {scores["java"]}')

"""
출력 결과:
박찬호 나이: 48
java 점수: B+

딕셔너리 추가/수정:
딕셔너리[키] = 값
→ 키가 없으면 추가, 있으면 수정
"""

ages['손흥민'] = 31
ages['박찬호'] = 49

print(f'ages: {ages}')

"""
출력 결과:
ages: {'박찬호': 49, '박지성': 40, '박세리': 50, '이승엽': 43, '박찌성': 50, '손흥민': 31}

딕셔너리 순회:
keys(), values(), items()를 사용한다.
"""

print('\n=== 딕셔너리 순회 ===')

for key in ages:
    print(f'{key}: {ages[key]}')

print()

for key, value in ages.items():
    print(f'{key}: {value}')

"""
출력 결과:
박찬호: 49
박지성: 40
박세리: 50
이승엽: 43
박찌성: 50
손흥민: 31


=================================================
[5단계] random 모듈
=================================================

난수(무작위 숫자)를 생성한다.
import 키워드로 모듈을 가져온다.

주요 함수:
randint(a, b)   → a 이상 b 이하 정수 (b 포함)
randrange(a, b) → a 이상 b 미만 정수 (b 제외)
choice(리스트)  → 리스트에서 무작위 선택
shuffle(리스트) → 리스트를 무작위로 섞는다
"""

import random

print('=== random 모듈 ===')

num1 = random.randint(1, 100)
num2 = random.randrange(1, 100)
choice = random.choice([1, 2, 3])

print(f'randint(1, 100): {num1}')
print(f'randrange(1, 100): {num2}')
print(f'choice([1, 2, 3]): {choice}')

"""
출력 결과 (실행할 때마다 다름):
randint(1, 100): 57
randrange(1, 100): 34
choice([1, 2, 3]): 2

shuffle() 함수:
리스트의 요소를 무작위로 섞는다.
"""

students = ['정우람', '박으뜸', '배힘찬', '천영웅', '신석기']

random.shuffle(students)
print(f'shuffle 후: {students}')

"""
출력 결과 (실행할 때마다 다름):
shuffle 후: ['배힘찬', '정우람', '신석기', '천영웅', '박으뜸']


=================================================
[핵심 패턴]
=================================================

1. 누적 계산
-------------------------------------------------
반복하면서 값을 계속 더하거나 곱한다.
"""

print('\n=== 누적 계산 ===')

total = 0
for i in range(1, 6):
    total += i
print(f'1+2+3+4+5 = {total}')

product = 1
for i in range(1, 6):
    product *= i
print(f'1×2×3×4×5 = {product}')

data = [5, 2, 8, 1, 9]
min_val = data[0]
max_val = data[0]

for num in data:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num

print(f'최소: {min_val}, 최대: {max_val}')

"""
출력 결과:
1+2+3+4+5 = 15
1×2×3×4×5 = 120
최소: 1, 최대: 9


2. 조건 검사
-------------------------------------------------
조건에 맞는 데이터만 처리한다.
"""

print('\n=== 조건 검사 ===')

print('1~5의 짝수/홀수:')
for num in range(1, 6):
    if num % 2 == 0:
        print(f'{num}: 짝수')
    else:
        print(f'{num}: 홀수')

score = 85
if 80 <= score < 90:
    print(f'점수 {score}은 B학점')

if 20 % 5 == 0:
    print('20은 5의 배수')

"""
출력 결과:
1: 홀수
2: 짝수
3: 홀수
4: 짝수
5: 홀수
점수 85은 B학점
20은 5의 배수


3. 리스트 필터링
-------------------------------------------------
조건에 맞는 요소만 새 리스트에 모은다.
"""

print('\n=== 리스트 필터링 ===')

numbers = [1, 2, 3, 4, 5, 6]
evens = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(f'모든 수: {numbers}')
print(f'짝수만: {evens}')

"""
출력 결과:
모든 수: [1, 2, 3, 4, 5, 6]
짝수만: [2, 4, 6]


4. 딕셔너리 활용
-------------------------------------------------
키-값 쌍으로 데이터를 관리한다.
"""

print('\n=== 딕셔너리 활용 ===')

scores = {
    '수학': 90,
    '영어': 85,
    '과학': 95
}

total = 0
for subject, score in scores.items():
    print(f'{subject}: {score}점')
    total += score

average = total / len(scores)
print(f'평균: {average}점')

"""
출력 결과:
수학: 90점
영어: 85점
과학: 95점
평균: 90.0점


=================================================
[실전 예제]
=================================================

예제 1: 출석부 관리 시스템
-------------------------------------------------
학급 학생 명단을 관리하는 프로그램이다.
리스트를 이용해서 학생들을 추가/삭제/정렬한다.

시나리오:
1. 학급 학생수가 10명인 리스트를 만든다.
2. '가나다' 순으로 정렬한다.
3. '박찬호' 학생이 전학을 간다. 출석부에서 삭제 후 전체 학생과 학생 수를 출력한다.
4. 선생님을 돕기 위한 학생으로 앞에서 3명을 뽑는다.
5. 새로운 친구 '이병규'가 전학 왔다.
6. 자리를 바꾸기 위해서 학생 순서를 역순으로 뒤집는다.
7. '정우람' 학생이 이름을 '정잘남'으로 개명했다.
"""

print('\n=== 출석부 관리 시스템 ===')

students = ['정우람', '박으뜸', '배힘찬', '천영웅', '신석기', '배민규', '전민수', '박건우', '박찬호', '이승엽']
print(f'1. 초기 명단: {students}')

students.sort()
print(f'2. 정렬 후: {students}')

students.remove('박찬호')
print(f'3. 박찬호 전학 후: {students}')
print(f'   학생 수: {len(students)}')

print(f'4. 앞에서 3명: {students[:3]}')

students.append('이병규')
print(f'5. 이병규 전학 후: {students}')

students.reverse()
print(f'6. 역순 정렬: {students}')

idx = students.index('정우람')
students[idx] = '정잘남'
print(f'7. 개명 후: {students}')

"""
출력 결과:
1. 초기 명단: ['정우람', '박으뜸', '배힘찬', '천영웅', '신석기', '배민규', '전민수', '박건우', '박찬호', '이승엽']
2. 정렬 후: ['박건우', '박으뜸', '박찬호', '배민규', '배힘찬', '신석기', '이승엽', '전민수', '천영웅', '정우람']
3. 박찬호 전학 후: ['박건우', '박으뜸', '배민규', '배힘찬', '신석기', '이승엽', '전민수', '천영웅', '정우람']
   학생 수: 9
4. 앞에서 3명: ['박건우', '박으뜸', '배민규']
5. 이병규 전학 후: ['박건우', '박으뜸', '배민규', '배힘찬', '신석기', '이승엽', '전민수', '천영웅', '정우람', '이병규']
6. 역순 정렬: ['이병규', '정우람', '천영웅', '전민수', '이승엽', '신석기', '배힘찬', '배민규', '박으뜸', '박건우']
7. 개명 후: ['이병규', '정잘남', '천영웅', '전민수', '이승엽', '신석기', '배힘찬', '배민규', '박으뜸', '박건우']


예제 2: 혈액 보관 시스템
-------------------------------------------------
헌혈 프로그램을 통해서 10명의 기부자에게 혈액을 받아 리스트에 보관하고,
보관하고 있는 혈액형을 종류별로 몇 팩씩 보유하고 있는지 보여주는 프로그램이다.
count() 함수를 활용한다.
"""

print('\n=== 혈액 보관 시스템 ===')

LOOP_COUNT = 10
bloods = []

for i in range(LOOP_COUNT):
    print(f'헌혈해 주셔서 감사합니다. 혈액형을 선택하세요. (A, B, AB, O)')
    bloods.append(input())

print(f'bloods: {bloods}')

print('-' * 30)
print(f'혈액형\t| 개수')
print('-' * 30)
print(f'A형\t: {bloods.count("A")}')
print(f'B형\t: {bloods.count("B")}')
print(f'AB형\t: {bloods.count("AB")}')
print(f'O형\t: {bloods.count("O")}')
print('-' * 30)

"""
출력 결과 (예시):
bloods: ['A', 'B', 'O', 'A', 'AB', 'O', 'B', 'A', 'O', 'AB']
------------------------------
혈액형	| 개수
------------------------------
A형	: 3
B형	: 2
AB형	: 2
O형	: 3
------------------------------


=================================================
[주의사항]
=================================================

1. 실수 오차
-------------------------------------------------
0.1 + 0.2를 계산하면 0.3이 아닌 0.30000000000000004가 나온다.
컴퓨터가 소수를 저장하는 방식 때문이다.
해결: round()로 반올림한다.
"""

result = 0.1 + 0.2
print(f'0.1 + 0.2 = {result}')
print(f'round(0.1 + 0.2, 1) = {round(result, 1)}')

"""
출력 결과:
0.1 + 0.2 = 0.30000000000000004
round(0.1 + 0.2, 1) = 0.3


2. input() 반환값
-------------------------------------------------
input()으로 받은 값은 항상 문자열이다!
숫자로 계산하려면 int() 또는 float()로 변환해야 한다.

예시:
user_input = input('숫자: ')
num = int(user_input)


3. 리스트 인덱스
-------------------------------------------------
인덱스는 0부터 시작한다.
마지막 인덱스 = len(리스트) - 1
"""

data = [1, 2, 3]
print(f'길이: {len(data)}')
print(f'마지막 인덱스: {len(data) - 1}')

"""
출력 결과:
길이: 3
마지막 인덱스: 2


4. 리스트 삭제 중 순회
-------------------------------------------------
리스트를 순회하면서 요소를 삭제하면 인덱스가 밀려 오류가 난다.
반드시 복사본(리스트[:])으로 순회한다.
"""

fruits = ['사과', '포도', '당근', '수박']
for fruit in fruits[:]:
    if fruit == '당근':
        fruits.remove(fruit)

print(f'야채 제거 후: {fruits}')

"""
출력 결과:
야채 제거 후: ['사과', '포도', '수박']


5. 슬라이싱 끝 인덱스는 제외
-------------------------------------------------
list[1:4]는 인덱스 1, 2, 3만 자른다. (4는 포함 안 됨)
"""

data = [0, 1, 2, 3, 4, 5]
print(f'data[1:4] = {data[1:4]}')

"""
출력 결과:
data[1:4] = [1, 2, 3]


6. 딕셔너리 키 오류
-------------------------------------------------
존재하지 않는 키로 접근하면 오류가 발생한다.
"""

student = {'name': 'Alice', 'age': 25}

print(f'이름: {student["name"]}')

"""
출력 결과:
이름: Alice

주의:
student['grade']  ← 'grade' 키가 없으면 오류 발생!


7. 튜플은 수정 불가능
-------------------------------------------------
튜플은 한 번 만들면 수정할 수 없다.
수정하려면 리스트로 변환한 후 다시 튜플로 변환해야 한다.
"""

colors = ('Red', 'Orange', 'Yellow')

colors = list(colors)
colors[1] = '오렌지'
colors = tuple(colors)

print(f'수정 후: {colors}')

"""
출력 결과:
수정 후: ('Red', '오렌지', 'Yellow')


8. 딕셔너리 키는 중복 불가
-------------------------------------------------
딕셔너리에서 키는 절대 중복되면 안 된다.
같은 키로 값을 다시 할당하면 기존 값이 덮어씌워진다.
"""

ages = {'박찬호': 48, '박찬호': 49}
print(f'ages: {ages}')

"""
출력 결과:
ages: {'박찬호': 49}
← 나중에 할당한 값으로 덮어씌워진다


=================================================
[학습 순서 요약]
=================================================

1단계: 변수, 자료형, 연산자, 입출력
2단계: 조건문
3단계: 루프
4단계: 리스트, 튜플, 딕셔너리
5단계: random 모듈
6단계: 핵심 패턴
7단계: 실전 예제

=================================================
[최종 체크리스트]
=================================================

✓ 변수와 자료형을 이해했는가?
✓ 모든 연산자를 사용할 수 있는가?
✓ 조건문을 자유자재로 쓸 수 있는가?
✓ for와 while을 구분해서 사용할 수 있는가?
✓ 리스트를 잘 다룰 수 있는가?
✓ split()으로 문자열을 리스트로 변환할 수 있는가?
✓ 튜플의 특성을 이해했는가?
✓ 튜플 조회 함수(index, count, in/not in)를 사용할 수 있는가?
✓ 튜플과 리스트를 변환할 수 있는가?
✓ 딕셔너리의 키-값 구조를 이해했는가?
✓ 딕셔너리를 순회할 수 있는가?
✓ 슬라이싱을 이해했는가?
✓ random 모듈(randint, randrange, choice, shuffle)을 사용할 수 있는가?
✓ count() 함수로 아이템 개수를 셀 수 있는가?
✓ 기본 패턴을 활용할 수 있는가?
✓ 실전 예제를 이해하고 응용할 수 있는가?

모두 체크되었다면 파이썬 기초는 충분히 이해한 것입니다!
"""

print('\n✓ 파이썬 기초 완전 학습 완료!')
