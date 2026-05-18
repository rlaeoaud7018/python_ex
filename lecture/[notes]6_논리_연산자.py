"""
논리 연산자(Logical Operator) 완전 정리
=================================================

1. 논리 연산자란?
-------------------------------------------------
논리 연산자는 Boolean 값(True, False)을 이용하여
논리 연산을 수행하는 연산자이다.

종류:
① and → '그리고' (모두 True이면 True)
② or  → '또는' (하나라도 True이면 True)
③ not → '아니오' (True를 False로, False를 True로)

비유:
논리 연산자는 신호등과 같다.
and는 모든 신호가 초록색일 때만 진행
or는 하나의 신호만 초록색이어도 진행
not는 신호의 반대를 나타낸다
"""

result1 = True and True

print(f'True and True = {result1}')

result2 = True or False

print(f'True or False = {result2}')

result3 = not True

print(f'not True = {result3}')

"""
위 코드 결과:
True and True = True
True or False = True
not True = False


2. and 연산자 (그리고)
-------------------------------------------------
and는 '그리고'의 의미로,
피연산자가 모두 True일 때만 결과가 True가 된다.

Truth Table (진리표):
True and True   = True
True and False  = False
False and True  = False
False and False = False
"""

var1 = True
var2 = True

result = var1 and var2

print(f'var1: {var1}')
print(f'var2: {var2}')
print(f'var1 and var2: {result}')

"""
위 코드 결과:
var1: True
var2: True
var1 and var2: True
"""

var1 = True
var2 = False

result = var1 and var2

print(f'var1: {var1}')
print(f'var2: {var2}')
print(f'var1 and var2: {result}')

"""
위 코드 결과:
var1: True
var2: False
var1 and var2: False
"""

var1 = False
var2 = False

result = var1 and var2

print(f'var1: {var1}')
print(f'var2: {var2}')
print(f'var1 and var2: {result}')

"""
위 코드 결과:
var1: False
var2: False
var1 and var2: False

and 연산자는 한 개라도 False이면 False가 된다.


3. and 연산자와 비교 연산자 조합
-------------------------------------------------
and 연산자는 비교 연산자와 함께 사용되는 경우가 많다.
"""

num1 = 10
num2 = 20
num3 = 30

result1 = (num1 < num3) and (num2 < num3)

print(f'num1: {num1}, num2: {num2}, num3: {num3}')
print(f'(num1 < num3) and (num2 < num3): {result1}')

"""
위 코드 결과:
num1: 10, num2: 20, num3: 30
(num1 < num3) and (num2 < num3): True

(10 < 30) and (20 < 30) = True and True = True
"""

num1 = 10
num2 = 20
num3 = 30

result2 = (num1 > num3) and (num2 < num3)

print(f'num1: {num1}, num2: {num2}, num3: {num3}')
print(f'(num1 > num3) and (num2 < num3): {result2}')

"""
위 코드 결과:
num1: 10, num2: 20, num3: 30
(num1 > num3) and (num2 < num3): False

(10 > 30) and (20 < 30) = False and True = False
"""

num1 = 10
num2 = 20
num3 = 30

result3 = (num1 < num2) and (num2 < num3) and (num3 > num1)

print(f'num1: {num1}, num2: {num2}, num3: {num3}')
print(f'(num1 < num2) and (num2 < num3) and (num3 > num1): {result3}')

"""
위 코드 결과:
num1: 10, num2: 20, num3: 30
(num1 < num2) and (num2 < num3) and (num3 > num1): True

(10 < 20) and (20 < 30) and (30 > 10) = True and True and True = True


4. and 연산자의 단락 평가(Short Circuit)
-------------------------------------------------
and 연산자는 왼쪽에서 오른쪽으로 평가된다.
만약 첫 번째 조건이 False이면,
나머지 조건은 평가하지 않고 바로 False를 반환한다.

이를 단락 평가(Short Circuit Evaluation)라고 한다.
"""

num1 = 17
num2 = 20

# 첫 번째 조건이 False이므로 두 번째 조건은 평가하지 않음
result = (num1 < 15) and (num2 > 15)

print(f'num1: {num1}')
print(f'num2: {num2}')
print(f'(num1 < 15) and (num2 > 15): {result}')

"""
위 코드 결과:
num1: 17
num2: 20
(num1 < 15) and (num2 > 15): False

(17 < 15) = False이므로 (num2 > 15)는 평가하지 않음
결과: False


5. or 연산자 (또는)
-------------------------------------------------
or은 '또는'의 의미로,
피연산자 중 하나라도 True이면 결과가 True가 된다.

Truth Table (진리표):
True or True   = True
True or False  = True
False or True  = True
False or False = False
"""

var1 = True
var2 = True

result = var1 or var2

print(f'var1: {var1}')
print(f'var2: {var2}')
print(f'var1 or var2: {result}')

"""
위 코드 결과:
var1: True
var2: True
var1 or var2: True
"""

var1 = True
var2 = False

result = var1 or var2

print(f'var1: {var1}')
print(f'var2: {var2}')
print(f'var1 or var2: {result}')

