'''
flag = True

members = {}

while flag:
    selectedMenuNum = int(input('1. 회원가입     2. 프로그램 종료 '))

    if selectedMenuNum == 1:
        id = input('아이디: ')
        pw = input('비밀번호: ')
        members[id] = pw

    elif selectedMenuNum == 2:
        flag = False

        for key in members.keys():
            print(f'ID: {key}, PW: {members[key]}')


classes =  {'python':'5학점', 'C/C++':'5학점', 'HTML5':'3학점', 
            'Java':'5학점', 'Javascript':'3학점'}

for key in classes:
    if classes[key] == '3학점':
        classes[key] = '5학점'
print(classes)
'''

'''
members = {
    '2019-052001': ['박찬호', 25, 'M', '010-1234-5678', '헬스, 수영', 0],
    '2019-052004': ['박용택', 65, 'M', '010-9012-3456', '수영', 50],
    '2019-052003': ['박세리', 70, 'W', '010-7890-1234', '아쿠아로빅', 50]
}

# 전체 회원 정보 출력
for key in members:
    print(f'회원번호: {key}, 회원정보: {members[key]}')

print('-' * 30)

# 전체 회원 정보 출력을 하는데, 이때 회원의 '이름'과 '성별'만 출력을 하자!
for key, value in members.items():
    print(f'회원번호: {key}, 회원정보(이름, 성별): {value[0]}, {value[2]}')
'''
'''
members = {
    '2019-052001': {
        '이름': '박찬호',
        '나이': 25,
        '성별': 'M',
        '연락처': '010-1234-5678',
        '이용서비스': ['헬스', '수영'],
        '할인율': 0
    },
    '2019-052004': {
        '이름': '박용택',
        '나이': 65,
        '성별': 'M',
        '연락처': '010-9012-3456',
        '이용서비스': ['수영'],
        '할인율': 50
    },
    '2019-052003': {
        '이름': '박세리',
        '나이': 70,
        '성별': 'W',
        '연락처': '010-7890-1234',
        '이용서비스': ['아쿠아로빅'],
        '할인율': 50
    }
}

# 전체 회원 정보 출력
for key in members:
    print(f'회원번호: {key}, 회원정보: {members[key]}')

print('-' * 30)

# 전체 회원 정보 출력을 하는데, 이때 회원의 '이름'과 '성별'만 출력을 하자!
for key, value in members.items():
    print(f'회원번호: {key}, 회원정보(이름, 성별): {value['이름']}, {value['성별']}')

print('-' * 30)

# 전체 회원 정보 출력을 하는데, 이때 회원의 '이름', '성별', '이용서비스' 그리고 이용서비스개수 만 출력을 하자!
for key, value in members.items():
    print(f'회원번호: {key}, 회원정보(이름, 성별): {value['이름']}, {value['성별']}, {value['이용서비스']}, {len(value['이용서비스'])}')
'''

# 다음 내용에 맞춰 냉장고에 보관하고 있는 야채의 재고 관리 프로그램을 만드시오.
'''
1.  당근     10개가   입고
2.  건대추   100개    입고
3.  대파     20개     입고
4.  애호박   3개      입고
5.  부추     1개      입고
6.  당근     1개      소비
7.  건대추   10개     소비 
8.  대파     1개      소비
9.  애호박   1개      소비
10. 부추     1개      소비

***야채별 재고 출력해 보자.
'''
''''''

veges = {}

# 입고

veges = {
    '당근': 10,
    '건대추': 100,
    '대파': 20,
    '애호박': 3,
    '부추': 1
}

print(f'신규 입고 후 재고: {veges} ')


# 출고

veges = {
    '당근': veges['당근']-1,
    '건대추': veges['건대추']-10,
    '대파': veges['대파']-1,
    '애호박': veges['애호박']-1,
    '부추': veges['부추']-1
}

print(f'출고 후 재고: {veges} ')



