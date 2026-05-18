"""
비교 연산자(Comparison Operator) 완전 정리
=================================================

1. 비교 연산자란?
-------------------------------------------------
비교 연산자는 두 개의 값을 비교하여 참(True) 또는 거짓(False)을 반환하는 연산자이다.

형태:
값1 비교연산자 값2 → True 또는 False

비유:
비교 연산자는 저울과 같다.
두 값을 비교하여 어느 것이 더 큰지, 같은지를 판단한다.
"""

result1 = 10 == 10

print(f'10 == 10: {result1}')

result2 = 10 == 20

print(f'10 == 20: {result2}')

result3 = 10 > 5

print(f'10 > 5: {result3}')

"""
위 코드 결과:
10 == 10: True
10 == 20: False
10 > 5: True

비교 연산자의 결과는 항상 Boolean(True/False) 값이다.


2. 같음 비교 연산자(==)
-------------------------------------------------
두 값이 같은지 비교하는 연산자이다.

형태:
값1 == 값2

같으면 True, 다르면 False를 반환한다.
"""

num1 = 10
num2 = 20

result1 = num1 == num2

print(f'num1: {num1}')
print(f'num2: {num2}')
print(f'num1 == num2: {result1}')

"""
위 코드 결과:
num1: 10
num2: 20
num1 == num2: False
"""

num1 = 15
num2 = 15

result2 = num1 == num2

print(f'num1: {num1}')
print(f'num2: {num2}')
print(f'num1 == num2: {result2}')

"""
위 코드 결과:
num1: 15
num2: 15
num1 == num2: True


3. 같지 않음 비교 연산자(!=)
-------------------------------------------------
두 값이 다른지 비교하는 연산자이다.

형태:
값1 != 값2

다르면 True, 같으면 False를 반환한다.
"""

num1 = 10
num2 = 20

result = num1 != num2

print(f'num1: {num1}')
print(f'num2: {num2}')
print(f'num1 != num2: {result}')

"""
위 코드 결과:
num1: 10
num2: 20
num1 != num2: True
"""

num1 = 25
num2 = 25

result = num1 != num2

print(f'num1: {num1}')
print(f'num2: {num2}')
print(f'num1 != num2: {result}')

"""
위 코드 결과:
num1: 25
num2: 25
num1 != num2: False


4. 크다 비교 연산자(>)
-------------------------------------------------
앞의 값이 뒤의 값보다 큰지 비교하는 연산자이다.

형태:
값1 > 값2

값1이 크면 True, 그렇지 않으면 False를 반환한다.
"""

num1 = 10
num2 = 20

result = num1 > num2

print(f'num1: {num1}')
print(f'num2: {num2}')
print(f'num1 > num2: {result}')

"""
위 코드 결과:
num1: 10
num2: 20
num1 > num2: False
"""

num1 = 30
num2 = 20

result = num1 > num2

print(f'num1: {num1}')
print(f'num2: {num2}')
print(f'num1 > num2: {result}')

"""
위 코드 결과:
num1: 30
num2: 20
num1 > num2: True


5. 작다 비교 연산자(<)
-------------------------------------------------
앞의 값이 뒤의 값보다 작은지 비교하는 연산자이다.

형태:
값1 < 값2

값1이 작으면 True, 그렇지 않으면 False를 반환한다.
"""

num1 = 10
num2 = 20

result = num1 < num2

print(f'num1: {num1}')
print(f'num2: {num2}')
print(f'num1 < num2: {result}')

"""
위 코드 결과:
num1: 10
num2: 20
num1 < num2: True
"""

num1 = 30
num2 = 20

result = num1 < num2

print(f'num1: {num1}')
print(f'num2: {num2}')
print(f'num1 < num2: {result}')

"""
위 코드 결과:
num1: 30
num2: 20
num1 < num2: False


6. 크거나 같다 비교 연산자(>=)
-------------------------------------------------
앞의 값이 뒤의 값보다 크거나 같은지 비교하는 연산자이다.

형태:
값1 >= 값2

값1이 크거나 같으면 True, 그렇지 않으면 False를 반환한다.
"""

num1 = 10
num2 = 20

result1 = num1 >= num2

print(f'num1: {num1}')
print(f'num2: {num2}')
print(f'num1 >= num2: {result1}')

"""
위 코드 결과:
num1: 10
num2: 20
num1 >= num2: False
"""

num1 = 30
num2 = 20

result2 = num1 >= num2

print(f'num1: {num1}')
print(f'num2: {num2}')
print(f'num1 >= num2: {result2}')

"""
위 코드 결과:
num1: 30
num2: 20
num1 >= num2: True
"""

num1 = 20
num2 = 20

result3 = num1 >= num2

print(f'num1: {num1}')
print(f'num2: {num2}')
print(f'num1 >= num2: {result3}')

