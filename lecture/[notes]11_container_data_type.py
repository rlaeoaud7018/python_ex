"""
컨테이너 자료형(Container Data Type) - 리스트(List) 완전 정리
=================================================

1. 컨테이너 자료형이란?
-------------------------------------------------
컨테이너는 여러 개의 데이터를 하나로 묶어서 관리하는 자료형이다.

비유:
컨테이너는 상자와 같다.
여러 개의 물건을 하나의 상자에 담아 관리한다.

예시:
개별 변수 사용 (비효율적):
fruit1 = '사과'
fruit2 = '포도'
fruit3 = '복숭아'

컨테이너 사용 (효율적):
fruits = ['사과', '포도', '복숭아']
"""

# 개별 변수 사용
fruit1 = '사과'
fruit2 = '포도'
fruit3 = '복숭아'

print(f'fruit1: {fruit1}')
print(f'fruit2: {fruit2}')
print(f'fruit3: {fruit3}')

"""
위 코드 결과:
fruit1: 사과
fruit2: 포도
fruit3: 복숭아

변수가 많아질수록 관리가 어려워진다.
"""

# 컨테이너 사용
fruits = ['사과', '포도', '복숭아']

print(f'fruits: {fruits}')
print(f'type of fruits: {type(fruits)}')

"""
위 코드 결과:
fruits: ['사과', '포도', '복숭아']
type of fruits: <class 'list'>

훨씬 깔끔하고 관리하기 쉽다!


2. 파이썬의 주요 컨테이너 자료형
-------------------------------------------------

① 리스트(list)
   - 순서 있음
   - 수정 가능 (mutable)
   - 형태: [데이터1, 데이터2, ...]
   - 다양한 자료형 저장 가능

② 튜플(tuple)
   - 순서 있음
   - 수정 불가능 (immutable)
   - 형태: (데이터1, 데이터2, ...)
   - 변하지 않는 데이터에 사용

③ 딕셔너리(dictionary)
   - 순서 있음
   - 수정 가능
   - 형태: {키: 값, 키: 값, ...}
   - key-value 쌍으로 저장

④ 집합(set)
   - 순서 없음
   - 수정 가능
   - 형태: {데이터1, 데이터2, ...}
   - 중복 제거에 유용
"""

# 리스트
list_data = ['사과', '포도', '복숭아']
print(f'list_data: {list_data}')

# 튜플
tuple_data = ('사과', '포도', '복숭아')
print(f'tuple_data: {tuple_data}')

# 딕셔너리
dict_data = {'과일1': '사과', '과일2': '포도'}
print(f'dict_data: {dict_data}')

# 집합
set_data = {'사과', '포도', '복숭아'}
print(f'set_data: {set_data}')

"""
위 코드 결과:
list_data: ['사과', '포도', '복숭아']
tuple_data: ('사과', '포도', '복숭아')
dict_data: {'과일1': '사과', '과일2': '포도'}
set_data: {'포도', '복숭아', '사과'}


3. 리스트(List)
-------------------------------------------------
리스트는 순서가 있는 변경 가능한 컨테이너 자료형이다.

특징:
- 대괄호 [] 사용
- 데이터는 쉼표(,)로 구분
- 수정 가능 (추가, 수정, 삭제)
- 순서 존재
- 다양한 자료형 저장 가능
"""

fruits = ['사과', '포도', '복숭아']

print(f'fruits: {fruits}')
print(f'type of fruits: {type(fruits)}')

"""
위 코드 결과:
fruits: ['사과', '포도', '복숭아']
type of fruits: <class 'list'>


4. 리스트 인덱스(Index)
-------------------------------------------------
인덱스는 리스트의 각 데이터에 부여된 위치 번호이다.

중요한 특징:
- 파이썬은 0부터 시작한다
- 마지막 인덱스 = 리스트 길이 - 1

구조:
     0       1        2
['사과', '포도', '복숭아']
"""

fruits = ['사과', '포도', '복숭아']

print(f'fruits[0]: {fruits[0]}')
print(f'fruits[1]: {fruits[1]}')
print(f'fruits[2]: {fruits[2]}')

"""
위 코드 결과:
fruits[0]: 사과
fruits[1]: 포도
fruits[2]: 복숭아

인덱스 3에 접근하면 IndexError가 발생한다.
"""

