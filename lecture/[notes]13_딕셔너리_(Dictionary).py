"""
딕셔너리 (Dictionary) 완전 정리
=================================================

딕셔너리란?
-------------------------------------------------
키(key)와 값(value)을 쌍으로 저장하는 자료형이다.

우리가 실생활에서 쓰는 사전(dictionary)을 생각하면 쉽다.
영어사전에서 'apple'이라는 단어(key)를 찾으면
'사과'라는 뜻(value)이 나오는 것처럼,
딕셔너리는 키로 값을 찾는다.

리스트와의 차이:
리스트 → 번호(인덱스)로 값을 찾는다.   fruits[0] → '사과'
딕셔너리 → 이름(키)으로 값을 찾는다.  student['name'] → '홍길동'
"""


"""
1. 딕셔너리 만들기
=================================================

형태:
변수 = { '키1': 값1, '키2': 값2, '키3': 값3 }

{ } 중괄호로 만든다.
키와 값은 콜론(:)으로 연결한다.
각 쌍은 쉼표(,)로 구분한다.

주의:
키(key)는 절대 중복되면 안 된다.
값(value)은 중복되어도 상관없다.
"""

# 예시 1: 학생 정보를 딕셔너리로 만들기
student = {
    'name': '홍길동',     # 키: 'name',  값: '홍길동'
    'age': 20,            # 키: 'age',   값: 20
    'score': 85           # 키: 'score', 값: 85
}

print(f'student: {student}')
print(f'student type: {type(student)}')

"""
출력 결과:
student: {'name': '홍길동', 'age': 20, 'score': 85}
student type: <class 'dict'>

왜 딕셔너리를 쓸까?
리스트로 학생 정보를 저장하면:
student = ['홍길동', 20, 85]
student[0] → '홍길동'  (0번이 이름인지 기억해야 함)
student[1] → 20        (1번이 나이인지 기억해야 함)

딕셔너리로 저장하면:
student = {'name': '홍길동', 'age': 20, 'score': 85}
student['name']  → '홍길동'  (키 이름으로 바로 이해 가능)
student['age']   → 20        (키 이름으로 바로 이해 가능)

코드를 읽는 사람이 훨씬 이해하기 쉽다.
"""


"""
2. 딕셔너리 값 조회 (꺼내기)
=================================================

딕셔너리[키] 형태로 값을 꺼낸다.
"""

student = {
    'name': '홍길동',
    'age': 20,
    'score': 85
}

# 키로 값 꺼내기
print(f'이름: {student["name"]}')
print(f'나이: {student["age"]}')
print(f'점수: {student["score"]}')

"""
출력 결과:
이름: 홍길동
나이: 20
점수: 85

주의:
없는 키로 접근하면 오류가 발생한다.
student['grade']  ← 'grade' 키가 없으므로 오류!
"""


"""
3. 딕셔너리 추가 / 수정
=================================================

딕셔너리[키] = 값

키가 없으면 → 새로 추가된다.
키가 있으면 → 기존 값이 수정된다.
"""

student = {
    'name': '홍길동',
    'age': 20,
    'score': 85
}

# 새로운 키-값 추가 ('city' 키가 없으므로 추가됨)
student['city'] = '서울'
print(f'추가 후: {student}')

# 기존 값 수정 ('score' 키가 이미 있으므로 값이 바뀜)
student['score'] = 99
print(f'수정 후: {student}')

"""
출력 결과:
추가 후: {'name': '홍길동', 'age': 20, 'score': 85, 'city': '서울'}
수정 후: {'name': '홍길동', 'age': 20, 'score': 99, 'city': '서울'}
"""


"""
4. 딕셔너리 순회 (전체 돌기)
=================================================

딕셔너리의 모든 키-값 쌍을 하나씩 꺼내서 사용할 때
for문과 items()를 함께 사용한다.

items()는 키와 값을 동시에 꺼내준다.
"""

ages = {
    '박찬호': 48,
    '박지성': 40,
    '박세리': 50,
    '이승엽': 43
}

