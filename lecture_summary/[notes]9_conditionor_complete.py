"""
조건문(if문) 완전 정리
=================================================

1. 조건문(if문)이란?
-------------------------------------------------
조건문은 특정 조건에 따라 실행 여부를 결정하는 구문이다.

형태:
if 조건식:
    실행문

조건식이 True(참)이면 실행문을 실행하고,
조건식이 False(거짓)이면 실행문을 건너뛴다.
"""

num = 5
if num > 10:
    print('num은 10보다 크다')

print(f'num: {num}')
print(f'num > 10: {num > 10}')

"""
위 코드에서:
- num = 5
- num > 10 = False
- 따라서 print('num은 10보다 크다')는 실행되지 않음
"""

num = 15
if num > 10:
    print('num은 10보다 크다')

print(f'num: {num}')
print(f'num > 10: {num > 10}')

"""
위 코드에서:
- num = 15
- num > 10 = True
- 따라서 print('num은 10보다 크다')가 실행됨


2. if문 구성 요소
-------------------------------------------------

① if 키워드
   → 조건문을 선언하는 키워드
   → '만약 ~ 라면'의 의미

② 조건식
   → 특정 조건을 기술
   → 결과에 따라 실행 여부가 결정됨

③ 콜론(:)
   → 코드 블록의 시작을 나타냄
   → 콜론 이후부터 실행될 문장

④ 실행문
   → 조건식이 True일 경우 실행
   → 조건식이 False일 경우 미실행

⑤ 들여쓰기
   → 코드 블록 유지를 위해 같은 크기의 공백 유지 필수
"""

# if 키워드   조건식      콜론
#   if      num > 10     :
#           실행문

"""
3. 기본 예제 - 정수 비교 프로그램
-------------------------------------------------
사용자가 입력한 정수가 10보다 크면 실행문을 출력하는 프로그램
"""

num = 8

if num > 10:
    print(f'{num}은 10보다 크다.')

if num == 10:
    print(f'{num}은 10과 같다.')

if num < 10:
    print(f'{num}은 10보다 작다.')

print(f'num: {num}')

"""
위 코드 결과:
- num = 8
- num < 10 = True이므로 '8은 10보다 작다.'가 출력됨


4. QUIZ - 속도위반 경고 프로그램
-------------------------------------------------
제한 속도가 50km/h인 도로에서 속도위반 차량에 경고를 하는 프로그램
"""

carSpeed = 55

if carSpeed > 50:
    print('속도 위반!!!')

if carSpeed <= 50:
    print('정상 운행')

print(f'carSpeed: {carSpeed}')

"""
위 코드 결과:
- carSpeed = 55
- carSpeed > 50 = True이므로 '속도 위반!!!'가 출력됨
"""

carSpeed = 40

if carSpeed > 50:
    print('속도 위반!!!')

if carSpeed <= 50:
    print('정상 운행')

print(f'carSpeed: {carSpeed}')

"""
위 코드 결과:
- carSpeed = 40
- carSpeed <= 50 = True이므로 '정상 운행'이 출력됨


5. 코드 블록(Code Block) 규칙
-------------------------------------------------
들여쓰기 너비가 같다면 실행문들 사이 빈 줄이 몇 개든
하나의 코드 블록으로 인식된다.
"""

carSpeed = 40

if carSpeed <= 50:
    print('정상 운행')

    print('좋아요~~')

print(f'carSpeed: {carSpeed}')

"""
위 코드 결과:
- 같은 들여쓰기 크기의 두 print문은 모두 실행됨
- 결과:
  정상 운행
  좋아요~~
  carSpeed: 40
"""

if carSpeed <= 50: print('정상 운행')

"""
실행문이 한 줄일 경우만 한 줄로 간략화 가능
(두 줄 이상은 불가)


6. pass 키워드
-------------------------------------------------
실행문이 아직 정해지지 않았을 때,
'나중에 코딩할테니 일단 넘어가라'는 의미로 사용한다.
"""

num = 5

if num > 0:
    pass