# 음수 인덱스 (뒤에서부터)
fruits = ['사과', '포도', '복숭아']

print(f'fruits[-1]: {fruits[-1]}')  # 마지막 요소
print(f'fruits[-2]: {fruits[-2]}')  # 끝에서 두 번째
print(f'fruits[-3]: {fruits[-3]}')  # 끝에서 세 번째

"""
위 코드 결과:
fruits[-1]: 복숭아
fruits[-2]: 포도
fruits[-1]: 사과

음수 인덱스는 뒤에서부터 센다!


5. len() 함수 - 리스트의 길이
-------------------------------------------------
len() 함수는 리스트에 포함된 데이터의 개수(길이)를 반환한다.
"""

fruits = ['사과', '포도', '복숭아']

length = len(fruits)

print(f'fruits: {fruits}')
print(f'fruits length: {length}')
print(f'마지막 인덱스: {length - 1}')
print(f'마지막 데이터: {fruits[length - 1]}')

"""
위 코드 결과:
fruits: ['사과', '포도', '복숭아']
fruits length: 3
마지막 인덱스: 2
마지막 데이터: 복숭아

길이가 3이면 마지막 인덱스는 2이다.


6. 리스트 전체 조회 - for 루프
-------------------------------------------------
for 루프를 사용하여 리스트의 모든 요소를 순회할 수 있다.
"""

fruits = ['사과', '포도', '복숭아']

print(f'fruits: {fruits}')
print()

# 방법 1: 요소만 출력
for fruit in fruits:
    print(f'fruit: {fruit}')

"""
위 코드 결과:
fruits: ['사과', '포도', '복숭아']

fruit: 사과
fruit: 포도
fruit: 복숭아
"""

# 방법 2: 인덱스와 요소 동시 출력
fruits = ['사과', '포도', '복숭아']

for idx, fruit in enumerate(fruits):
    print(f'index: {idx}, fruit: {fruit}')

"""
위 코드 결과:
index: 0, fruit: 사과
index: 1, fruit: 포도
index: 2, fruit: 복숭아

enumerate()는 인덱스와 요소를 동시에 제공한다!
"""

# 방법 3: while 루프
fruits = ['사과', '포도', '복숭아']

i = 0

while i < len(fruits):
    print(f'fruits[{i}]: {fruits[i]}')
    i += 1

"""
위 코드 결과:
fruits[0]: 사과
fruits[1]: 포도
fruits[2]: 복숭아


7. 특정 데이터의 위치 찾기 - index()
-------------------------------------------------
index() 함수는 특정 데이터의 인덱스 위치를 반환한다.
"""

languages = ['c/c++', 'c#', 'python', 'java']

target_idx = languages.index('python')

print(f'languages: {languages}')
print(f'python의 인덱스: {target_idx}')

"""
위 코드 결과:
languages: ['c/c++', 'c#', 'python', 'java']
python의 인덱스: 2


8. 리스트에 데이터 추가 - append()
-------------------------------------------------
append() 함수는 리스트의 맨 끝에 데이터를 추가한다.
"""

fruits = ['사과', '포도', '복숭아']

print(f'추가 전: {fruits}')

fruits.append('수박')

print(f'추가 후: {fruits}')

"""
위 코드 결과:
추가 전: ['사과', '포도', '복숭아']
추가 후: ['사과', '포도', '복숭아', '수박']


9. 특정 위치에 데이터 삽입 - insert()
-------------------------------------------------
insert(위치, 데이터) 함수는 지정한 위치에 데이터를 삽입한다.
"""

fruits = ['사과', '포도', '복숭아']

print(f'삽입 전: {fruits}')

fruits.insert(1, '망고')

print(f'삽입 후: {fruits}')

"""
위 코드 결과:
삽입 전: ['사과', '포도', '복숭아']
삽입 후: ['사과', '망고', '포도', '복숭아']

인덱스 1의 위치에 '망고'가 삽입되었다.


10. 두 리스트 연결 - extend()
-------------------------------------------------
extend() 함수는 두 리스트를 연결한다.
"""

list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(f'연결 전: list1 = {list1}')
print(f'연결 전: list2 = {list2}')

list1.extend(list2)