"""
위 코드 결과:
num1: 20
num2: 20
num1 >= num2: True

20 >= 20은 True이다. (같은 경우도 포함)


7. 작거나 같다 비교 연산자(<=)
-------------------------------------------------
앞의 값이 뒤의 값보다 작거나 같은지 비교하는 연산자이다.

형태:
값1 <= 값2

값1이 작거나 같으면 True, 그렇지 않으면 False를 반환한다.
"""

num1 = 10
num2 = 20

result1 = num1 <= num2

print(f'num1: {num1}')
print(f'num2: {num2}')
print(f'num1 <= num2: {result1}')

"""
위 코드 결과:
num1: 10
num2: 20
num1 <= num2: True
"""

num1 = 30
num2 = 20

result2 = num1 <= num2

print(f'num1: {num1}')
print(f'num2: {num2}')
print(f'num1 <= num2: {result2}')

"""
위 코드 결과:
num1: 30
num2: 20
num1 <= num2: False
"""

num1 = 20
num2 = 20

result3 = num1 <= num2

print(f'num1: {num1}')
print(f'num2: {num2}')
print(f'num1 <= num2: {result3}')

"""
위 코드 결과:
num1: 20
num2: 20
num1 <= num2: True

20 <= 20은 True이다. (같은 경우도 포함)


8. 모든 비교 연산자 한번에 보기
-------------------------------------------------
"""

num1 = 10
num2 = 20

print(f'num1 == num2: {num1 == num2}')
print(f'num1 != num2: {num1 != num2}')
print(f'num1 > num2: {num1 > num2}')
print(f'num1 < num2: {num1 < num2}')
print(f'num1 >= num2: {num1 >= num2}')
print(f'num1 <= num2: {num1 <= num2}')

"""
위 코드 결과:
num1 == num2: False
num1 != num2: True
num1 > num2: False
num1 < num2: True
num1 >= num2: False
num1 <= num2: True


9. QUIZ - 범퍼카 탑승 가능 판별 프로그램
-------------------------------------------------
DW 놀이동산에서 범퍼카는 신장이 120cm 이상인 어린이만 탑승할 수 있다.

조건:
신장 >= 120cm → 탑승 가능 (True)
신장 < 120cm → 탑승 불가능 (False)
"""

height = 135

result = height >= 120

print(f'어린이 신장: {height}cm')
print(f'탑승 가능 여부: {result}')

"""
위 코드 결과:
어린이 신장: 135cm
탑승 가능 여부: True
"""

height = 110

result = height >= 120

print(f'어린이 신장: {height}cm')
print(f'탑승 가능 여부: {result}')

"""
위 코드 결과:
어린이 신장: 110cm
탑승 가능 여부: False


10. 문자 비교 - ASCII 코드
-------------------------------------------------
문자도 비교 연산자로 비교할 수 있다.
문자는 ASCII(아스키) 코드 값으로 비교된다.

ASCII 코드란:
컴퓨터가 문자를 숫자로 표현하는 방식이다.
각 문자마다 고유한 숫자 값을 가진다.

예시:
'a' = 97
'b' = 98
'A' = 65
'B' = 66
'0' = 48
'9' = 57
"""

result1 = 'a' == 'b'

print(f"'a' == 'b': {result1}")

result2 = 'a' < 'b'

print(f"'a' < 'b': {result2}")

result3 = 'a' > 'b'

print(f"'a' > 'b': {result3}")

"""
위 코드 결과:
'a' == 'b': False
'a' < 'b': True
'a' > 'b': False

'a'는 97, 'b'는 98이므로:
'a' < 'b'는 True이다.


11. 문자 비교 - 대문자와 소문자
-------------------------------------------------
대문자와 소문자는 ASCII 코드가 다르다.

소문자: a=97, b=98, ..., z=122
대문자: A=65, B=66, ..., Z=90
"""

result1 = 'z' >= 'X'

print(f"'z' >= 'X': {result1}")

result2 = 'a' > 'Z'

print(f"'a' > 'Z': {result2}")

result3 = 'A' < 'a'

print(f"'A' < 'a': {result3}")

"""
위 코드 결과:
'z' >= 'X': True
'a' > 'Z': True
'A' < 'a': True

'z'는 122, 'X'는 88이므로 'z' >= 'X'는 True이다.
'a'는 97, 'Z'는 90이므로 'a' > 'Z'는 True이다.
'A'는 65, 'a'는 97이므로 'A' < 'a'는 True이다.


12. 문자열 비교
-------------------------------------------------
문자열도 비교 연산자로 비교할 수 있다.

문자열 비교는 사전식 순서(사전에서 먼저 나오는 것)로 비교된다.
"""

str1 = 'hello'
str2 = 'hello'

result1 = str1 == str2

print(f"str1 == str2: {result1}")

