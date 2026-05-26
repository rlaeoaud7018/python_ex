# 산술 연산자
# 산술 연산자는 우리가 자주 사용하는 사칙 연산자와
# 컴퓨터 프로그램에서만 사용하는 나머지, 몫, 지수 연산자를 뜻 합니다.
# 사칙 연산자 : +, -, *, /
# %(나머지), //(몫), **(지수)


# 덧셈 연산자(+)
print(10 + 20)  # 30
print(3.14 + 5) # 8.14
num1 = 10; num2 = 100
print(num1 + num2)  # 110

                               
num = 1
num = num + 10
num += 10
print(num)

num -= 10
print(num)


# # quiz) DW 전자 회사에서 1분기 매출의 총합을 구하고자 합니다. 프로그램을 작성해봅시다.
# sales1 = int(input('1월 매출: '))
# sales2 = int(input('2월 매출: '))
# sales3 = int(input('3월 매출: '))
# total = sales1 + sales2 + sales3
# print(f'1분기 매출: {total:,}원')  # 1분기 매출: 300,000원

# # 문자열 덧셈
# print('a' + 'b')  # ab 덧셈(연결) 연산자

# # 문자열 + 숫자 > TypeError 
# print('hello' + 3)  # TypeError


# # 뺄셈 연산자(-)
# print(10 - 5)  # 5
# print(3.14 - 0.1)  # 3.04

# print('hello' - 10)  # TypeError


# quiz) DW 전자에서 1분기 수익을 계산하려고 합니다.
# 사용자가 1분기 매출액과 매입액을 입력하면
# 수익을 계산해주는 프로그램을 만들어봅시다.

sales = int(input('1분기 매출: '))         # 매출 입력
purchase = int(input('1분기 매입: '))      # 매입 입력
profit = sales - purchase                 # 수익 계산
print(f'수익: {profit:,}원')               # 수익: 0원


# 곱셈(*) 연산자
print(10 * 20)  # 200
print(3.14 * 3)  # 9.42

# 문자열 곱셈
print('hello' * 3)  # hellohellohello

str = 'hello '
print(str * 3)  # hello hello hello


# quiz) 가로, 세로 길이를 입력하면
# 방의 넓이를 계산해주는 프로그램을 만들어봅시다.
width = int(input('가로 입력: '))
height = int(input('세로 입력: '))
area = width * height
print(f'방의 넓이: {area}㎡')


# quiz) 'Good morning' 문자열을 사용자가 입력한 숫자만큼 출력하는 프로그램을 만들어봅시다.
intro = 'Good morning '
cnt = int(input('출력을 원하는 횟수를 입력하세요.'))
print(intro * cnt)



# 비교형 연산자는 Boolean 값이 나온다.
10 == 10  # True
10 != 10  # False 

