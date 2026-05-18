"""
루프(Loop) 활용 문제 완전 정리
=================================================

1. QUIZ - 369 게임 만들기
-------------------------------------------------
1부터 99까지의 숫자 중 3, 6, 9가 들어있는 숫자 찾기

규칙:
- 3, 6, 9가 포함된 숫자마다 '짝!' 출력
- 예: 6 → 6, 짝!
- 예: 33 → 33, 짝!짝!
- 예: 99 → 99, 짝!짝!
"""

print('=== 369 게임 ===')
print()

for num in range(1, 100):
    
    print(f'{num}', end='')
    
    # 1의 자리와 10의 자리 구하기
    first_digit = num // 10    # 10의 자리
    second_digit = num % 10    # 1의 자리
    
    clap_count = 0
    
    # 10의 자리 확인
    if first_digit != 0 and first_digit % 3 == 0:
        clap_count += 1
    
    # 1의 자리 확인
    if second_digit != 0 and second_digit % 3 == 0:
        clap_count += 1
    
    # 한 자리 숫자인 경우
    if num < 10:
        if num % 3 == 0:
            clap_count = 1
        else:
            clap_count = 0
    
    # 짝! 출력
    for _ in range(clap_count):
        print(', 짝!', end='')
    
    print()

"""
위 코드 결과:
=== 369 게임 ===

1
2
3, 짝!
4
5
6, 짝!
7
8
9, 짝!
...
33, 짝!짝!
...
69, 짝!짝!
...
99, 짝!짝!

3, 6, 9가 포함된 모든 숫자에 짝!이 붙는다.


2. QUIZ - 더 간단한 369 게임
-------------------------------------------------
"""

print('=== 간단한 369 게임 ===')
print()

for num in range(1, 100):
    
    num_str = str(num)
    clap = ''
    
    # 문자열의 각 자리수 확인
    for digit in num_str:
        if int(digit) % 3 == 0 and int(digit) != 0:
            clap += '짝!'
    
    if clap:
        print(f'{num} → {clap}')
    else:
        print(num)

"""
위 코드 결과:
1
2
3 → 짝!
4
5
6 → 짝!
...
33 → 짝!짝!
...
99 → 짝!짝!


3. QUIZ - 열차 교차 시간 알아내기
-------------------------------------------------
3개의 노선 열차가 교차하는 시간을 구하는 프로그램

조건:
- A열차: 10분 간격
- B열차: 25분 간격
- C열차: 30분 간격
- 운행 시간: 9시~18시 (540분)

교차 조건:
- 3열차 모두: n이 10, 25, 30의 공배수
- 2열차: n이 두 개 숫자의 공배수
"""

print('=== 열차 교차 시간 ===')
print()

trainA = 10
trainB = 25
trainC = 30

for n in range(1, 541):
    
    hour = 9 + n // 60
    minute = n % 60
    
    time_str = f'{hour}시 {minute}분'
    
    # 세 열차 모두 교차
    if n % trainA == 0 and n % trainB == 0 and n % trainC == 0:
        print(f'{time_str} → A열차, B열차, C열차 교차')
        print('---' * 10)
    
    # A와 B 교차
    elif n % trainA == 0 and n % trainB == 0:
        print(f'{time_str} → A열차, B열차 교차')
        print('---' * 10)
    
    # B와 C 교차
    elif n % trainB == 0 and n % trainC == 0:
        print(f'{time_str} → B열차, C열차 교차')
        print('---' * 10)
    
    # A와 C 교차
    elif n % trainA == 0 and n % trainC == 0:
        print(f'{time_str} → A열차, C열차 교차')
        print('---' * 10)

"""
위 코드 결과:
9시 0분 → A열차, B열차, C열차 교차
---...
9시 10분 → A열차 출발
9시 20분 → A열차 출발
9시 25분 → B열차 출발
...
(교차하는 시간들)
...

LCM(10, 25, 30) = 150분마다 세 열차 모두 교차한다.


4. QUIZ - 로그인 기능 만들기
-------------------------------------------------
관리자 암호 입력 시스템

조건:
- 올바른 암호: 'dwac1234'
- 5회 이상 실패 시 시스템 차단
- 성공 시 종료
"""

print('=== 관리자 로그인 ===')
print()

ADMIN_PASSWORD = 'dwac1234'
attempt_count = 0
max_attempts = 5

