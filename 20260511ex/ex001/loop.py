# 반복문(for문 & while문)
# for문 횟수만큼 반복, while문은 조건이 충족되는 한 반복

# for 문: ~ 하는 동안 ==> 회수에 의한 반복
'''
for 변수 in 범위: 
    실행구문

for~in 키워드   iterable(반복 가능한 객체)
  for i in 
    print(i)
     실행문
'''
'''
for 변수 in range(시작값, 끝값+1, 단계):
    print()
'''


# 1 ~ 10까지의 정수를 출력하자(1,3,5,7,9)
# 1 ~ n까지의 정수 range(1, (n+1), 1)
'''
for 변수 in range(1, 11, 1):
    print('hello')

for num in range(1, 11, 1):
    print(f'num : {'hello'}')

# range() 간략화 - 단계가 1인 경우 단계를 생략할 수 있다.(1만 가능)
for num in range(0, 11):
    print(f'num : {num}')

# range() 간략화 - 단계 생략된 상태에서 시작이 0이면 시작도 생략 가능하다.
for num in range(11):
    print(f'num : {num}')

# quiz) 2~8 사이의 짝수 출력하기
for i in range(2, 9, 2):
    print(f'num: {num}')

for num in range(1, 16):  # 2~8 사이만 출력하자
    if (num % 2) == 0 and (num < 8):
        print(f'num : {num}')

# quiz) 사용자가 입력한 횟수만큼 '메일 발송!' 문자열 출력하기
num = int(input('횟수를 입력하세요: '))
for num in range(num):
    print(f'{num}: 메일 발송!')


# 1~10 사이의 정수를 출력화되, 정수가 3의 배수이면 '3의 배수!' 출력하기
for num in range(1,11):
    if num % 3 == 0:
        print('3의 배수!')
    else:
        print(num)

for num in range(1,11):
    print(f"{'3의 배수' if num % 3 == 0 else num}")

# 사용자가 원하는 구구단을 입력하면 해당 구구단을 출력하자!
num = int(input('구구단을 입력하세요: '))
for num in range (num * 1, num * 10, num):
    print(f'num : {num}')

# ==> 수정

num = int(input('원하는 구구단을 입력하세요: '))
for mul in range(1,11):
    print(f'{num} X {mul} = {num * mul}')

googoo = int(input('원하는 구구단의 숫자를 입력하세요 :'))
print(f'---{googoo}단 출력 ---')
for num in range(1,10):
    print(f' {googoo} X {num} = {googoo * num }')

multiplication = int(input('원하는 구구단을 입력하세요.'))
for num in range(1,11):
    print(f'{multiplication} * {num} = {multiplication*num}')
'''
'''
# quiz) 1~10까지 정수의 합 출력하기

total = 0
for num in range(1,11):
    total += num
print(total)

userInputInteger = int(input('정수 입력: '))

total = 0
for num in range(1, userInputInteger + 1):
    sum += 1

print(f'1부터 10까지의 합:', sum)

sum = 0
for i in range(1, 11):
    sum += i
print("1부터 10까지의 합:", sum)


print(sum(range(1,11)))

# quiz) for문을 이용해서 1~100까지 정수 중에서
# 3과 7의 공배수와 최소 공배수를 출력하시오.

minimum =100

for num in range(1, 101):
    if (num % 3 == 0) and (num % 7 == 0):
        minimum = num if num < minimum else minimum
        print(f'3과 7의 공배수 : {num}')

for num in range(1, 101):
    if (num % 3 == 0) and (num % 7 == 0):
        if minNum == 0: minNum = num
    
print(f'3과 7의 공배수 : {num}')

minimum = 100

for num in range(1, 101):
    if (num % 3 == 0) and (num % 7 == 0):
        minimum = num if num < minimum else minimum
        print(num)

print(f'최소공배수: {minimum}')


first = True
for i in range(1, 101):
    if i % 3 == 0 and i % 7 == 0 and first == True:
        print(f'{i}는 3과 7의 최소공배수입니다.')
        first = False
    elif i % 3 == 0 and i % 7 == 0 :
        print(f'{i}는 3과 7의 공배수입니다.')
'''