# 방법 1: 키만 순회
print('=== 방법 1: 키만 순회 ===')
for key in ages:
    print(f'{key}: {ages[key]}')

"""
출력 결과:
박찬호: 48
박지성: 40
박세리: 50
이승엽: 43

for key in ages 는
ages 딕셔너리에서 키를 하나씩 꺼낸다는 뜻이다.
ages[key]로 해당 키의 값을 꺼낸다.
"""

# 방법 2: 키와 값을 동시에 순회 (더 깔끔)
print('\n=== 방법 2: 키와 값 동시 순회 ===')
for key, value in ages.items():
    print(f'{key}: {value}')

"""
출력 결과:
박찬호: 48
박지성: 40
박세리: 50
이승엽: 43

for key, value in ages.items() 는
ages 딕셔너리에서 키와 값을 동시에 꺼낸다는 뜻이다.
방법 1보다 이 방법이 더 자주 쓰인다.
"""


"""
5. 딕셔너리 + 조건문 활용
=================================================

딕셔너리를 순회하면서 특정 조건에 맞는 데이터만 출력할 수 있다.
"""

scores = {
    'c/c++': 'A',
    'java': 'B+',
    '네트워킹': 'C',
    '보안': 'A+',
    '해킹': 'F',
    '시스템': 'C+'
}

print('=== 전체 성적 ===')
for subject, grade in scores.items():
    print(f'{subject}: {grade}')

"""
출력 결과:
=== 전체 성적 ===
c/c++: A
java: B+
네트워킹: C
보안: A+
해킹: F
시스템: C+
"""

print('\n=== F학점 과목 ===')
for subject, grade in scores.items():
    if grade == 'F':
        print(f'{subject}: {grade}')

"""
출력 결과:
=== F학점 과목 ===
해킹: F

딕셔너리를 순회하면서 if문으로 조건에 맞는 것만 출력한다.
리스트와 동일한 방식으로 필터링할 수 있다.
"""


"""
6. 딕셔너리로 누적 계산하기
=================================================

딕셔너리를 순회하면서 값들을 더하거나 곱할 수 있다.
"""

studentScores = {
    '수학': 90,
    '영어': 85,
    '과학': 95
}

# 합계와 평균 구하기
total = 0
for subject, score in studentScores.items():
    total += score                           # 순회하면서 점수를 계속 더한다

average = total / len(studentScores)         # len()으로 과목 수를 구한다

print(f'합계: {total}점')
print(f'평균: {average:.1f}점')

"""
출력 결과:
합계: 270점
평균: 90.0점

total = 0 으로 시작해서
순회할 때마다 total += score 로 점수를 계속 더한다.
마지막에 과목 수(len)로 나누면 평균이 나온다.
"""


"""
7. 딕셔너리로 최고/최저 찾기
=================================================

딕셔너리를 순회하면서 가장 크거나 작은 값을 찾을 수 있다.
"""

students = {
    '박찬호': 88,
    '이승엽': 72,
    '박세리': 95,
    '박지성': 63,
    '손흥민': 91
}

# 최고 점수 학생 찾기
maxName = ''      # 최고 점수 학생 이름을 저장할 변수
maxScore = 0      # 최고 점수를 저장할 변수 (0부터 시작)

for name, score in students.items():
    if score > maxScore:      # 현재 점수가 저장된 최고 점수보다 크면
        maxScore = score      # 최고 점수를 바꾼다
        maxName = name        # 최고 점수 학생 이름도 바꾼다

print(f'최고 점수: {maxName} ({maxScore}점)')

"""
출력 결과:
최고 점수: 박세리 (95점)

동작 원리:
처음에 maxScore = 0 으로 시작한다.

첫 번째 반복: 박찬호(88) > 0  → maxScore = 88, maxName = '박찬호'
두 번째 반복: 이승엽(72) > 88 → 아니므로 넘어감
세 번째 반복: 박세리(95) > 88 → maxScore = 95, maxName = '박세리'
네 번째 반복: 박지성(63) > 95 → 아니므로 넘어감
다섯 번째 반복: 손흥민(91) > 95 → 아니므로 넘어감

최종 결과: 박세리 (95점)
"""


