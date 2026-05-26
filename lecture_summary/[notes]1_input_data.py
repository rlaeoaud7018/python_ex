"""
데이터 입력(input data) 완전 정리
=================================================

1. input() 함수란?
-------------------------------------------------
input() 함수는 외부에서 데이터를 받아오는 함수이다.

형태:
변수 = input()

또는

변수 = input('프롬프트 메시지')

프롬프트 메시지: 사용자에게 어떤 데이터를 입력할지 알려주는 메시지
"""

print('데이터를 입력하세요.')
inputData = input()

print(f'inputData: {inputData}')
print(f'type of inputData: {type(inputData)}')

"""
위 코드 결과 (사용자가 'hello' 입력했을 경우):
inputData: hello
type of inputData: <class 'str'>

input() 함수는 모든 데이터를 문자열(str)로 취급한다.


2. 정수 입력받기
-------------------------------------------------
사용자가 정수를 입력하면 어떤 자료형으로 받아지는가?
"""

print('정수를 입력하세요.')
inputInteger = input()

print(f'inputInteger: {inputInteger}')
print(f'type of inputInteger: {type(inputInteger)}')

"""
위 코드 결과 (사용자가 6 입력했을 경우):
inputInteger: 6
type of inputInteger: <class 'str'>

사용자가 정수 6을 입력했지만,
input() 함수는 이를 문자열 '6'으로 받아온다.


3. 실수 입력받기
-------------------------------------------------
사용자가 실수를 입력하면 어떤 자료형으로 받아지는가?
"""

print('실수를 입력하세요.')
inputFloat = input()

print(f'inputFloat: {inputFloat}')
print(f'type of inputFloat: {type(inputFloat)}')

"""
위 코드 결과 (사용자가 3.14 입력했을 경우):
inputFloat: 3.14
type of inputFloat: <class 'str'>

사용자가 실수 3.14를 입력했지만,
input() 함수는 이를 문자열 '3.14'로 받아온다.


4. 논리형 데이터 입력받기
-------------------------------------------------
사용자가 논리형 데이터를 입력하면 어떤 자료형으로 받아지는가?
"""

print('논리형 데이터를 입력하세요.')
inputBoolean = input()

print(f'inputBoolean: {inputBoolean}')
print(f'type of inputBoolean: {type(inputBoolean)}')

"""
위 코드 결과 (사용자가 True 입력했을 경우):
inputBoolean: True
type of inputBoolean: <class 'str'>

사용자가 True를 입력했지만,
input() 함수는 이를 문자열 'True'로 받아온다.

핵심:
input() 함수는 어떤 형태의 데이터를 입력하든 모두 문자열(str)로 받아온다!


5. input() 함수에 프롬프트 메시지 포함하기
-------------------------------------------------
input() 함수에 프롬프트 메시지를 포함하면,
사용자 입력 전에 메시지가 출력된다.
"""

userInputData = input('사용자여~~~~ 정수를 입력해라!')

print(f'userInputData: {userInputData}')
print(f'type of userInputData: {type(userInputData)}')

"""
위 코드 결과 (사용자가 10 입력했을 경우):
사용자여~~~~ 정수를 입력해라!10
userInputData: 10
type of userInputData: <class 'str'>

input() 함수에 메시지를 넣으면 print() 함수를 따로 쓸 필요가 없다.


6. 데이터 타입 변환(Type Casting)
-------------------------------------------------
input() 함수로 받은 문자열 데이터를 다른 자료형으로 변환해야 할 때가 있다.

비유:
- 원래 형태: 종이에 적힌 숫자 '10'
- 타입 변환: 실제 숫자값 10으로 변환

형태:
새로운변수 = int(문자열)      # 정수로 변환
새로운변수 = float(문자열)    # 실수로 변환
새로운변수 = bool(문자열)     # 논리형으로 변환
새로운변수 = str(정수)        # 문자열로 변환
"""

userInputData = input('정수를 입력하세요: ')

print(f'변환 전:')
print(f'userInputData: {userInputData}')
print(f'type of userInputData: {type(userInputData)}')

userInputData = int(userInputData)