# range() 함수란?
'''
지금까지 이터러블에 range() 함수를 이용한 예를 살펴봤습니다.
그런데 이터러블에는 다음과 같은 문자열도 이용할 수 있습니다.

for ch in 'hello':
    print(f'ch: {ch}')

# 50보다 작은 7의 배수를 출력하는 프로그램을 만드시오.
for num in range(1, 51):
    if num % 7 ==0:
            print(f'num: {num}')
'''

# while 문: ~ 하는 동안 ==> 조건에 의한 반복
'''
num = 1   # while문의 시작, 무적권 써야함

while num < 5:    # num이 5보다 작다면
    print(num)    # 여기까지만 조건이 반복되면 무한 루프
    num += 1      # num 값에 1을 더한 후 그 결과를 다시 num에 저장해야 루프가 완성


num = 1 

while num < 10:
    print('num: ', num) 
    num += 1

num = 1

while num <= 10:
    print(f'num: {num}')
    num += 2


# quiz) 1~30까지의 정수 중 홀수와 짝수를 구분하여 출력하기

num = 1

while num <= 30:
    if num % 2 == 0 and num > 0:
        print(f'{num}: 짝수')
    else:
        print(f'{num}: 홀수')
    num += 1

# quiz) 구구단 3단 출력하기 by while문


num = 1

while num <= 9:
    print(f'3 x {num} = {3 * num}')
    num += 1
'''

'''
timesTables = int(input('구구단 숫자를 입력하세요.'))
num = 1
while num < 10:
    print(f'{timesTables} x {num} = {timesTables * num}')
    num += 1
'''

# quiz) 구구단 전체(2단,3단,4단...9단) 출력하자
'''
dan = 2
while dan <= 9:
    print(f'---{dan}단---')
    num = 1
    while num <= 9:
        print(f'{dan} x {num} = {dan * num}')
        num += 1
    dan += 1


mul = 2                                         # 단수 지정
while mul < 10:                                 # 단수 한계 지정(9단까지)
    print('{mul}단')                             # 단 표시
    num = 1                                     # 단에 곱할 숫자의 기준
    while num < 10:                              # 곱할 숫자의 한계 지정(9까지)
        print(f'{mul} X {num} = {mul * num}')   # 단수 x 곱할 숫자 = 단수*곱하기
        num += 1                                # 곱하기 숫자는 1씩 더해서 계산할 것
    mul += 1                                    # 단수는 1씩 더해서 계산할 것
'''

'''
# quiz) 구구단 전체를 각 단마다 가로로 출력하자
dan = 2
while dan <= 9:
    print(f'---{dan}단---')
    num = 1
    while num <= 9:
        print(f'{dan} x {num} = {dan * num:2}', end=' ')
        num += 1
    print()
    dan += 1

# result
# ---2단---
# 2 x 1 =  2 2 x 2 =  4 2 x 3 =  6 2 x 4 =  8 2 x 5 = 10 2 x 6 = 12 2 x 7 = 14 2 x 8 = 16 2 x 9 = 18 

num = 1

while num <= 9:
    dan = 2

    while dan <= 9:
        print(f'{dan} x {num} = {dan * num:2}', end='   ')
        dan += 1

    print()
    num += 1

# result
# 2 x 1 =  2   3 x 1 =  3   4 x 1 =  4   5 x 1 =  5   6 x 1 =  6   7 x 1 =  7   8 x 1 =  8   9 x 1 =  9   


num1 = 1                                              # 곱할 숫자

while num1 < 10:                                      # 10이하로

    num2 = 2                                          # 단으로 표시할 숫자
    str = ' '                                         
    while num2 < 10:                                  # 10보다 작음 = 9단까지
        str += f'{num2} X {num1} = {num2 * num1}\t'
        num2 += 1                                     # 2+1=3+1=4+1 연속

    print(str)
    num1 += 1
'''