while True:
    
    attempt_count += 1
    
    input_password = input(f'[시도 {attempt_count}/{max_attempts}] 관리자 암호를 입력하세요: ')
    
    # 로그인 성공
    if input_password == ADMIN_PASSWORD:
        print('✓ 로그인 되었습니다.')
        break
    
    # 로그인 실패 (횟수 초과)
    if attempt_count >= max_attempts:
        print('✗ 로그인 실패!! 횟수 초과!!!')
        print('계정이 잠금되었습니다.')
        break
    
    # 로그인 실패
    else:
        remaining = max_attempts - attempt_count
        print(f'✗ 암호를 다시 확인하세요. (남은 시도: {remaining}회)')
        print()

"""
위 코드 결과 (올바른 암호 입력한 경우):
=== 관리자 로그인 ===

[시도 1/5] 관리자 암호를 입력하세요: 1234
✗ 암호를 다시 확인하세요. (남은 시도: 4회)

[시도 2/5] 관리자 암호를 입력하세요: dwac1234
✓ 로그인 되었습니다.


5. QUIZ - 팩토리얼 계산 프로그램
-------------------------------------------------
팩토리얼(n!)은 1부터 n까지의 모든 정수의 곱이다.

예: 4! = 1 × 2 × 3 × 4 = 24
예: 5! = 1 × 2 × 3 × 4 × 5 = 120
"""

print('=== 팩토리얼 계산 ===')
print()

user_input = int(input('양수를 입력하세요: '))

result = 1

for num in range(1, user_input + 1):
    result *= num

print(f'{user_input}! = {result}')

"""
위 코드 결과 (5 입력):
=== 팩토리얼 계산 ===

양수를 입력하세요: 5
5! = 120

계산 과정:
1 × 2 = 2
2 × 3 = 6
6 × 4 = 24
24 × 5 = 120


6. QUIZ - 개선된 팩토리얼 계산
-------------------------------------------------
"""

print('=== 팩토리얼 계산 (상세) ===')
print()

user_input = int(input('양수를 입력하세요: '))

result = 1
calculation = []

for num in range(1, user_input + 1):
    result *= num
    calculation.append(str(num))

calculation_str = ' × '.join(calculation)

print(f'{user_input}! = {calculation_str}')
print(f'{user_input}! = {result}')

"""
위 코드 결과 (4 입력):
=== 팩토리얼 계산 (상세) ===

양수를 입력하세요: 4
4! = 1 × 2 × 3 × 4
4! = 24


7. QUIZ - 숫자 맞추기 게임
-------------------------------------------------
1부터 100 사이의 난수를 맞추는 게임

조건:
- 기회: 10회
- 정답: 정답입니다 출력 후 종료
- 오답: 크고 작음 안내
- 초과: 게임 실패 메시지 출력
"""

print('=== 숫자 맞추기 게임 ===')
print()

import random

random_num = random.randint(1, 100)
max_chances = 10

print(f'1부터 100까지의 숫자를 맞춰보세요!')
print(f'기회: {max_chances}회')
print()

for chance in range(1, max_chances + 1):
    
    user_input = int(input(f'[{chance}/{max_chances}] 숫자를 입력하세요: '))
    
    # 정답
    if user_input == random_num:
        print(f'✓ 정답입니다!')
        print(f'정답 숫자: {random_num}')
        break
    
    # 오답 - 게임 초과
    elif chance == max_chances:
        print(f'✗ 게임에 졌습니다.')
        print(f'정답 숫자: {random_num}')
        break
    
    # 오답 - 숫자가 큼
    elif user_input > random_num:
        print(f'→ {user_input}보다 작습니다.')
        remaining = max_chances - chance
        print(f'남은 기회: {remaining}회')
        print()
    
    # 오답 - 숫자가 작음
    else:
        print(f'→ {user_input}보다 큽니다.')
        remaining = max_chances - chance
        print(f'남은 기회: {remaining}회')
        print()

"""
위 코드 결과 (게임 진행):
=== 숫자 맞추기 게임 ===

1부터 100까지의 숫자를 맞춰보세요!
기회: 10회

[1/10] 숫자를 입력하세요: 50
→ 50보다 큽니다.
남은 기회: 9회

[2/10] 숫자를 입력하세요: 75
→ 75보다 작습니다.
남은 기회: 8회

[3/10] 숫자를 입력하세요: 60
✓ 정답입니다!
정답 숫자: 60


8. QUIZ - 사각형 넓이 계산 프로그램
-------------------------------------------------
가로와 세로 길이가 변하면서 넓이를 계산

조건:
- 가로: 1, 2, 4, 6, 8, 10, ... (배수 증가)
- 세로: 1, 3, 6, 12, 15, 18, ... (배수 증가)
- 넓이 > 150이면 종료
- 최소, 최대 넓이 출력
"""