"""
위 코드 결과:
var1: True
var2: False
var1 or var2: True
"""

var1 = False
var2 = False

result = var1 or var2

print(f'var1: {var1}')
print(f'var2: {var2}')
print(f'var1 or var2: {result}')

"""
위 코드 결과:
var1: False
var2: False
var1 or var2: False

or 연산자는 하나라도 True이면 True가 된다.


6. or 연산자와 비교 연산자 조합
-------------------------------------------------
or 연산자도 비교 연산자와 함께 사용된다.
"""

num1 = 10
num2 = 5

result1 = (num1 > 15) or (num2 > 3)

print(f'num1: {num1}, num2: {num2}')
print(f'(num1 > 15) or (num2 > 3): {result1}')

"""
위 코드 결과:
num1: 10, num2: 5
(num1 > 15) or (num2 > 3): True

(10 > 15) or (5 > 3) = False or True = True
"""

num1 = 10
num2 = 5

result2 = (num1 > 15) or (num2 > 10)

print(f'num1: {num1}, num2: {num2}')
print(f'(num1 > 15) or (num2 > 10): {result2}')

"""
위 코드 결과:
num1: 10, num2: 5
(num1 > 15) or (num2 > 10): False

(10 > 15) or (5 > 10) = False or False = False


7. or 연산자의 단락 평가(Short Circuit)
-------------------------------------------------
or 연산자는 왼쪽에서 오른쪽으로 평가된다.
만약 첫 번째 조건이 True이면,
나머지 조건은 평가하지 않고 바로 True를 반환한다.
"""

num1 = 10

result = (num1 > 5) or (num1 < 0)

print(f'num1: {num1}')
print(f'(num1 > 5) or (num1 < 0): {result}')

"""
위 코드 결과:
num1: 10
(num1 > 5) or (num1 < 0): True

(10 > 5) = True이므로 (num1 < 0)은 평가하지 않음
결과: True


8. QUIZ - 어린이용 범퍼카 탑승 가능 판별 프로그램
-------------------------------------------------
탑승 기준: 신장이 120cm 이상이고 170cm 미만

조건:
height >= 120 AND height < 170 → 탑승 가능 (True)
그 외 → 탑승 불가능 (False)
"""

height = 150

result = (height >= 120) and (height < 170)

print(f'어린이 신장: {height}cm')
print(f'탑승 가능 여부: {result}')

"""
위 코드 결과:
어린이 신장: 150cm
탑승 가능 여부: True

(150 >= 120) and (150 < 170) = True and True = True
"""

height = 110

result = (height >= 120) and (height < 170)

print(f'어린이 신장: {height}cm')
print(f'탑승 가능 여부: {result}')

"""
위 코드 결과:
어린이 신장: 110cm
탑승 가능 여부: False

(110 >= 120) and (110 < 170) = False and True = False
"""

height = 180

result = (height >= 120) and (height < 170)

print(f'어린이 신장: {height}cm')
print(f'탑승 가능 여부: {result}')

"""
위 코드 결과:
어린이 신장: 180cm
탑승 가능 여부: False

(180 >= 120) and (180 < 170) = True and False = False


9. not 연산자 (아니오)
-------------------------------------------------
not은 '아니오'의 의미로,
피연산자의 상태를 부정(반대)하는 연산자이다.

Truth Table (진리표):
not True  = False
not False = True
"""

var1 = True

result1 = not var1

print(f'var1: {var1}')
print(f'not var1: {result1}')

"""
위 코드 결과:
var1: True
not var1: False
"""

var1 = False

result2 = not var1

print(f'var1: {var1}')
print(f'not var1: {result2}')

"""
위 코드 결과:
var1: False
not var1: True


10. not 연산자와 비교 연산자 조합
-------------------------------------------------
not 연산자는 비교 연산자의 결과를 부정할 수 있다.
"""

num = 15

result1 = num > 10

print(f'num: {num}')
print(f'num > 10: {result1}')
print(f'not (num > 10): {not result1}')

"""
위 코드 결과:
num: 15
num > 10: True
not (num > 10): False
"""

num = 5

result2 = num > 10

print(f'num: {num}')
print(f'num > 10: {result2}')
print(f'not (num > 10): {not result2}')

"""
위 코드 결과:
num: 5
num > 10: False
not (num > 10): True


11. and, or, not 조합
-------------------------------------------------
여러 논리 연산자를 조합하여 복잡한 조건을 만들 수 있다.
"""

num1 = 10
num2 = 20
num3 = 30

result = (num1 < num2) and (num2 < num3) and not (num1 == num3)

print(f'num1: {num1}, num2: {num2}, num3: {num3}')
print(f'(num1 < num2) and (num2 < num3) and not (num1 == num3): {result}')

"""
위 코드 결과:
num1: 10, num2: 20, num3: 30
(num1 < num2) and (num2 < num3) and not (num1 == num3): True

(10 < 20) and (20 < 30) and not (10 == 30)
= True and True and not False
= True and True and True
= True


12. 삼항 연산자 (조건식)
-------------------------------------------------
삼항 연산자는 if~else 구문을 한 줄로 표현하는 방식이다.

형태:
값1 if 조건식 else 값2

조건식이 True이면 값1, False이면 값2를 반환한다.
"""