str1 = 'apple'
str2 = 'banana'

result2 = str1 < str2

print(f"'apple' < 'banana': {result2}")

str1 = 'zebra'
str2 = 'apple'

result3 = str1 > str2

print(f"'zebra' > 'apple': {result3}")

"""
위 코드 결과:
str1 == str2: True
'apple' < 'banana': True
'zebra' > 'apple': True

'hello'와 'hello'는 같으므로 True이다.
'apple'은 'banana'보다 사전에서 먼저 나오므로 True이다.
'zebra'는 'apple'보다 사전에서 나중에 나오므로 True이다.


13. 문자열 비교 - 첫 글자 기준
-------------------------------------------------
문자열 비교는 첫 글자부터 비교된다.
첫 글자가 같으면 두 번째 글자를 비교한다.
"""

str1 = 'abc'
str2 = 'abd'

result = str1 < str2

print(f"'abc' < 'abd': {result}")

"""
위 코드 결과:
'abc' < 'abd': True

'abc'와 'abd'의 첫 두 글자는 'ab'로 같다.
세 번째 글자에서 'c'(99) < 'd'(100)이므로 True이다.


14. 문자열 길이 비교
-------------------------------------------------
문자열의 길이도 비교할 수 있다.
"""

str1 = 'hello'
str2 = 'hi'

result = len(str1) > len(str2)

print(f"len('hello') > len('hi'): {result}")
print(f"len('hello'): {len(str1)}")
print(f"len('hi'): {len(str2)}")

"""
위 코드 결과:
len('hello') > len('hi'): True
len('hello'): 5
len('hi'): 2

'hello'의 길이는 5, 'hi'의 길이는 2이므로 True이다.


15. 실수 비교
-------------------------------------------------
실수도 비교할 수 있다.
"""

num1 = 3.14
num2 = 3.14

result1 = num1 == num2

print(f'3.14 == 3.14: {result1}')

num1 = 3.14
num2 = 3.15

result2 = num1 < num2

print(f'3.14 < 3.15: {result2}')

"""
위 코드 결과:
3.14 == 3.14: True
3.14 < 3.15: True


16. 비교 연산자의 우선순위
-------------------------------------------------
비교 연산자는 산술 연산자보다 낮은 우선순위를 가진다.

먼저 계산되는 순서:
1. 산술 연산 (+, -, *, /, %, //, **)
2. 비교 연산 (==, !=, <, >, <=, >=)
"""

result1 = 10 + 5 > 12

print(f'10 + 5 > 12: {result1}')

result2 = 20 / 2 == 10

print(f'20 / 2 == 10: {result2}')

"""
위 코드 결과:
10 + 5 > 12: True
20 / 2 == 10: True

10 + 5 > 12는 (10 + 5) > 12 = 15 > 12 = True이다.
20 / 2 == 10은 (20 / 2) == 10 = 10.0 == 10 = True이다.


17. 비교 연산자의 실무 활용
-------------------------------------------------
"""

# 점수 합격 판정
score = 75

is_passed = score >= 60

print(f'점수: {score}')
print(f'합격 여부: {is_passed}')

"""
위 코드 결과:
점수: 75
합격 여부: True
"""

# 나이 확인
age = 25

is_adult = age >= 18

print(f'나이: {age}')
print(f'성인 여부: {is_adult}')

"""
위 코드 결과:
나이: 25
성인 여부: True


=================================================
핵심 함수 및 연산자 총정리
=================================================

==              → 같은지 비교 (같으면 True)
!=              → 다른지 비교 (다르면 True)
>               → 크다 (왼쪽이 더 크면 True)
<               → 작다 (왼쪽이 더 작으면 True)
>=              → 크거나 같다 (왼쪽 >= 오른쪽이면 True)
<=              → 작거나 같다 (왼쪽 <= 오른쪽이면 True)

ASCII 코드 (일부):
'0'~'9' = 48~57
'A'~'Z' = 65~90
'a'~'z' = 97~122


=================================================
핵심 정리
=================================================

비교 연산자는:
"두 값을 비교하여 참(True) 또는 거짓(False)을 반환하는 연산자"

반드시 기억할 점:
1. 비교 연산자의 결과는 항상 Boolean(True/False)이다
2. 문자와 문자열은 ASCII 코드로 비교된다
3. 산술 연산이 비교 연산보다 먼저 실행된다
4. >= 와 <=는 같음도 포함한다
5. == 는 값이 같은지, = 는 값을 할당한다

실제 개발에서는:
- 로그인 검증 (입력값 == 저장값)
- 나이/신장 확인 (>= 조건 확인)
- 성적 판정 (범위 비교)
- 게임 승패 판정 (점수 비교)
- 입력값 유효성 검사
- 권한 확인
- 재고 여부 확인

등 거의 모든 프로그램의 조건문에서 사용된다.
"""