print(f'연결 후: list1 = {list1}')
print(f'연결 후: list2 = {list2}')

"""
위 코드 결과:
연결 전: list1 = [1, 2, 3]
연결 전: list2 = [10, 20, 30]
연결 후: list1 = [1, 2, 3, 10, 20, 30]
연결 후: list2 = [10, 20, 30]

extend()는 list1을 변경한다. (in-place)


11. 두 리스트 연결 - + 연산자
-------------------------------------------------
+ 연산자로도 두 리스트를 연결할 수 있다.
"""

list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(f'list1: {list1}')
print(f'list2: {list2}')

list3 = list1 + list2

print(f'list3 = list1 + list2: {list3}')
print(f'list1: {list1}')  # list1은 변경되지 않음

"""
위 코드 결과:
list1: [1, 2, 3]
list2: [10, 20, 30]
list3 = list1 + list2: [1, 2, 3, 10, 20, 30]
list1: [1, 2, 3]

+ 연산자는 새로운 리스트를 반환한다.
원본 list1은 변경되지 않는다.


12. extend() vs + 연산자
-------------------------------------------------
extend()와 + 연산자의 차이점
"""

# extend() 방식
list1 = [1, 2, 3]
list2 = [10, 20, 30]

list1.extend(list2)

print(f'extend() 후 list1: {list1}')

# + 연산자 방식
list1 = [1, 2, 3]
list2 = [10, 20, 30]

list3 = list1 + list2

print(f'+ 연산자 후 list3: {list3}')
print(f'+ 연산자 후 list1: {list1}')

"""
extend(): 원본을 변경 (in-place)
+ 연산자: 새로운 리스트 반환 (원본 유지)


13. 리스트 데이터 삭제 - pop()
-------------------------------------------------
pop() 함수는 지정한 위치의 데이터를 삭제하고 반환한다.

특징:
- pop(): 마지막 데이터 삭제
- pop(인덱스): 특정 위치의 데이터 삭제
- 삭제된 데이터를 반환한다
"""

sports = ['football', 'baseball', 'volleyball', 'basketball']

print(f'삭제 전: {sports}')

# 마지막 데이터 삭제
deleted_item = sports.pop()

print(f'삭제된 데이터: {deleted_item}')
print(f'삭제 후: {sports}')

"""
위 코드 결과:
삭제 전: ['football', 'baseball', 'volleyball', 'basketball']
삭제된 데이터: basketball
삭제 후: ['football', 'baseball', 'volleyball']
"""

sports = ['football', 'baseball', 'volleyball', 'basketball']

print(f'삭제 전: {sports}')

# 인덱스 1의 데이터 삭제
deleted_item = sports.pop(1)

print(f'삭제된 데이터: {deleted_item}')
print(f'삭제 후: {sports}')

"""
위 코드 결과:
삭제 전: ['football', 'baseball', 'volleyball', 'basketball']
삭제된 데이터: baseball
삭제 후: ['football', 'volleyball', 'basketball']


14. 리스트 데이터 삭제 - del
-------------------------------------------------
del 키워드로도 리스트의 데이터를 삭제할 수 있다.

특징:
- del 리스트[인덱스]
- 삭제된 데이터를 반환하지 않는다
"""

sports = ['football', 'baseball', 'volleyball', 'basketball']

print(f'삭제 전: {sports}')

del sports[2]

print(f'삭제 후: {sports}')

"""
위 코드 결과:
삭제 전: ['football', 'baseball', 'volleyball', 'basketball']
삭제 후: ['football', 'baseball', 'basketball']


15. pop() vs del vs remove()
-------------------------------------------------
세 가지 삭제 방법의 차이점
"""

# pop(): 인덱스로 삭제, 삭제된 데이터 반환
nums = [1, 2, 3, 4, 5]
deleted = nums.pop(2)
print(f'pop(2): deleted={deleted}, list={nums}')

# del: 인덱스로 삭제, 데이터 반환 없음
nums = [1, 2, 3, 4, 5]
del nums[2]
print(f'del nums[2]: list={nums}')

# remove(): 값으로 삭제, 데이터 반환 없음
nums = [1, 2, 3, 4, 5]
nums.remove(3)
print(f'remove(3): list={nums}')