print(f'num: {num}')
print(f'코드 실행이 정상적으로 진행됨')

"""
pass 키워드를 사용하지 않으면 문법 오류가 발생한다.
나중에 if문 안에 실행문을 추가할 계획이 있을 때 사용한다.


7. if ~ else 구문
-------------------------------------------------
else는 '그렇지 않으면'의 의미로,
조건식이 False일 때 실행할 코드 블록을 지정한다.

형태:
if 조건식:
    실행문 (True일 때)
else:
    실행문 (False일 때)
"""

myScore = 70

if myScore >= 90:
    print('용돈 획득~~')
else:
    print('빠따~~')

print(f'myScore: {myScore}')

"""
위 코드 결과:
- myScore = 70
- myScore >= 90 = False이므로 else의 '빠따~~'가 출력됨
"""

myScore = 95

if myScore >= 90:
    print('용돈 획득~~')
else:
    print('빠따~~')

print(f'myScore: {myScore}')

"""
위 코드 결과:
- myScore = 95
- myScore >= 90 = True이므로 '용돈 획득~~'이 출력됨

만약 if문만 사용했다면:
if myScore >= 90:
    print('용돈 획득~~')
if myScore < 90:
    print('빠따~~')

이렇게 조건문을 2개 써야 한다.
else를 사용하면 하나로 처리할 수 있다. → 더 효율적!


8. if ~ elif 구문 (다중 선택)
-------------------------------------------------
여러 조건을 순서대로 검사할 때 사용한다.

형태:
if 조건식1:
    실행문1
elif 조건식2:
    실행문2
elif 조건식3:
    실행문3
else:
    실행문4 (위 조건 모두 False일 때)

예시: 점수에 따른 학점 출력
"""

myScore = 85

if myScore >= 90:
    print('A')
elif myScore >= 80:
    print('B')
elif myScore >= 70:
    print('C')
elif myScore >= 60:
    print('D')
else:
    print('F')

print(f'myScore: {myScore}')

"""
위 코드 결과:
- myScore = 85
- myScore >= 90 = False
- myScore >= 80 = True이므로 'B'가 출력됨
"""

myScore = 72

if myScore >= 90:
    print('A')
elif myScore >= 80:
    print('B')
elif myScore >= 70:
    print('C')
elif myScore >= 60:
    print('D')
else:
    print('F')

print(f'myScore: {myScore}')

"""
위 코드 결과:
- myScore = 72
- myScore >= 70 = True이므로 'C'가 출력됨
"""

"""
논리 연산자(and)를 활용한 명시적 범위 지정 버전
"""

myScore = 85

if myScore >= 90:
    print('A')
elif (myScore >= 80) and (myScore < 90):
    print('B')
elif (myScore >= 70) and (myScore < 80):
    print('C')
elif (myScore >= 60) and (myScore < 70):
    print('D')
else:
    print('F')

print(f'myScore: {myScore}')

"""
위 코드 결과:
- (85 >= 80) and (85 < 90) = True이므로 'B'가 출력됨
- 더 명시적으로 범위를 표현할 수 있다


9. QUIZ - 다국어 자동 주문 시스템
-------------------------------------------------
번호를 선택하면 해당 언어로 주문을 받는 프로그램

1. 대한민국  2. USA  3. 中國  그 외 → 영어
"""

selectedNumber = 1

if selectedNumber == 1:
    print('주문하시겠습니까?')
elif selectedNumber == 2:
    print('Would you like to order?')
elif selectedNumber == 3:
    print('니취팔러마?')
else:
    print('Would you like to order?')

print(f'selectedNumber: {selectedNumber}')

"""
위 코드 결과:
- selectedNumber = 1
- selectedNumber == 1 = True이므로 '주문하시겠습니까?'가 출력됨
"""

selectedNumber = 2

if selectedNumber == 1:
    print('주문하시겠습니까?')
elif selectedNumber == 2:
    print('Would you like to order?')
elif selectedNumber == 3:
    print('니취팔러마?')
else:
    print('Would you like to order?')

print(f'selectedNumber: {selectedNumber}')

