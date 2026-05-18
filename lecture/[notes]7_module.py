"""
모듈(Module) 완전 정리
=================================================

1. 모듈이란?
-------------------------------------------------
모듈은 특정 기능을 모아놓은 파이썬 파일이다.

특징:
- 자주 사용되는 기능을 미리 만들어 놓은 것
- 직접 코딩해야 하는 수고를 덜 수 있다
- import 키워드를 사용하여 가져온다

비유:
모듈은 도구 가게와 같다.
필요한 도구(기능)를 직접 만들지 않고
미리 만들어진 도구를 사서 사용한다.

예시:
random 모듈 → 난수 발생 기능
math 모듈 → 수학 연산 기능
datetime 모듈 → 날짜/시간 기능
"""

# 모듈을 사용하지 않은 경우
# 난수를 발생시키려면 복잡한 수학 알고리즘을 직접 구현해야 함

# 모듈을 사용한 경우
import random

randomNum = random.randrange(1, 10)

print(f'randomNum: {randomNum}')

"""
위 코드 결과 (실행할 때마다 다름):
randomNum: 7

random 모듈의 randrange() 함수를 사용하여
간단하게 난수를 발생시켰다.


2. 모듈 import 하기
-------------------------------------------------
모듈을 사용하려면 import 키워드로 모듈을 가져와야 한다.

형태:
import 모듈이름
"""

import math

result = math.sqrt(16)

print(f'math.sqrt(16): {result}')

"""
위 코드 결과:
math.sqrt(16): 4.0

math 모듈을 import하여 sqrt() 함수를 사용했다.


3. random 모듈 - randrange()
-------------------------------------------------
random 모듈의 randrange() 함수는
지정한 범위 내에서 무작위 정수를 반환한다.

형태:
random.randrange(시작, 끝)
→ 시작 이상 끝 미만의 정수 반환

형태:
random.randrange(끝)
→ 0 이상 끝 미만의 정수 반환
"""

import random

randomNum1 = random.randrange(1, 46)

print(f'1 이상 46 미만의 난수: {randomNum1}')

randomNum2 = random.randrange(10)

print(f'0 이상 10 미만의 난수: {randomNum2}')

randomNum3 = random.randrange(1, 7)

print(f'주사위 번호(1~6): {randomNum3}')

"""
위 코드 결과 (실행할 때마다 다름):
1 이상 46 미만의 난수: 23
0 이상 10 미만의 난수: 7
주사위 번호(1~6): 4


4. random 모듈 - randint()
-------------------------------------------------
random 모듈의 randint() 함수는
지정한 범위 내에서 무작위 정수를 반환한다.

형태:
random.randint(시작, 끝)
→ 시작 이상 끝 이하의 정수 반환 (끝 포함!)

randrange()와 다른 점:
randrange: 끝 미포함
randint: 끝 포함
"""

import random

randomNum1 = random.randint(1, 10)

print(f'1 이상 10 이하의 난수: {randomNum1}')

randomNum2 = random.randint(1, 6)

print(f'주사위 번호(1~6): {randomNum2}')

"""
위 코드 결과 (실행할 때마다 다름):
1 이상 10 이하의 난수: 7
주사위 번호(1~6): 5


5. operator 모듈이란?
-------------------------------------------------
operator 모듈은 산술, 비교, 논리 연산자를 함수로 제공한다.

특징:
- 일반적인 연산자를 함수 형태로 사용할 수 있다
- 코드를 함수형 프로그래밍 스타일로 작성할 수 있다

비유:
+ 기호 대신 add() 함수를 사용하는 것처럼,
모든 연산자를 함수로 표현할 수 있다.
"""

import operator

# 산술 연산자를 일반적으로 사용
result1 = 10 + 20

print(f'10 + 20: {result1}')

# 산술 연산자를 함수로 사용
result2 = operator.add(10, 20)

print(f'operator.add(10, 20): {result2}')

"""
위 코드 결과:
10 + 20: 30
operator.add(10, 20): 30

두 방식의 결과는 동일하다.


6. operator 모듈 - 산술 연산
-------------------------------------------------
"""

import operator

print(f'덧셈:')
print(f'10 + 20 = {10 + 20}')
print(f'operator.add(10, 20) = {operator.add(10, 20)}')
print()

print(f'뺄셈:')
print(f'10 - 20 = {10 - 20}')
print(f'operator.sub(10, 20) = {operator.sub(10, 20)}')
print()

print(f'곱셈:')
print(f'10 * 20 = {10 * 20}')
print(f'operator.mul(10, 20) = {operator.mul(10, 20)}')
print()

print(f'나눗셈:')
print(f'10 / 20 = {10 / 20}')
print(f'operator.truediv(10, 20) = {operator.truediv(10, 20)}')
print()

print(f'나머지:')
print(f'10 % 20 = {10 % 20}')
print(f'operator.mod(10, 20) = {operator.mod(10, 20)}')
print()