"""
위 코드 결과:
pop(2): deleted=3, list=[1, 2, 4, 5]
del nums[2]: list=[1, 2, 4, 5]
remove(3): list=[1, 2, 4, 5]

pop(): 인덱스 기반, 반환값 있음
del: 인덱스 기반, 반환값 없음
remove(): 값 기반, 반환값 없음


16. remove()로 특정 값 삭제
-------------------------------------------------
remove() 함수는 값으로 데이터를 삭제한다.
"""

languages = ['c/c++', 'c#', 'python', 'java']

print(f'삭제 전: {languages}')

languages.remove('python')

print(f'삭제 후: {languages}')

"""
위 코드 결과:
삭제 전: ['c/c++', 'c#', 'python', 'java']
삭제 후: ['c/c++', 'c#', 'java']


17. remove()의 주의사항 - 중복 데이터
-------------------------------------------------
remove() 함수는 처음 일치하는 데이터만 삭제한다.
"""

languages = ['c/c++', 'c#', 'python', 'java', 'python']

print(f'삭제 전: {languages}')

languages.remove('python')

print(f'삭제 후: {languages}')

"""
위 코드 결과:
삭제 전: ['c/c++', 'c#', 'python', 'java', 'python']
삭제 후: ['c/c++', 'c#', 'java', 'python']

처음 'python'만 삭제되었다!
두 번째 'python'은 남아있다.

모든 'python'을 삭제하려면 반복문을 사용해야 한다.
"""

languages = ['python', 'java', 'python', 'c++', 'python']

print(f'삭제 전: {languages}')

# 방법 1: while 루프
while 'python' in languages:
    languages.remove('python')

print(f'삭제 후: {languages}')

"""
위 코드 결과:
삭제 전: ['python', 'java', 'python', 'c++', 'python']
삭제 후: ['java', 'c++']

모든 'python'이 삭제되었다!


18. QUIZ - 과일 리스트에서 야채 삭제
-------------------------------------------------
과일 리스트에서 야채(당근, 토마토)를 찾아 삭제하는 프로그램
"""

fruits = ['사과', '망고', '당근', '수박', '포도', '참외', '토마토']

print(f'삭제 전: {fruits}')

for item in fruits[:]:  # 복사본으로 순회 (삭제 중 오류 방지)
    if item == '당근' or item == '토마토':
        fruits.remove(item)

print(f'삭제 후: {fruits}')

"""
위 코드 결과:
삭제 전: ['사과', '망고', '당근', '수박', '포도', '참외', '토마토']
삭제 후: ['사과', '망고', '수박', '포도', '참외']

주의: 리스트를 순회하면서 삭제할 때는
      fruits[:] 복사본으로 순회해야 오류가 발생하지 않는다!


19. 리스트 정렬 - sort()
-------------------------------------------------
sort() 함수는 리스트의 데이터를 정렬한다.

형태:
리스트.sort()           # 오름차순 (기본값)
리스트.sort(reverse=True)  # 내림차순
"""

numbers = [5, 1, 2, 3, 4, 2, 6]

print(f'정렬 전: {numbers}')

# 오름차순 (ASC)
numbers.sort()

print(f'오름차순: {numbers}')

# 내림차순 (DESC)
numbers.sort(reverse=True)

print(f'내림차순: {numbers}')

"""
위 코드 결과:
정렬 전: [5, 1, 2, 3, 4, 2, 6]
오름차순: [1, 2, 2, 3, 4, 5, 6]
내림차순: [6, 5, 4, 3, 2, 2, 1]


20. 문자열 정렬
-------------------------------------------------
"""

korean = ['다', '가', '마', '하', '카']

print(f'정렬 전: {korean}')

korean.sort()

print(f'오름차순: {korean}')

korean.sort(reverse=True)

print(f'내림차순: {korean}')

"""
위 코드 결과:
정렬 전: ['다', '가', '마', '하', '카']
오름차순: ['가', '다', '마', '하', '카']
내림차순: ['카', '하', '마', '다', '가']


21. QUIZ - 회의 참석자 정렬
-------------------------------------------------
참석자 명단을 오름차순과 내림차순으로 정렬하는 프로그램
"""

names = ['홍길동', '김길동', '이길동', '박길동', '정길동']

print(f'정렬 전: {names}')

names.sort()