"""
위 코드 결과:
- selectedNumber = 2
- selectedNumber == 2 = True이므로 'Would you like to order?'가 출력됨


10. QUIZ - 국가재난지원금 안내 프로그램
-------------------------------------------------
가구 인원수에 따른 지원금 수령액 안내

1인 가구  → 400,000원
2인 가구  → 600,000원
3인 가구  → 800,000원
4인 이상  → 1,000,000원

※ 리팩토링(Refactoring):
   프로그램의 기능은 그대로 유지하면서 코드를 더 좋게 고치는 작업
"""

SINGLE = 1
DOUBLE = 2
TRIPLE = 3

family = 2

if family == SINGLE:
    print('400,000원')
elif family == DOUBLE:
    print('600,000원')
elif family == TRIPLE:
    print('800,000원')
else:
    print('1,000,000원')

print(f'family: {family}')

"""
위 코드 결과:
- family = 2 (DOUBLE)
- family == DOUBLE = True이므로 '600,000원'이 출력됨
"""

family = 4

if family == SINGLE:
    print('400,000원')
elif family == DOUBLE:
    print('600,000원')
elif family == TRIPLE:
    print('800,000원')
else:
    print('1,000,000원')

print(f'family: {family}')

"""
위 코드 결과:
- family = 4
- 위의 모든 elif 조건이 False이므로 else의 '1,000,000원'이 출력됨


11. 중첩 조건문 (Nested if)
-------------------------------------------------
조건문 안에 또 다른 조건문을 쓸 수 있다.
이를 중첩 조건문이라고 한다.

형태:
if 조건식1:
    if 조건식2:
        실행문

비유:
- 일반 if문 = 1층 선택지
- 중첩 if문 = 2층, 3층 선택지

예시: 양수 판별 후 홀수/짝수 구분
"""

myInteger = 7

if myInteger >= 0:
    if myInteger % 2 == 0:
        print('짝수!')
    else:
        print('홀수!')
else:
    print('음수!')

print(f'myInteger: {myInteger}')

"""
위 코드 결과:
- myInteger = 7
- myInteger >= 0 = True (1차 조건 통과)
- myInteger % 2 == 0 = False
- myInteger % 2 != 0 = True이므로 '홀수!'가 출력됨
"""

myInteger = -5

if myInteger >= 0:
    if myInteger % 2 == 0:
        print('짝수!')
    else:
        print('홀수!')
else:
    print('음수!')

print(f'myInteger: {myInteger}')

"""
위 코드 결과:
- myInteger = -5
- myInteger >= 0 = False (1차 조건 불통과)
- 중첩된 if문은 실행되지 않음
- else의 '음수!'가 출력됨


12. QUIZ - 짝수/홀수 판별 프로그램
-------------------------------------------------
양의 정수를 입력하면 짝수 또는 홀수를 판별하는 프로그램
"""

num = 8

if num > 0:
    if num % 2 == 0:
        print('짝수')
    else:
        print('홀수')
else:
    print('입력한 정수는 0 또는 음수입니다.')

print(f'num: {num}')

"""
위 코드 결과:
- num = 8
- num > 0 = True (1차 조건 통과)
- num % 2 == 0 = True이므로 '짝수'가 출력됨
"""

num = 9

if num > 0:
    if num % 2 == 0:
        print('짝수')
    else:
        print('홀수')
else:
    print('입력한 정수는 0 또는 음수입니다.')

print(f'num: {num}')

"""
위 코드 결과:
- num = 9
- num > 0 = True (1차 조건 통과)
- num % 2 == 0 = False이므로 else의 '홀수'가 출력됨
"""

num = -3

if num > 0:
    if num % 2 == 0:
        print('짝수')
    else:
        print('홀수')
else:
    print('입력한 정수는 0 또는 음수입니다.')

print(f'num: {num}')