myScore = 95
targetScore = 90

result = '합격' if myScore >= targetScore else '불합격'

print(f'myScore: {myScore}')
print(f'targetScore: {targetScore}')
print(f'result: {result}')

"""
위 코드 결과:
myScore: 95
targetScore: 90
result: 합격

myScore >= targetScore이 True이므로 '합격'이 반환된다.
"""

myScore = 75
targetScore = 90

result = '합격' if myScore >= targetScore else '불합격'

print(f'myScore: {myScore}')
print(f'targetScore: {targetScore}')
print(f'result: {result}')

"""
위 코드 결과:
myScore: 75
targetScore: 90
result: 불합격

myScore >= targetScore이 False이므로 '불합격'이 반환된다.


13. QUIZ - 적자/흑자 판단 프로그램
-------------------------------------------------
수입과 지출을 입력하면 흑자인지 적자인지 판별하는 프로그램

조건:
수입 > 지출 → 흑자
수입 <= 지출 → 적자
"""

incoming = 5000000
outgoing = 3000000

result = '흑자' if incoming > outgoing else '적자'

print(f'수입: {incoming:,}원')
print(f'지출: {outgoing:,}원')
print(f'판단 결과: {result}')

"""
위 코드 결과:
수입: 5,000,000원
지출: 3,000,000원
판단 결과: 흑자

incoming > outgoing이 True이므로 '흑자'가 반환된다.
"""

incoming = 2000000
outgoing = 3000000

result = '흑자' if incoming > outgoing else '적자'

print(f'수입: {incoming:,}원')
print(f'지출: {outgoing:,}원')
print(f'판단 결과: {result}')

"""
위 코드 결과:
수입: 2,000,000원
지출: 3,000,000원
판단 결과: 적자

incoming > outgoing이 False이므로 '적자'가 반환된다.


14. QUIZ - 조명 장치 ON/OFF 프로그램
-------------------------------------------------
현재 조도와 목표 조도를 비교하여
조명을 켤지 끌지 결정하는 프로그램

조건:
현재 조도 < 목표 조도 → Turn on (조명 켜기)
현재 조도 >= 목표 조도 → Turn off (조명 끄기)
"""

currentLight = 50
targetLight = 60

result = 'Turn on' if currentLight < targetLight else 'Turn off'

print(f'현재 조도: {currentLight}')
print(f'목표 조도: {targetLight}')
print(f'명령: {result}')

"""
위 코드 결과:
현재 조도: 50
목표 조도: 60
명령: Turn on

currentLight < targetLight이 True이므로 'Turn on'이 반환된다.
"""

currentLight = 75
targetLight = 60

result = 'Turn on' if currentLight < targetLight else 'Turn off'

print(f'현재 조도: {currentLight}')
print(f'목표 조도: {targetLight}')
print(f'명령: {result}')

"""
위 코드 결과:
현재 조도: 75
목표 조도: 60
명령: Turn off

currentLight < targetLight이 False이므로 'Turn off'가 반환된다.


15. 논리 연산자 우선순위
-------------------------------------------------
여러 논리 연산자가 함께 사용될 때 평가 순서:

높음: not
중간: and
낮음: or

예: A or B and C not D
→ (A or (B and (not D))) or C로 평가된다
"""

num1 = 10
num2 = 20

result1 = True or False and False

print(f'True or False and False: {result1}')

result2 = False or True and True

print(f'False or True and True: {result2}')

"""
위 코드 결과:
True or False and False: True
False or True and True: True

True or (False and False) = True or False = True
False or (True and True) = False or True = True


=================================================
핵심 함수 및 연산자 총정리
=================================================

and             → '그리고' (모두 True이면 True)
or              → '또는' (하나라도 True이면 True)
not             → '아니오' (True를 False로, False를 True로)

삼항 연산자:
값1 if 조건식 else 값2

논리 연산자 우선순위 (높음 → 낮음):
1. not
2. and
3. or


=================================================
핵심 정리
=================================================

논리 연산자는:
"Boolean 값(True/False)을 이용하여 복잡한 조건을 표현하는 연산자"

반드시 기억할 점:
1. and는 모두 True일 때만 True (하나라도 False이면 False)
2. or은 하나라도 True이면 True (모두 False일 때만 False)
3. not은 True와 False를 반대로 변환한다
4. 단락 평가를 이용하면 불필요한 연산을 줄일 수 있다
5. 삼항 연산자로 간단한 if~else를 한 줄로 표현할 수 있다

실제 개발에서는:
- 범위 확인 (and 사용)
- 여러 조건 중 하나 확인 (or 사용)
- 조건 부정 (not 사용)
- 사용자 입력 검증 (and, or 조합)
- 게임 상태 확인 (and, or, not 조합)
- 게시글 필터링
- 권한 및 접근 제어

등 거의 모든 조건문과 의사결정 로직에서 사용된다.
"""
