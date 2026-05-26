# 데이터 입력(input data)
# input()

'''
print('데이터를 입력하세요.')
inputData = input()        * input() = 외부에서 데이터를 받는 함수
print(inputData)
'''

'''
print('정수를 입력하세요.')
inputInteger = input()    # 6
print(inputInteger)       # 6
print(type(inputInteger)) # Int
'''

'''
print('실수 입력하세요.')
inputFloat = input()       # 3.14
print(inputFloat)          # 3.14
print(type(inputFloat))    # str
'''

# 외부에서 들어온 자료는 전부 문자열로 취급된다.

'''
print('논리형 데이터 입력하세요.')    # 논리형 데이터 입력하세요. (개행)
intputBoolean = input()           # True
print(intputBoolean)              # True
print(type(intputBoolean))        # str
'''

# inputBoolean = input('논리형 데이터 입력하세요.', end='')      # \n = 개행  \n\n\n\n\n                      
# print(inputBoolean)       # True
# print(type(inputBoolean)) # str

# 자료형을 변환해야 합니다. (데이터 타입 변환)
# userInputData = input('사용자야~~~~ 정수 입력해라~')        # 10
# print(userInputData)                                     # 10
# print(type(userInputData))                               # str
# userInputData = int(userInputData)                       # str --> int
# print(type(userInputData))                               # int 


# str --> boolean
# userInputData = input('True or False 입력하세요')
# print(userInputData)                                   # True
# print(type(userInputData))                             # str
# userInputData = bool(userInputData) 
# print(userInputData)

# str --> float
# userInputData = input('실수 입력하세요')
# print(userInputData)
# print(type(userInputData))                       # str
# userInputData = float(userInputData)
# print(type(userInputData))                       # float

userInputData = 'True'
userInputData = bool(userInputData)
print(type(userInputData))

# 데이타 형변환 = type casting 

x = 3.141592
y = int(x)
print(y)                   # 3
print(float(y))            # 3.0