print(f'변환 후:')
print(f'userInputData: {userInputData}')
print(f'type of userInputData: {type(userInputData)}')

"""
위 코드 결과 (사용자가 10 입력했을 경우):
변환 전:
userInputData: 10
type of userInputData: <class 'str'>
변환 후:
userInputData: 10
type of userInputData: <class 'int'>

문자열 '10'이 정수 10으로 변환되었다.


7. 문자열을 실수로 변환
-------------------------------------------------
"""

userInputData = input('실수를 입력하세요: ')

print(f'변환 전:')
print(f'userInputData: {userInputData}')
print(f'type of userInputData: {type(userInputData)}')

userInputData = float(userInputData)

print(f'변환 후:')
print(f'userInputData: {userInputData}')
print(f'type of userInputData: {type(userInputData)}')

"""
위 코드 결과 (사용자가 3.14 입력했을 경우):
변환 전:
userInputData: 3.14
type of userInputData: <class 'str'>
변환 후:
userInputData: 3.14
type of userInputData: <class 'float'>

문자열 '3.14'가 실수 3.14로 변환되었다.


8. 문자열을 논리형으로 변환
-------------------------------------------------
"""

userInputData = 'True'

print(f'변환 전:')
print(f'userInputData: {userInputData}')
print(f'type of userInputData: {type(userInputData)}')

userInputData = bool(userInputData)

print(f'변환 후:')
print(f'userInputData: {userInputData}')
print(f'type of userInputData: {type(userInputData)}')

"""
위 코드 결과:
변환 전:
userInputData: True
type of userInputData: <class 'str'>
변환 후:
userInputData: True
type of userInputData: <class 'bool'>

주의:
bool() 함수는 특이하게 동작한다.
- 빈 문자열 '' → False
- 빈 문자열이 아닌 모든 문자열 → True
- 0 → False
- 0이 아닌 모든 숫자 → True


9. 실수를 정수로 변환
-------------------------------------------------
"""

x = 3.141592

print(f'변환 전:')
print(f'x: {x}')
print(f'type of x: {type(x)}')

y = int(x)

print(f'변환 후:')
print(f'y: {y}')
print(f'type of y: {type(y)}')

"""
위 코드 결과:
변환 전:
x: 3.141592
type of x: <class 'float'>
변환 후:
y: 3
type of y: <class 'int'>

주의:
int() 함수는 소수점 이하를 버린다.
반올림하지 않고 내림(floor)을 한다.


10. 정수를 실수로 변환
-------------------------------------------------
"""

y = 3

print(f'변환 전:')
print(f'y: {y}')
print(f'type of y: {type(y)}')

z = float(y)

print(f'변환 후:')
print(f'z: {z}')
print(f'type of z: {type(z)}')

"""
위 코드 결과:
변환 전:
y: 3
type of y: <class 'int'>
변환 후:
z: 3.0
type of z: <class 'float'>

정수 3이 실수 3.0으로 변환되었다.


11. 입력받은 데이터로 계산하기
-------------------------------------------------
사용자로부터 정수를 입력받아 계산하는 프로그램
"""

num1 = int(input('첫 번째 정수를 입력하세요: '))
num2 = int(input('두 번째 정수를 입력하세요: '))

sum_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2

print(f'num1: {num1}, num2: {num2}')
print(f'덧셈: {sum_result}')
print(f'뺄셈: {sub_result}')
print(f'곱셈: {mul_result}')
print(f'나눗셈: {div_result}')

"""
위 코드 결과 (사용자가 10, 3 입력했을 경우):
첫 번째 정수를 입력하세요: 10
두 번째 정수를 입력하세요: 3
num1: 10, num2: 3
덧셈: 13
뺄셈: 7
곱셈: 30
나눗셈: 3.3333333333333335

int() 함수로 형변환했기 때문에 정수로 계산된다.


12. 입력받은 실수 데이터로 계산하기
-------------------------------------------------
"""

height = float(input('키를 입력하세요(cm): '))
weight = float(input('몸무게를 입력하세요(kg): '))

bmi = weight / ((height / 100) ** 2)

print(f'키: {height} cm')
print(f'몸무게: {weight} kg')
print(f'BMI: {bmi:.2f}')