'''
# 용돈 기입장을 만들어보자

# 용돈 기입장 프로그램

# =========================
# 용돈 기입장 딕셔너리 생성
# =========================

moneyBook = {}

# =========================
# 수입(Create)
# =========================

moneyBook['용돈'] = 50000
moneyBook['알바비'] = 120000
moneyBook['세뱃돈'] = 30000

# =========================
# 지출(Create)
# =========================

moneyBook['점심식사'] = -8000
moneyBook['카페'] = -5500
moneyBook['영화'] = -15000
moneyBook['교통비'] = -2500
moneyBook['문구점'] = -4000

# =========================
# 특정 항목 조회(Read)
# =========================

print('-' * 40)
print(f'용돈 금액: {moneyBook["용돈"]}원')
print(f'영화 지출: {moneyBook["영화"]}원')
print('-' * 40)

# =========================
# 수정(Update)
# =========================

# 카페 지출 수정
moneyBook['카페'] = -7000

print(f'수정된 카페 지출: {moneyBook["카페"]}원')

print('-' * 40)

# =========================
# 삭제(Delete)
# =========================

del moneyBook['문구점']

print('문구점 항목 삭제 완료')

print('-' * 40)

# =========================
# 전체 용돈 기입장 출력
# =========================

print('용돈 기입장 내역')
print('-' * 40)

for key, value in moneyBook.items():

    # 수입 / 지출 구분
    if value > 0:
        print(f'[수입] {key}: {value}원')

    else:
        print(f'[지출] {key}: {value}원')

print('-' * 40)

# =========================
# 총 수입 / 총 지출 계산
# =========================

totalIncome = 0
totalExpense = 0

for value in moneyBook.values():

    if value > 0:
        totalIncome += value

    else:
        totalExpense += value

# =========================
# 최종 결과 출력
# =========================

print(f'총 수입: {totalIncome}원')
print(f'총 지출: {totalExpense}원')
print(f'남은 금액: {totalIncome + totalExpense}원')

print('-' * 40)

# =========================
# 전체 항목 개수 출력
# =========================

print(f'전체 항목 개수: {len(moneyBook)}개')
'''

'''
----------------------------------------
용돈 금액: 50000원
영화 지출: -15000원
----------------------------------------
수정된 카페 지출: -7000원
----------------------------------------
문구점 항목 삭제 완료
----------------------------------------
용돈 기입장 내역
----------------------------------------
[수입] 용돈: 50000원
[수입] 알바비: 120000원
[수입] 세뱃돈: 30000원
[지출] 점심식사: -8000원
[지출] 카페: -7000원
[지출] 영화: -15000원
[지출] 교통비: -2500원
----------------------------------------
총 수입: 200000원
총 지출: -32500원
남은 금액: 167500원
----------------------------------------
전체 항목 개수: 7개
'''


#::::: 용돈 기입장 :::::
from datetime import datetime

MENU_INCOME     = 1
MENU_EXPENSE    = 2
MENU_VIEW       = 3
EXIT            = 99

flag = True
DEV_MOD = True

bankAccount = []
currentMoney = 0

if DEV_MOD:
    txt =  '[2026-05-15 15:14:08] \t 100 \t\t aaaaa \t\t 100'
    bankAccount.append(txt)
    txt = '[2026-05-15 15:15:08] \t 200 \t\t bbbbb \t\t 300'
    bankAccount.append(txt)
    txt = '[2026-05-15 15:16:08] \t\t -50 \t ccccc \t\t 250'
    bankAccount.append(txt)

while flag:

    selectedMenuNum = int(input('1.수입    2.지출    3.조회    99.시스템종료 -----> '))
    if selectedMenuNum == MENU_INCOME:
        incomeMoney = int(input('수입 금액: '))
        incomeDesc = input('수입 내용: ')
        currentMoney += incomeMoney

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        txt = f'[{now}] \t {incomeMoney} \t {incomeDesc} \t\t\t {currentMoney}'
        bankAccount.append(txt)

    elif selectedMenuNum == MENU_EXPENSE:
        expenseMoney = int(input('지출 금액: '))
        expenseDesc = input('지출 내용: ')
        currentMoney -= expenseMoney

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        txt = f'[{now}] \t\t\t -{expenseMoney} \t {expenseDesc} \t {currentMoney}'
        bankAccount.append(txt)

    elif selectedMenuNum == MENU_VIEW:
        print('-' * 63)
        print('날짜&시간 \t\t 입금 \t 출금 \t 내역 \t\t 잔액')
        print('-' * 63)
        for item in bankAccount:
            print(item)
        print('-' * 63)

    elif selectedMenuNum == EXIT:
        flag = False 