"""
위 코드 결과:
- num = -3
- num > 0 = False (1차 조건 불통과)
- else의 '입력한 정수는 0 또는 음수입니다.'가 출력됨


13. QUIZ - 공적마스크 5부제 프로그램
-------------------------------------------------
출생연도 끝자리와 나이를 입력하면 마스크 구매 가능 요일을 출력

끝자리 1, 6 → 월요일
끝자리 2, 7 → 화요일
끝자리 3, 8 → 수요일
끝자리 4, 9 → 목요일
끝자리 5, 0 → 금요일
만 65세 이상 → 언제나 구매 가능
"""

endBirthYear = 6
age = 45

if age >= 65:
    print('언제나 구매 가능합니다.')
else:
    if endBirthYear == 1 or endBirthYear == 6:
        print('월요일에 구매 가능합니다.')
    elif endBirthYear == 2 or endBirthYear == 7:
        print('화요일에 구매 가능합니다.')
    elif endBirthYear == 3 or endBirthYear == 8:
        print('수요일에 구매 가능합니다.')
    elif endBirthYear == 4 or endBirthYear == 9:
        print('목요일에 구매 가능합니다.')
    elif endBirthYear == 5 or endBirthYear == 0:
        print('금요일에 구매 가능합니다.')

print(f'endBirthYear: {endBirthYear}, age: {age}')

"""
위 코드 결과:
- age = 45
- age >= 65 = False
- endBirthYear == 6 = True이므로 '월요일에 구매 가능합니다.'가 출력됨
"""

endBirthYear = 3
age = 70

if age >= 65:
    print('언제나 구매 가능합니다.')
else:
    if endBirthYear == 1 or endBirthYear == 6:
        print('월요일에 구매 가능합니다.')
    elif endBirthYear == 2 or endBirthYear == 7:
        print('화요일에 구매 가능합니다.')
    elif endBirthYear == 3 or endBirthYear == 8:
        print('수요일에 구매 가능합니다.')
    elif endBirthYear == 4 or endBirthYear == 9:
        print('목요일에 구매 가능합니다.')
    elif endBirthYear == 5 or endBirthYear == 0:
        print('금요일에 구매 가능합니다.')

print(f'endBirthYear: {endBirthYear}, age: {age}')

"""
위 코드 결과:
- age = 70
- age >= 65 = True이므로 '언제나 구매 가능합니다.'가 출력됨


14. QUIZ - 차량 2부제 프로그램
-------------------------------------------------
오늘 날짜와 차량 번호를 비교하여 입차 가능 여부를 결정

짝수 날  → 차량 번호 짝수인 차량 입차 가능
홀수 날  → 차량 번호 홀수인 차량 입차 가능

datetime 모듈을 사용하여 오늘 날짜를 자동으로 가져온다.
"""

from datetime import datetime

dayNum = 14
carNum = 2468

print(f'오늘 날짜: {dayNum}일')

if dayNum % 2 == 0:
    print('오늘 입차: 번호가 짝수인 차량')
else:
    print('오늘 입차: 번호가 홀수인 차량')

if dayNum % 2 == carNum % 2:
    print('귀하의 차량은 입차 가능합니다.')
else:
    print('귀하의 차량은 입차 불가능합니다.')

print(f'dayNum: {dayNum}, carNum: {carNum}')

"""
위 코드 결과:
- dayNum = 14 (짝수 날)
- carNum = 2468 (짝수 차량번호)
- dayNum % 2 == carNum % 2 = True이므로 '귀하의 차량은 입차 가능합니다.'가 출력됨
"""

dayNum = 15
carNum = 1357

print(f'오늘 날짜: {dayNum}일')

if dayNum % 2 == 0:
    print('오늘 입차: 번호가 짝수인 차량')
else:
    print('오늘 입차: 번호가 홀수인 차량')

if dayNum % 2 == carNum % 2:
    print('귀하의 차량은 입차 가능합니다.')
else:
    print('귀하의 차량은 입차 불가능합니다.')

print(f'dayNum: {dayNum}, carNum: {carNum}')