print(f'정수 나눗셈:')
print(f'10 // 20 = {10 // 20}')
print(f'operator.floordiv(10, 20) = {operator.floordiv(10, 20)}')
print()

print(f'거듭제곱:')
print(f'10 ** 20 = {10 ** 20}')
print(f'operator.pow(10, 20) = {operator.pow(10, 20)}')

"""
위 코드 결과:
덧셈:
10 + 20 = 30
operator.add(10, 20) = 30

뺄셈:
10 - 20 = -10
operator.sub(10, 20) = -10

곱셈:
10 * 20 = 200
operator.mul(10, 20) = 200

나눗셈:
10 / 20 = 0.5
operator.truediv(10, 20) = 0.5

나머지:
10 % 20 = 10
operator.mod(10, 20) = 10

정수 나눗셈:
10 // 20 = 0
operator.floordiv(10, 20) = 0

거듭제곱:
10 ** 20 = 100000000000000000000
operator.pow(10, 20) = 100000000000000000000

operator 모듈의 산술 연산 함수:
- add: 덧셈
- sub: 뺄셈
- mul: 곱셈
- truediv: 나눗셈 (실수 결과)
- mod: 나머지
- floordiv: 정수 나눗셈
- pow: 거듭제곱


7. operator 모듈 - 비교 연산
-------------------------------------------------
"""

import operator

print(f'같음:')
print(f'10 == 20: {10 == 20}')
print(f'operator.eq(10, 20): {operator.eq(10, 20)}')
print()

print(f'다름:')
print(f'10 != 20: {10 != 20}')
print(f'operator.ne(10, 20): {operator.ne(10, 20)}')
print()

print(f'크다:')
print(f'10 > 20: {10 > 20}')
print(f'operator.gt(10, 20): {operator.gt(10, 20)}')
print()

print(f'크거나 같다:')
print(f'10 >= 20: {10 >= 20}')
print(f'operator.ge(10, 20): {operator.ge(10, 20)}')
print()

print(f'작다:')
print(f'10 < 20: {10 < 20}')
print(f'operator.lt(10, 20): {operator.lt(10, 20)}')
print()

print(f'작거나 같다:')
print(f'10 <= 20: {10 <= 20}')
print(f'operator.le(10, 20): {operator.le(10, 20)}')

"""
위 코드 결과:
같음:
10 == 20: False
operator.eq(10, 20): False

다름:
10 != 20: True
operator.ne(10, 20): True

크다:
10 > 20: False
operator.gt(10, 20): False

크거나 같다:
10 >= 20: False
operator.ge(10, 20): False

작다:
10 < 20: True
operator.lt(10, 20): True

작거나 같다:
10 <= 20: True
operator.le(10, 20): True

operator 모듈의 비교 연산 함수:
- eq: 같음 (==)
- ne: 다름 (!=)
- gt: 크다 (>)
- ge: 크거나 같다 (>=)
- lt: 작다 (<)
- le: 작거나 같다 (<=)


8. operator 모듈 - 논리 연산
-------------------------------------------------
"""

import operator

print(f'논리곱 (and):')
print(f'True and False: {True and False}')
print(f'operator.and_(True, False): {operator.and_(True, False)}')
print()

print(f'논리합 (or):')
print(f'True or False: {True or False}')
print(f'operator.or_(True, False): {operator.or_(True, False)}')
print()

print(f'논리부정 (not):')
print(f'not True: {not True}')
print(f'operator.not_(True): {operator.not_(True)}')

"""
위 코드 결과:
논리곱 (and):
True and False: False
operator.and_(True, False): False

논리합 (or):
True or False: True
operator.or_(True, False): True

논리부정 (not):
not True: False
operator.not_(True): False

operator 모듈의 논리 연산 함수:
- and_: 논리곱 (and)
- or_: 논리합 (or)
- not_: 논리부정 (not)

주의: and_와 or_ 뒤에 언더스코어(_)가 붙어 있다!
이는 and와 or가 파이썬의 예약어이기 때문이다.


9. operator 모듈 활용 예제 - 비교 함수
-------------------------------------------------
"""

import operator

def compare_numbers(num1, num2):
    """두 숫자를 비교하는 함수"""
    
    print(f'num1: {num1}, num2: {num2}')
    print(f'num1 == num2: {operator.eq(num1, num2)}')
    print(f'num1 < num2: {operator.lt(num1, num2)}')
    print(f'num1 > num2: {operator.gt(num1, num2)}')
    print()

compare_numbers(10, 20)
compare_numbers(30, 15)