# quiz) while문과 if문을 이용해서 0~100까지 정수 중 3과 8의 공배수와 최소공배수 출력하기
'''
num = 1                                        # 반복문의 시작(초기값)
minNum = 0                                     # 최소공배수

while num < 101:
    if num % 3 == 0 and num % 8 == 0:
        print(f'3과 8의 공배수 : {num}')         # 공배수 출력
        if minNum == 0:                        # 아직 최소공배수를 저장하지 않았니?
            minNum = num                       # 최초로 발견한 공배수 한 번만 저장해라

    num += 1

print(f'최소공배수 : {minNum}')


if minNum == 0:
   minNum = num

이 코드는 최소공배수를 한 번만 저장하기 위한 조건문이다. 
처음에는 minNum을 0으로 설정해 “아직 최소공배수를 저장하지 않았다”는 의미로 사용한다. 
반복문이 작은 숫자부터 차례대로 검사하다가 처음으로 3과 8의 공배수를 발견하면, 
minNum == 0 조건이 참(True)이 되어 현재 공배수인 num 값을 minNum에 저장한다. 
이후에는 minNum 값이 이미 24처럼 바뀌어 있으므로 조건이 거짓(False)이 되어 
더 큰 공배수(48, 72, 96 등)는 저장하지 않는다. 따라서 가장 먼저 발견된 공배수인 
24가 최종적으로 최소공배수로 남게 된다.
'''
'''
# 반복문 내 실행 제어(continue, break)

# continue:
# 반복문에 continue 키워드를 사용하면 이후 실행을 생략하고 다시 반복문의 처음으로 돌아갑니다.

# continue를 이용해서 1부터 10까지의 정수 중 홀수만 출력하는 프로그램을 만들어 봅시다.

for num in range(1,11):
    if num % 2 == 0:            # 정수를 2로 나눴을 때 0이 남으면 짝수, 홀수는 1이 남았을때
        continue
    print(f'num: {num}')

# continue 횟수를 지정하려면 따로 명령문을 넣어줘야함!

count = 1
for num in range(10):
    print(f'num: {num}')
    count += 1
    if count >= 5:
        break
    

# break:
# 반복문에서 break 키워드를 만나면 '실행을 중단하고 반복문을 빠져'나옵니다.

for num in range(1,11):
    if num % 2 == 0:            # 정수를 2로 나눴을 때 0이 남으면 짝수, 홀수는 1이 남았을때
        break
    print(f'num: {num}')


# 1 부터 10까지의 정수를 더하되, 결과가 30이상이 될 때 정수를 찾는 프로그램을 만들어 봅시다.

num = 1
sum = 0

while num < 11:
    sum += num
    if sum>= 30:
        print(f'num: {num}')
        break
    num += 1

'''
# ----------이런게 있다--------------
# for ~ else 키워드
# for문에 else 키워드를 사용하는 경우, else 이하의 구문은 for문의 반복 업무를 모두 완료하고 난 후 실행됩니다.

# 1부터 5까지 정수를 출력하고 반복문이 끝나면 완료 메세지를 출력하자!
'''
for num in range(1, 6):
    print(f'num: {num}')
else:
    print('완료')
'''
# ----------이런게 있다--------------

# pass 키워드
# for num in range(1, 10):
#     pass

# quiz)
'''
삼각형의 넓이 구하기
가로와 세로 길이의 변화에 따른 삼각형의 넓이를 구하는 프로그램을 만들어 보자.
단, 가로 길이는 1부터 2의 배수로 증가하고
세로 길이는 1부터 3의 배수로 증가하며,
삼각형의 넓이가 150보다 크면 프로그램을 종료한다.


count = 1
maxArea = 150

while True:
    result = ((count * 2) * (count * 3)) / 2
    if result > 150: break
    print(f'삼각형의 넓이는: {result}')
    count += 1

'''