"""
위 코드 결과:
- dayNum = 15 (홀수 날)
- carNum = 1357 (홀수 차량번호)
- dayNum % 2 == carNum % 2 = True이므로 '귀하의 차량은 입차 가능합니다.'가 출력됨


15. QUIZ - 심장충격기 생존율 안내 프로그램
-------------------------------------------------
최초 장비 사용 시간에 따른 환자 생존율을 출력

60초 이하   → 85%
60~120초    → 76%
120~180초   → 66%
180~240초   → 57%
240~300초   → 47%
300초 초과  → 25% 미만
"""

time = 45

if time <= 60:
    print('생존율: 85%')
elif time > 60 and time <= 120:
    print('생존율: 76%')
elif time > 120 and time <= 180:
    print('생존율: 66%')
elif time > 180 and time <= 240:
    print('생존율: 57%')
elif time > 240 and time <= 300:
    print('생존율: 47%')
else:
    print('생존율: 25% 미만')

print(f'time: {time}초')

"""
위 코드 결과:
- time = 45
- time <= 60 = True이므로 '생존율: 85%'가 출력됨
"""

time = 250

if time <= 60:
    print('생존율: 85%')
elif time > 60 and time <= 120:
    print('생존율: 76%')
elif time > 120 and time <= 180:
    print('생존율: 66%')
elif time > 180 and time <= 240:
    print('생존율: 57%')
elif time > 240 and time <= 300:
    print('생존율: 47%')
else:
    print('생존율: 25% 미만')

print(f'time: {time}초')

"""
위 코드 결과:
- time = 250
- time > 240 and time <= 300 = True이므로 '생존율: 47%'가 출력됨


16. QUIZ - 전기요금 계산 프로그램
-------------------------------------------------
전기 사용량을 입력하면 누진세가 적용된 전기요금을 출력

사용량          단가(원)    기본요금(원)
200 이하        99.3        910
201 ~ 400       187.9       1,600
400 초과        280.6       7,300

전기 요금 = (사용량 × 단가) + 기본요금
"""

usedElec = 150

if usedElec <= 200:
    unitPrice = 99.3
    basicRate = 910
elif usedElec <= 400:
    unitPrice = 187.9
    basicRate = 1600
else:
    unitPrice = 280.6
    basicRate = 7300

elecPrice = (usedElec * unitPrice) + basicRate

print(f'사용량   : {usedElec} kwh')
print(f'기본요금 : {basicRate} 원')
print(f'단가     : {unitPrice} 원')
print(f'전기요금 : {elecPrice:.1f} 원')

"""
위 코드 결과:
- usedElec = 150
- usedElec <= 200 = True
- unitPrice = 99.3, basicRate = 910
- elecPrice = (150 × 99.3) + 910 = 15885.0원
"""

usedElec = 350

if usedElec <= 200:
    unitPrice = 99.3
    basicRate = 910
elif usedElec <= 400:
    unitPrice = 187.9
    basicRate = 1600
else:
    unitPrice = 280.6
    basicRate = 7300

elecPrice = (usedElec * unitPrice) + basicRate

print(f'사용량   : {usedElec} kwh')
print(f'기본요금 : {basicRate} 원')
print(f'단가     : {unitPrice} 원')
print(f'전기요금 : {elecPrice:.1f} 원')

"""
위 코드 결과:
- usedElec = 350
- usedElec <= 400 = True
- unitPrice = 187.9, basicRate = 1600
- elecPrice = (350 × 187.9) + 1600 = 67365.0원


17. 삼항 연산자 (조건식)
-------------------------------------------------
if ~ else 구문을 한 줄로 간략하게 표현하는 방식이다.

형태:
변수 = 참일 때 값  if  조건식  else  거짓일 때 값
"""

testScore = 90

result = 'success' if testScore >= 85 else 'fail'

print(f'testScore: {testScore}')
print(f'result: {result}')

"""
위 코드 결과:
- testScore = 90
- testScore >= 85 = True
- result = 'success'
"""

testScore = 75

result = 'success' if testScore >= 85 else 'fail'

print(f'testScore: {testScore}')
print(f'result: {result}')