"""
8. 딕셔너리 값 수정하기 (실전 예제)
=================================================

과자 구매 프로그램:
딕셔너리의 값을 직접 수정해서 재고를 관리한다.
"""

goods = {
    '새우깡': 1200,
    '비비빅': 400,
    '초코파이': 500,
    '맛동산': 1500
}

goodsTotalPrice = 0

def shrimpCrackerPrice():
    global goodsTotalPrice
    goodsTotalPrice += goods['새우깡'] * shrimpCrackers
    print(f'새우깡 구매 금액: {goods["새우깡"] * shrimpCrackers}원')

def bibibigPrice():
    global goodsTotalPrice
    goodsTotalPrice += goods['비비빅'] * bibibigs
    print(f'비비빅 구매 금액: {goods["비비빅"] * bibibigs}원')

def chocopiePrice():
    global goodsTotalPrice
    goodsTotalPrice += goods['초코파이'] * chocopies
    print(f'초코파이 구매 금액: {goods["초코파이"] * chocopies}원')

def matdongsanPrice():
    global goodsTotalPrice
    goodsTotalPrice += goods['맛동산'] * matdongsans
    print(f'맛동산 구매 금액: {goods["맛동산"] * matdongsans}원')

shrimpCrackers = int(input('새우깡 구매 개수: '))
bibibigs = int(input('비비빅 구매 개수: '))
chocopies = int(input('초코파이 구매 개수: '))
matdongsans = int(input('맛동산 구매 개수: '))

print(f'새우깡 구매 개수: {shrimpCrackers}')
print(f'비비빅 구매 개수: {bibibigs}')
print(f'초코파이 구매 개수: {chocopies}')
print(f'맛동산 구매 개수: {matdongsans}')

print('=' * 40)

shrimpCrackerPrice()
bibibigPrice()
chocopiePrice()
matdongsanPrice()

print('=' * 40)
print(f'총 구매 금액: {goodsTotalPrice}원')

"""
출력 결과 (1, 2, 1, 1 입력 시):
새우깡 구매 개수: 1
비비빅 구매 개수: 2
초코파이 구매 개수: 1
맛동산 구매 개수: 1
========================================
새우깡 구매 금액: 1200원
비비빅 구매 금액: 800원
초코파이 구매 금액: 500원
맛동산 구매 금액: 1500원
========================================
총 구매 금액: 4000원

동작 원리:
goods['새우깡'] → 1200 (새우깡 한 개 가격)
1200 * shrimpCrackers → 새우깡 총 가격
goodsTotalPrice += 새우깡 총 가격 → 전체 합계에 더한다

global goodsTotalPrice 를 쓰는 이유:
goodsTotalPrice 는 함수 밖에서 선언한 변수다.
함수 안에서 이 변수를 수정하려면
반드시 global 키워드를 써야 한다.
안 쓰면 함수 안에서만 쓰는 새로운 변수로 인식한다.
"""


"""
=================================================
딕셔너리 핵심 정리
=================================================

① 만들기
   변수 = {'키1': 값1, '키2': 값2}

② 값 꺼내기
   변수['키']

③ 추가/수정
   변수['키'] = 값    ← 키가 없으면 추가, 있으면 수정

④ 전체 순회
   for key, value in 변수.items():

⑤ 조건 필터링
   for key, value in 변수.items():
       if 조건:
           출력

⑥ 누적 계산
   total = 0
   for key, value in 변수.items():
       total += value
   average = total / len(변수)

⑦ 최고/최저 찾기
   maxScore = 0
   for key, value in 변수.items():
       if value > maxScore:
           maxScore = value

⑧ 주의사항
   키는 중복 불가
   없는 키로 접근하면 오류 발생
   함수 안에서 전역 변수 수정 시 global 키워드 필요
"""