print(f'오름차순: {names}')

names.sort(reverse=True)

print(f'내림차순: {names}')

"""
위 코드 결과:
정렬 전: ['홍길동', '김길동', '이길동', '박길동', '정길동']
오름차순: ['김길동', '박길동', '이길동', '정길동', '홍길동']
내림차순: ['홍길동', '정길동', '이길동', '박길동', '김길동']


22. 리스트 순서 뒤집기 - reverse()
-------------------------------------------------
reverse() 함수는 리스트의 데이터 순서를 반대로 뒤집는다.

주의:
- reverse(): 정렬하지 않고 순서만 반대로
- sort(reverse=True): 내림차순으로 정렬
"""

vegetables = ['당근', '오이', '양파', '감자', '고구마']

print(f'뒤집기 전: {vegetables}')

vegetables.reverse()

print(f'뒤집기 후: {vegetables}')

"""
위 코드 결과:
뒤집기 전: ['당근', '오이', '양파', '감자', '고구마']
뒤집기 후: ['고구마', '감자', '양파', '오이', '당근']


23. 리스트 슬라이싱(List Slicing) - 기초
-------------------------------------------------
슬라이싱은 리스트에서 필요한 부분만 추출하는 기법이다.

형태:
리스트[시작:끝]
→ 시작 인덱스부터 (끝-1) 인덱스까지 추출

특징:
- 끝 인덱스는 포함되지 않는다
- 원본 리스트는 변경되지 않는다
"""

animals = ['호랑이', '사자', '곰', '여우', '늑대']

print(f'animals: {animals}')
print()

# [1:4] 슬라이싱
result = animals[1:4]

print(f'animals[1:4]: {result}')

"""
위 코드 결과:
animals: ['호랑이', '사자', '곰', '여우', '늑대']

animals[1:4]: ['사자', '곰', '여우']

인덱스 1부터 3까지 (4는 포함 안 됨)가 추출되었다.


24. 리스트 슬라이싱 - 시작/끝 생략
-------------------------------------------------
시작이나 끝을 생략하면 자동으로 처음 또는 끝까지 된다.
"""

animals = ['호랑이', '사자', '곰', '여우', '늑대']

# 처음부터 인덱스 2까지
result1 = animals[:3]

print(f'animals[:3]: {result1}')

# 인덱스 2부터 끝까지
result2 = animals[2:]

print(f'animals[2:]: {result2}')

# 처음부터 끝까지
result3 = animals[:]

print(f'animals[:]: {result3}')

"""
위 코드 결과:
animals[:3]: ['호랑이', '사자', '곰']
animals[2:]: ['곰', '여우', '늑대']
animals[:]: ['호랑이', '사자', '곰', '여우', '늑대']


25. 리스트 슬라이싱 - 음수 인덱스
-------------------------------------------------
음수 인덱스를 사용하면 뒤에서부터 추출할 수 있다.
"""

animals = ['호랑이', '사자', '곰', '여우', '늑대']

# 마지막 요소 제외
result1 = animals[:-1]

print(f'animals[:-1]: {result1}')

# 두 번째부터 끝에서 두 번째까지
result2 = animals[1:-1]

print(f'animals[1:-1]: {result2}')

# 뒤에서 2개
result3 = animals[-2:]

print(f'animals[-2:]: {result3}')

# 뒤에서 3개
result4 = animals[-3:]

print(f'animals[-3:]: {result4}')

"""
위 코드 결과:
animals[:-1]: ['호랑이', '사자', '곰', '여우']
animals[1:-1]: ['사자', '곰', '여우']
animals[-2:]: ['여우', '늑대']
animals[-3:]: ['곰', '여우', '늑대']


26. 리스트 슬라이싱 - 스텝(간격)
-------------------------------------------------
세 번째 파라미터로 스텝(간격)을 지정할 수 있다.

형태:
리스트[시작:끝:스텝]
"""

animals = ['호랑이', '사자', '곰', '여우', '늑대']

# 2칸씩 건너뛰기
result1 = animals[::2]

print(f'animals[::2]: {result1}')

# 인덱스 1부터 끝까지 2칸씩
result2 = animals[1::2]

print(f'animals[1::2]: {result2}')

# 역순 (스텝 -1)
result3 = animals[::-1]