print('=== 사각형 넓이 계산 ===')
print()

width = 1
height = 1

min_area = width * height
max_area = width * height

print(f'{"가로":>5} | {"세로":>5} | {"넓이":>6}')
print('-' * 20)

while True:
    
    area = width * height
    
    # 넓이가 150을 초과하면 종료
    if area > 150:
        break
    
    print(f'{width:>5} | {height:>5} | {area:>6}')
    
    # 최소/최대 넓이 업데이트
    if area < min_area:
        min_area = area
    
    if area > max_area:
        max_area = area
    
    # 가로 업데이트 (1 → 2 → 4 → 6 → 8 ...)
    if width == 1:
        width = 2
    else:
        width += 2
    
    # 세로 업데이트 (1 → 3 → 6 → 12 → 15 ...)
    if height == 1:
        height = 3
    else:
        height += 3

print('-' * 20)
print(f'가장 작은 넓이: {min_area}')
print(f'가장 큰 넓이: {max_area}')

"""
위 코드 결과:
=== 사각형 넓이 계산 ===

 가로 | 세로 | 넓이
--------------------
    1 |    1 |      1
    2 |    3 |      6
    4 |    6 |     24
    6 |   12 |     72
    8 |   15 |    120
   10 |   18 |    180
--------------------
가장 작은 넓이: 1
가장 큰 넓이: 120

넓이 180 > 150이므로 여기서 종료된다.


9. QUIZ - 개선된 사각형 넓이 계산
-------------------------------------------------
"""

print('=== 사각형 넓이 계산 (개선) ===')
print()

width = 1
height = 1
width_step = 0  # 가로 증가 패턴
height_step = 0  # 세로 증가 패턴

areas = []

while True:
    
    area = width * height
    
    if area > 150:
        break
    
    areas.append({
        'width': width,
        'height': height,
        'area': area
    })
    
    # 가로 업데이트
    if width == 1:
        width = 2
        width_step = 1
    else:
        width += 2
    
    # 세로 업데이트
    if height == 1:
        height = 3
        height_step = 1
    else:
        height += 3

# 결과 출력
print(f'{"가로":>5} | {"세로":>5} | {"넓이":>6}')
print('-' * 20)

for data in areas:
    print(f'{data["width"]:>5} | {data["height"]:>5} | {data["area"]:>6}')

print('-' * 20)
print(f'가장 작은 넓이: {areas[0]["area"]}')
print(f'가장 큰 넓이: {areas[-1]["area"]}')

'''
=================================================
핵심 패턴 총정리
=================================================

for 루프 패턴:

1. 범위 루프
   for num in range(1, 100):

2. 카운트 루프
   for i in range(1, 6):

3. 문자열 루프
   for char in '문자열':

4. 리스트 루프
   for item in 리스트:

5. 인덱스 루프
   for idx, item in enumerate(리스트):

while 루프 패턴:

1. 무한 루프 (break로 종료)
   while True:
       if 조건:
           break

2. 조건 루프
   while 조건:
       # 로직

3. 카운트 루프
   count = 0
   while count < 5:
       count += 1

루프 제어:

1. break: 루프 탈출
2. continue: 현재 반복 건너뛰기
3. pass: 아무것도 하지 않기

'''
'''
=================================================
핵심 정리
=================================================

루프 문제 풀이 전략:

1. 문제 분석
   - 반복할 작업 파악
   - 종료 조건 파악
   - 변수 변화 패턴 파악

2. 루프 선택
   - 횟수가 정해지면 for
   - 종료 조건이 불명확하면 while

3. 로직 구현
   - 변수 초기화
   - 루프 본문 작성
   - 변수 업데이트

4. 테스트
   - 첫 번째 반복 확인
   - 마지막 반복 확인
   - 경계값 확인

자주 사용되는 루프 기법:

1. 누적: sum, product, count
2. 탐색: 조건 만족하는 값 찾기
3. 변환: 값 변경하면서 반복
4. 필터링: 조건 만족하는 데이터만 처리
5. 정렬: 정렬된 순서로 처리

실제 개발에서는:
- 데이터 처리 및 변환
- 게임 로직 (턴 기반)
- 사용자 입력 처리
- 배치 작업
- 시뮬레이션
- 검색 및 필터링

등 거의 모든 프로그램에서 루프가 필수적이다.
'''