"""
위 코드 결과 (사용자가 170, 65 입력했을 경우):
키: 170.0 cm
몸무게: 65.0 kg
BMI: 22.49

float() 함수로 형변환했기 때문에 실수로 계산된다.


13. 여러 데이터를 한 줄에 입력받기
-------------------------------------------------
split() 메서드를 사용하면 여러 데이터를 한 줄에 입력받을 수 있다.
"""

data = input('두 개의 정수를 입력하세요(공백으로 구분): ')

num1, num2 = data.split()

print(f'data: {data}')
print(f'num1: {num1}')
print(f'num2: {num2}')
print(f'type of num1: {type(num1)}')
print(f'type of num2: {type(num2)}')

"""
위 코드 결과 (사용자가 '10 20' 입력했을 경우):
data: 10 20
num1: 10
num2: 20
type of num1: <class 'str'>
type of num2: <class 'str'>

split()은 공백을 기준으로 문자열을 나누어 리스트로 반환한다.
하지만 여전히 문자열이므로 정수로 변환해야 한다.


14. split()과 int() 함께 사용하기
-------------------------------------------------
"""

num1, num2 = map(int, input('두 개의 정수를 입력하세요(공백으로 구분): ').split())

sum_result = num1 + num2

print(f'num1: {num1}, num2: {num2}')
print(f'합계: {sum_result}')
print(f'type of num1: {type(num1)}')
print(f'type of num2: {type(num2)}')

"""
위 코드 결과 (사용자가 '10 20' 입력했을 경우):
num1: 10, num2: 20
합계: 30
type of num1: <class 'int'>
type of num2: <class 'int'>

map(int, ...) 을 사용하면 split()으로 나뉜 모든 문자열을 정수로 변환한다.


15. 데이터 타입 변환 주의사항
-------------------------------------------------
"""

# 정상 변환
validData = '123'
result = int(validData)

print(f'validData: {validData}')
print(f'result: {result}')
print(f'type of result: {type(result)}')

"""
위 코드 결과:
validData: 123
result: 123
type of result: <class 'int'>

숫자 형태의 문자열은 정수로 변환된다.
"""

# 오류 발생
invalidData = 'abc'

try:
    result = int(invalidData)
except ValueError:
    print('오류: 숫자 형태가 아닌 문자열은 정수로 변환할 수 없습니다!')

"""
위 코드 결과:
오류: 숫자 형태가 아닌 문자열은 정수로 변환할 수 없습니다!

숫자 형태가 아닌 문자열(예: 'abc')을 정수로 변환하려면 오류가 발생한다.
따라서 사용자 입력을 처리할 때는 항상 예외 처리를 해야 한다.


=================================================
핵심 함수 및 키워드 총정리
=================================================

input()         → 사용자로부터 데이터를 입력받는 함수
int()           → 문자열을 정수로 변환
float()         → 문자열을 실수로 변환
bool()          → 문자열 또는 값을 논리형으로 변환
str()           → 정수, 실수 등을 문자열로 변환
split()         → 문자열을 공백 기준으로 나누기
map()           → 함수를 iterable의 모든 항목에 적용
type()          → 데이터의 자료형을 확인
type casting    → 데이터 타입 변환
프롬프트 메시지  → input() 함수 내에 포함되는 안내 메시지


=================================================
핵심 정리
=================================================

input() 함수는:
"사용자로부터 모든 데이터를 문자열(str) 형태로 받아오는 함수"

반드시 기억할 점:
1. input()으로 받은 모든 데이터는 문자열이다
2. 정수, 실수로 계산하려면 int(), float()로 변환해야 한다
3. 타입 변환 시 형태가 맞지 않으면 오류가 발생한다
4. split()과 map()을 함께 사용하면 여러 데이터를 효율적으로 처리할 수 있다

실제 개발에서는:
- 회원가입 폼에서 사용자 정보 입력받기
- 설문조사 데이터 수집하기
- 게임에서 플레이어의 선택 입력받기
- 상품 주문 시 수량, 가격 입력받기
- 계산기, 날씨 앱 등 사용자 입력이 필요한 모든 프로그램

등에서 input() 함수를 사용한다.
"""