"""
위 코드 결과:
num1: 10, num2: 20
num1 == num2: False
num1 < num2: True
num1 > num2: False

num1: 30, num2: 15
num1 == num2: False
num1 < num2: False
num1 > num2: True


10. 자주 사용되는 다른 모듈들
-------------------------------------------------

① math 모듈
   - 수학 연산 관련 기능
   - sqrt(): 제곱근
   - ceil(): 올림
   - floor(): 내림
   - pi: 원주율
"""

import math

print(f'math.sqrt(16): {math.sqrt(16)}')
print(f'math.ceil(3.2): {math.ceil(3.2)}')
print(f'math.floor(3.8): {math.floor(3.8)}')
print(f'math.pi: {math.pi}')

"""
위 코드 결과:
math.sqrt(16): 4.0
math.ceil(3.2): 4
math.floor(3.8): 3
math.pi: 3.141592653589793


11. datetime 모듈
-------------------------------------------------
"""

from datetime import datetime

current_time = datetime.now()

print(f'현재 날짜와 시간: {current_time}')
print(f'년도: {current_time.year}')
print(f'월: {current_time.month}')
print(f'일: {current_time.day}')
print(f'시간: {current_time.hour}')
print(f'분: {current_time.minute}')
print(f'초: {current_time.second}')

"""
위 코드 결과:
현재 날짜와 시간: 2024-01-15 14:30:45.123456
년도: 2024
월: 1
일: 15
시간: 14
분: 30
초: 45


12. time 모듈
-------------------------------------------------
"""

import time

print(f'프로그램 시작')

time.sleep(2)

print(f'2초 후에 출력됨')

"""
위 코드 결과:
프로그램 시작
(2초 대기)
2초 후에 출력됨

time.sleep(초): 지정한 초만큼 프로그램을 멈춘다


13. os 모듈 (Operating System)
-------------------------------------------------
"""

import os

print(f'현재 작업 디렉토리: {os.getcwd()}')
print(f'현재 디렉토리의 파일 목록: {os.listdir()}')

"""
위 코드 결과:
현재 작업 디렉토리: C:\\Users\\username\\Desktop
현재 디렉토리의 파일 목록: ['file1.py', 'file2.py', ...]

os.getcwd(): 현재 작업 디렉토리 반환
os.listdir(): 디렉토리의 파일 목록 반환


14. 모듈 함수 이름이 겹칠 때
-------------------------------------------------
여러 모듈을 import할 때 함수 이름이 겹치면
as 키워드로 별칭을 붙여서 구분한다.
"""

import operator as op

result = op.add(10, 20)

print(f'operator.add(10, 20): {result}')

"""
위 코드 결과:
operator.add(10, 20): 30

operator 모듈을 op로 별칭을 지었으므로
op.add()로 사용할 수 있다.


15. 모듈에서 특정 함수만 import
-------------------------------------------------
모듈 전체가 아니라 필요한 함수만 import할 수 있다.

형태:
from 모듈이름 import 함수이름
"""

from math import sqrt, pi

result = sqrt(16)

print(f'sqrt(16): {result}')
print(f'pi: {pi}')

"""
위 코드 결과:
sqrt(16): 4.0
pi: 3.141592653589793

math 모듈에서 sqrt와 pi만 import했다.
따라서 math.sqrt() 대신 sqrt()로 직접 사용할 수 있다.


=================================================
핵심 함수 및 모듈 총정리
=================================================

모듈 import:
import 모듈이름
from 모듈이름 import 함수이름
import 모듈이름 as 별칭

자주 사용되는 모듈:
- random: 난수 생성 (randint, randrange, choice)
- math: 수학 연산 (sqrt, ceil, floor, pi)
- datetime: 날짜/시간 (datetime, date, time)
- time: 시간 관련 (sleep, time)
- os: 운영체제 (getcwd, listdir, remove)
- operator: 연산자 함수 (add, sub, mul, eq, lt)
- sys: 시스템 (argv, exit, version)
- json: JSON 파일 처리
- csv: CSV 파일 처리


=================================================
핵심 정리
=================================================

모듈은:
"특정 기능을 모아놓은 파이썬 파일"

반드시 기억할 점:
1. import 키워드로 모듈을 가져온다
2. 모듈을 사용하면 복잡한 기능을 쉽게 구현할 수 있다
3. random 모듈은 난수 생성에 자주 사용된다
4. operator 모듈은 연산자를 함수로 제공한다
5. as 키워드로 모듈에 별칭을 붙일 수 있다
6. from import로 특정 함수만 가져올 수 있다

실제 개발에서는:
- 난수 생성 (random 모듈)
- 날짜/시간 처리 (datetime 모듈)
- 파일 시스템 접근 (os 모듈)
- 수학 계산 (math 모듈)
- JSON/CSV 파일 처리 (json, csv 모듈)
- 웹 요청 (requests 모듈)
- 데이터 분석 (pandas, numpy 모듈)
- 머신러닝 (scikit-learn, tensorflow 모듈)

등 거의 모든 프로그램에서 모듈을 사용한다.
"""
