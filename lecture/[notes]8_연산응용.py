"""
프로그래밍 문제 풀이 완전 정리
=================================================

1. 수심에 따른 수온 계산 프로그램
-------------------------------------------------
수심이 깊어질수록 수온이 낮아진다.
수심을 입력하면 수온을 계산하는 프로그램

조건:
- 기준 수온: 20°C (수심 0m일 때)
- 수심이 10m 깊어질 때마다 0.7°C 내려감
- 수온 = 20 - (수심 // 10 × 0.7)
"""

data = 50

temperature = 20 - (data // 10 * 0.7)

print(f'수심: {data}m')
print(f'수온: {temperature}°C')

"""
위 코드 결과:
수심: 50m
수온: 16.5°C

계산 과정:
수심 50m → 50 // 10 = 5 (10m씩 5번)
온도 감소 = 5 × 0.7 = 3.5°C
수온 = 20 - 3.5 = 16.5°C
"""

data = 30

temperature = 20 - (data // 10 * 0.7)

print(f'수심: {data}m')
print(f'수온: {temperature}°C')

"""
위 코드 결과:
수심: 30m
수온: 17.9°C


2. 주행 거리 계산 프로그램
-------------------------------------------------
주행 속도와 주행 시간을 입력하면
총 주행 거리를 계산하는 프로그램

공식:
거리 = 속도 × 시간
"""

speed = 60
time = 3

distance = speed * time

print(f'주행 속도: {speed}km/h')
print(f'주행 시간: {time}시간')
print(f'주행 거리: {distance}km')

"""
위 코드 결과:
주행 속도: 60km/h
주행 시간: 3시간
주행 거리: 180km


3. QUIZ - 컴퓨터 필요 개수 계산 프로그램
-------------------------------------------------
A회사의 컴퓨터 처리 능력:
- 3대의 컴퓨터 → 8시간 → 하루 업무 처리 가능
- 근무 시간이 줄어들면 더 많은 컴퓨터가 필요

조건:
- 근무 시간을 입력한다
- 필요한 컴퓨터 개수를 계산한다
- 나머지가 있으면 추가로 1대가 필요하다

공식:
필요한 컴퓨터 = (3 × 8) // 근무시간
나머지가 있으면 + 1
"""

time = 6

# 기본 필요 컴퓨터 개수
computer = (3 * 8) // time

# 나머지가 있으면 추가 1대 필요
addComputer = 1 if (3 * 8 % time) > 0 else 0

totalComputer = computer + addComputer

print(f'근무 시간: {time}시간')
print(f'기본 필요 컴퓨터: {computer}대')
print(f'추가 필요 컴퓨터: {addComputer}대')
print(f'총 필요 컴퓨터: {totalComputer}대')

"""
위 코드 결과:
근무 시간: 6시간
기본 필요 컴퓨터: 4대
추가 필요 컴퓨터: 0대
총 필요 컴퓨터: 4대

계산 과정:
하루 처리량 = 3 × 8 = 24 (컴퓨터-시간)
필요 컴퓨터 = 24 // 6 = 4대
나머지 = 24 % 6 = 0 (추가 필요 없음)
"""

time = 5

computer = (3 * 8) // time
addComputer = 1 if (3 * 8 % time) > 0 else 0
totalComputer = computer + addComputer

print(f'근무 시간: {time}시간')
print(f'총 필요 컴퓨터: {totalComputer}대')

"""
위 코드 결과:
근무 시간: 5시간
총 필요 컴퓨터: 5대

계산 과정:
필요 컴퓨터 = 24 // 5 = 4대
나머지 = 24 % 5 = 4 (추가 필요)
총 필요 = 4 + 1 = 5대


4. QUIZ - 마스크 구매 프로그램
-------------------------------------------------
마스크 한 장의 가격: 340원
구매 개수를 입력하면 총가격과 거스름돈을 계산하는 프로그램
"""

maskPrice = 340
maskCnt = 5

totalPrice = maskPrice * maskCnt

print(f'마스크 가격: {maskPrice}원')
print(f'마스크 개수: {maskCnt}개')
print(f'총 가격: {totalPrice:,}원')

cash = 2000

change = cash - totalPrice

print(f'지불 금액: {cash:,}원')
print(f'거스름 돈: {change:,}원')

"""
위 코드 결과:
마스크 가격: 340원
마스크 개수: 5개
총 가격: 1,700원
지불 금액: 2,000원
거스름 돈: 300원

계산 과정:
총 가격 = 340 × 5 = 1,700원
거스름 돈 = 2,000 - 1,700 = 300원


5. QUIZ - 시간을 초로 변환하는 프로그램
-------------------------------------------------
13시간 30분 25초를 초 단위로 변환하는 프로그램

공식:
총 초 = (시간 × 3600) + (분 × 60) + 초
"""

hour = 13
minute = 30
second = 25

totalSecond = (hour * 3600) + (minute * 60) + second

print(f'시간: {hour}시간 {minute}분 {second}초')
print(f'총 초: {totalSecond}초')

"""
위 코드 결과:
시간: 13시간 30분 25초
총 초: 48625초

계산 과정:
시간 → 초: 13 × 3600 = 46,800초
분 → 초: 30 × 60 = 1,800초
초: 25초
총합: 46,800 + 1,800 + 25 = 48,625초
"""

hour = 2
minute = 15
second = 10

totalSecond = (hour * 3600) + (minute * 60) + second

print(f'시간: {hour}시간 {minute}분 {second}초')
print(f'총 초: {totalSecond}초')

"""
위 코드 결과:
시간: 2시간 15분 10초
총 초: 8110초


6. QUIZ - 학생 성적 처리 프로그램
-------------------------------------------------
국어, 영어, 수학 점수를 입력하면
총점과 평균을 출력하는 프로그램
"""

kor = 85
eng = 92
math = 88

totalScore = kor + eng + math
averageScore = totalScore / 3

print(f'국어 점수: {kor}점')
print(f'영어 점수: {eng}점')
print(f'수학 점수: {math}점')
print(f'총점: {totalScore}점')
print(f'평균: {averageScore:.2f}점')

"""
위 코드 결과:
국어 점수: 85점
영어 점수: 92점
수학 점수: 88점
총점: 265점
평균: 88.33점

계산 과정:
총점 = 85 + 92 + 88 = 265점
평균 = 265 / 3 = 88.333...점
"""

kor = 75
eng = 80
math = 90

totalScore = kor + eng + math
averageScore = totalScore / 3

print(f'총점: {totalScore}점')
print(f'평균: {averageScore:.1f}점')

"""
위 코드 결과:
총점: 245점
평균: 81.7점


7. QUIZ - 일교차 계산 프로그램
-------------------------------------------------
낮 최고 기온과 밤 최저 기온을 입력하면
일교차(낮과 밤의 기온 차이)를 계산하는 프로그램

공식:
일교차 = 낮 최고 기온 - 밤 최저 기온
"""

highTemp = 28
lowTemp = 15

tempRange = highTemp - lowTemp

print(f'낮 최고 기온: {highTemp}°C')
print(f'밤 최저 기온: {lowTemp}°C')
print(f'일교차: {tempRange}°C')

"""
위 코드 결과:
낮 최고 기온: 28°C
밤 최저 기온: 15°C
일교차: 13°C

일교차가 크면 건강 관리가 필요하다.
"""

highTemp = 25
lowTemp = 18

tempRange = highTemp - lowTemp

print(f'낮 최고 기온: {highTemp}°C')
print(f'밤 최저 기온: {lowTemp}°C')
print(f'일교차: {tempRange}°C')

"""
위 코드 결과:
낮 최고 기온: 25°C
밤 최저 기온: 18°C
일교차: 7°C


8. QUIZ - 단위 변환 프로그램 (cm → inch)
-------------------------------------------------
1cm = 0.39 inch (근사값)

길이를 센티미터로 입력하면
인치 단위로 변환하는 프로그램
"""

cm = 100

inch = cm * 0.39

print(f'길이: {cm}cm')
print(f'변환 결과: {inch}inch')
print(f'변환 결과: {inch:.2f}inch')

"""
위 코드 결과:
길이: 100cm
변환 결과: 39.0inch
변환 결과: 39.00inch

계산 과정:
inch = 100 × 0.39 = 39 inch
"""

cm = 50

inch = cm * 0.39

print(f'길이: {cm}cm')
print(f'변환 결과: {inch:.2f}inch')

"""
위 코드 결과:
길이: 50cm
변환 결과: 19.50inch


9. QUIZ - 다른 단위 변환 프로그램들
-------------------------------------------------
다양한 단위 변환을 자주 사용한다.
"""

# 킬로미터 → 마일
km = 10
mile = km * 0.62137

print(f'{km}km = {mile:.2f}mile')

"""
결과:
10km = 6.21mile
"""

# 킬로그램 → 파운드
kg = 75
pound = kg * 2.20462

print(f'{kg}kg = {pound:.2f}pound')

"""
결과:
75kg = 165.35pound
"""

# 섭씨 → 화씨
celsius = 25
fahrenheit = (celsius * 9/5) + 32

print(f'{celsius}°C = {fahrenheit:.2f}°F')

"""
결과:
25°C = 77.00°F


10. 복합 계산 문제
-------------------------------------------------
여러 연산을 조합하여 복잡한 문제를 푼다.
"""

# 직사각형의 넓이와 둘레 계산
width = 10
height = 5

area = width * height
perimeter = 2 * (width + height)

print(f'가로: {width}cm, 세로: {height}cm')
print(f'넓이: {area}㎠')
print(f'둘레: {perimeter}cm')

"""
위 코드 결과:
가로: 10cm, 세로: 5cm
넓이: 50㎠
둘레: 30cm
"""

# 원의 넓이와 둘레 계산
import math

radius = 5

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f'반지름: {radius}cm')
print(f'넓이: {area:.2f}㎠')
print(f'둘레: {circumference:.2f}cm')

"""
위 코드 결과:
반지름: 5cm
넓이: 78.54㎠
둘레: 31.42cm


11. 실무 계산 예제
-------------------------------------------------
"""

# 급여 계산
basicSalary = 3000000
bonus = 0.15  # 15% 보너스

totalSalary = basicSalary + (basicSalary * bonus)

print(f'기본 급여: {basicSalary:,}원')
print(f'보너스: {basicSalary * bonus:,}원')
print(f'총 급여: {totalSalary:,}원')

"""
위 코드 결과:
기본 급여: 3,000,000원
보너스: 450,000원
총 급여: 3,450,000원
"""

# 할인율 적용
originalPrice = 100000
discountRate = 0.20  # 20% 할인

discountAmount = originalPrice * discountRate
finalPrice = originalPrice - discountAmount

print(f'원가: {originalPrice:,}원')
print(f'할인액: {discountAmount:,}원')
print(f'최종 가격: {finalPrice:,}원')

"""
위 코드 결과:
원가: 100,000원
할인액: 20,000원
최종 가격: 80,000원


=================================================
핵심 계산 공식 총정리
=================================================

거리 = 속도 × 시간
속도 = 거리 / 시간
시간 = 거리 / 속도

총 초 = (시간 × 3600) + (분 × 60) + 초

일교차 = 낮 최고 기온 - 밤 최저 기온

넓이 = 가로 × 세로
둘레 = 2 × (가로 + 세로)

원의 넓이 = π × r²
원의 둘레 = 2π × r

평균 = 합계 / 개수

거스름 돈 = 지불 금액 - 상품 가격

최종 가격 = 원가 - (원가 × 할인율)

총 급여 = 기본 급여 + (기본 급여 × 보너스율)


=================================================
핵심 정리
=================================================

프로그래밍 문제 풀이 과정:

1. 문제 분석
   - 주어진 정보 파악
   - 구하려는 값 파악
   - 필요한 공식 확인

2. 변수 정의
   - 입력할 변수들 정의
   - 계산할 변수들 정의

3. 계산 및 출력
   - 공식에 따라 계산
   - 결과 출력
   - 필요시 포맷팅 (소수점, 쉼표 등)

반드시 기억할 점:
1. 문제를 여러 번 읽고 정확히 이해한다
2. 필요한 공식을 정확히 파악한다
3. 단위를 일관되게 사용한다
4. 계산 순서가 중요하다
5. 결과가 합리적인지 검토한다

실제 개발에서 자주 사용되는 계산:
- 가격/결제 계산
- 시간/날짜 계산
- 통계 계산 (평균, 합계)
- 단위 변환
- 기하학 계산 (넓이, 둘레)
- 물리 계산 (거리, 속도, 시간)

등에서 기본이 되는 계산들이다.
"""