print(f'animals[::-1]: {result3}')

"""
위 코드 결과:
animals[::2]: ['호랑이', '곰', '늑대']
animals[1::2]: ['사자', '여우']
animals[::-1]: ['늑대', '여우', '곰', '사자', '호랑이']


27. QUIZ - 알파벳 리스트 슬라이싱
-------------------------------------------------
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(f'alphabet: {alphabet}')
print()

# 1. 역순으로 입력하기
alphabet.reverse()
print(f'1. 역순: {alphabet}')
print()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# 2-1. 인덱스 2부터 5까지
result1 = alphabet[2:6]
print(f'2-1. alphabet[2:6]: {result1}')

# 2-2. 인덱스 0부터 4까지
result2 = alphabet[:5]
print(f'2-2. alphabet[:5]: {result2}')

# 2-3. 인덱스 3부터 7까지
result3 = alphabet[3:8]
print(f'2-3. alphabet[3:8]: {result3}')

# 2-4. 인덱스 5부터 끝까지
result4 = alphabet[5:]
print(f'2-4. alphabet[5:]: {result4}')

# 2-5. 뒤에서 4개
result5 = alphabet[-4:]
print(f'2-5. alphabet[-4:]: {result5}')

"""
위 코드 결과:
alphabet: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

1. 역순: ['j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

2-1. alphabet[2:6]: ['c', 'd', 'e', 'f']
2-2. alphabet[:5]: ['a', 'b', 'c', 'd', 'e']
2-3. alphabet[3:8]: ['d', 'e', 'f', 'g', 'h']
2-4. alphabet[5:]: ['f', 'g', 'h', 'i', 'j']
2-5. alphabet[-4:]: ['g', 'h', 'i', 'j']


=================================================
핵심 함수 및 메서드 총정리
=================================================

리스트 생성:
리스트 = [데이터1, 데이터2, ...]

리스트 접근:
리스트[인덱스]
리스트[-인덱스]  # 뒤에서부터

리스트 길이:
len(리스트)

리스트 순회:
for 변수 in 리스트:
for 인덱스, 변수 in enumerate(리스트):

리스트 조회:
리스트.index(값)      # 값의 위치 반환

리스트 추가:
리스트.append(값)     # 끝에 추가
리스트.insert(위치, 값)  # 특정 위치에 삽입

리스트 연결:
리스트1.extend(리스트2)
리스트3 = 리스트1 + 리스트2

리스트 삭제:
리스트.pop()          # 마지막 삭제, 반환
리스트.pop(인덱스)    # 특정 위치 삭제, 반환
del 리스트[인덱스]    # 특정 위치 삭제
리스트.remove(값)     # 값으로 삭제 (첫 번째만)

리스트 정렬:
리스트.sort()         # 오름차순
리스트.sort(reverse=True)  # 내림차순
sorted(리스트)        # 새 리스트 반환

리스트 역순:
리스트.reverse()      # 순서 뒤집기
리스트[::-1]          # 역순 슬라이싱

리스트 슬라이싱:
리스트[시작:끝]       # 시작부터 (끝-1)까지
리스트[:끝]           # 처음부터 (끝-1)까지
리스트[시작:]         # 시작부터 끝까지
리스트[::스텝]        # 스텝만큼 건너뛰기
리스트[::-1]          # 역순


=================================================
핵심 정리
=================================================

리스트는:
"순서가 있는 변경 가능한 컨테이너 자료형"

반드시 기억할 점:
1. 인덱스는 0부터 시작한다
2. 마지막 인덱스 = 길이 - 1
3. 음수 인덱스는 뒤에서부터 센다
4. 슬라이싱은 끝 인덱스를 포함하지 않는다
5. 리스트를 순회하면서 삭제할 때는 복사본을 사용한다
6. extend()와 +는 다르다 (원본 변경 vs 새 리스트)
7. remove()는 첫 번째 요소만 삭제한다

실제 개발에서는:
- 데이터 모음 관리
- 순서가 있는 데이터 저장
- 동적 데이터 추가/삭제
- 데이터 정렬
- 반복문에서 순회
- 게임 아이템 목록
- 채팅 메시지 히스토리

등 거의 모든 프로그램에서 가장 자주 사용되는 자료형이다.
"""
