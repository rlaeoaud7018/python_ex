# 비교 연산자
'''
a == b : a와 b가 같다. => True or False
a != b : a와 b가 같지 않다. => True or False
a > b : a가 b보다 크다. => True or False
a < b : a가 b보다 작다. => True or False
a >= b : a가 b보다 크거나 같다. => True or False
a <= b : a가 b보다 작거나 같다. => True or False
'''

num1 = 10; num2 = 20

print(num1 == num2)  # False
print(num1 != num2)  # True
print(num1 > num2)   # False
print(num1 < num2)   # True
print(num1 >= num2)  # False
print(num1 <= num2)  # True

# quiz) 범퍼카 탑승 가능 판별하기
'''
DW 놀이동산에서 범퍼카는 신장이 120cm 이상인 어린이만 탑승할 수 있습니다.
사용자가 신장을 입력하면 범퍼카 탑승 가능 여부를 출력하는 프로그램을 만들어봅시다.
True: 탑승 가능, False: 탑승 불가능
'''
height = int(input('어린이의 신장을 입력하세요. '))
print(height >= 120)  # True 또는 False가 출력됨

# 문자 vs 문자 비교 => 아스키코드
print('a' == 'b')   # False  97 == 98
print('a' < 'b')   # True  97 < 98
print('a' > 'b')   # False  97 > 98

# 문자열 비교
str1 = 'hello'
str2 = 'hello'
print(str1 == str2)  # True
print(str1 < str2)   # False
print(str1 > str2)   # False

str1 = 'z'
str2 = 'X'
str1 >= str2 # True 122 >= 88