"""
위 코드 결과:
- testScore = 75
- testScore >= 85 = False
- result = 'fail'

삼항 연산자 없이 if~else로 쓰면:
if testScore >= 85:
    result = 'success'
else:
    result = 'fail'

삼항 연산자는 코드를 더 간결하게 만들어준다.


18. QUIZ - 가위바위보 프로그램
-------------------------------------------------
컴퓨터와 사용자가 가위바위보를 하는 프로그램

1 → 가위
2 → 바위
3 → 보

random 모듈을 사용하여 컴퓨터의 선택을 무작위로 결정한다.
"""

import random

ranNum = 1
myNum = 3

print(f'컴퓨터: {ranNum}, 사용자: {myNum}')

if ranNum == myNum:
    print('무승부')
elif (myNum == 1 and ranNum == 3) or \
     (myNum == 2 and ranNum == 1) or \
     (myNum == 3 and ranNum == 2):
    print('사용자 승')
else:
    print('컴퓨터 승')

"""
위 코드 결과:
- ranNum = 1 (가위), myNum = 3 (보)
- myNum == 3 and ranNum == 2 = False
- myNum == 3 and ranNum == 2를 확인하면 True가 되어야 사용자 승리
- 현재는 사용자가 보(3), 컴퓨터가 가위(1)이므로 사용자 승
"""

ranNum = 2
myNum = 2

print(f'컴퓨터: {ranNum}, 사용자: {myNum}')

if ranNum == myNum:
    print('무승부')
elif (myNum == 1 and ranNum == 3) or \
     (myNum == 2 and ranNum == 1) or \
     (myNum == 3 and ranNum == 2):
    print('사용자 승')
else:
    print('컴퓨터 승')

"""
위 코드 결과:
- ranNum = 2 (바위), myNum = 2 (바위)
- ranNum == myNum = True
- '무승부'가 출력됨


19. QUIZ - SMS / MMS 발송 프로그램
-------------------------------------------------
메시지 길이에 따라 SMS 또는 MMS 발송 여부를 결정

메시지 길이 50 이하  → SMS 발송
메시지 길이 50 초과  → MMS 발송
"""

useMessage = 'hello'
msgLen = len(useMessage)

if msgLen <= 50:
    print('SMS 발송!')
else:
    print('MMS 발송!')

print(f'useMessage: {useMessage}')
print(f'msgLen: {msgLen}')

"""
위 코드 결과:
- useMessage = 'hello'
- msgLen = 5
- msgLen <= 50 = True이므로 'SMS 발송!'이 출력됨
"""

useMessage = 'a' * 60
msgLen = len(useMessage)

if msgLen <= 50:
    print('SMS 발송!')
else:
    print('MMS 발송!')

print(f'useMessage length: {msgLen}')

"""
위 코드 결과:
- useMessage = 'a' × 60 (a가 60개)
- msgLen = 60
- msgLen <= 50 = False이므로 'MMS 발송!'이 출력됨

=================================================
핵심 함수 및 키워드 총정리
=================================================

if              → 조건문 선언 ('만약 ~라면')
else            → 조건 불만족 시 실행 ('그렇지 않으면')
elif            → 다중 조건 검사 ('그게 아니라 만약 ~라면')
pass            → 실행문 없이 넘어갈 때 사용
중첩 if         → 조건문 안의 조건문
삼항 연산자     → if~else를 한 줄로 축약
리팩토링        → 기능 유지하면서 코드 품질 개선
datetime        → 오늘 날짜/시간 정보를 가져오는 모듈
random          → 무작위 숫자를 생성하는 모듈
len()           → 문자열 또는 자료형의 길이를 반환

=================================================
핵심 정리
=================================================

조건문(if문)은:
"특정 조건의 참(True) / 거짓(False)에 따라
 실행 흐름을 제어하는 구문"

실제 개발에서는:
- 로그인 성공 / 실패 처리
- 회원 등급별 혜택 부여
- 입력값 유효성 검사
- 게임 승패 판정
- 요금 및 할인 정책 적용

등 거의 모든 프로그램에서 조건문을 사용한다.
"""
