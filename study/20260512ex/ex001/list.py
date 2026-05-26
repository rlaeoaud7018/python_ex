# 컨테이너 자료형(container data type)
# 같은 유형의 자료를 통으로 묶어 관리
# list,  tuple,  dictionary

'''
사과
포도
복숭아
연필
칼

fruits = ['사과', '포도', '복숭아']
tools = ['연필', '칼']
'''

# list
# 카테고리 = [데이터,데이터,데이터]
# 리스트 안에 있는 데이터는 개수로 표현하지 않고 길이(length)로 표현한다.

# fruits = ['사과', '포도', '복숭아'] fruits 리스트의 길이는 3이다.
# 리스트를 선언할때는 대괄호([])를 이용해서 데이터를 묶고 데이터와 데이터는 쉽표(,)로
# 구분 합니다.

# 기초 데이터 타입은 메모리를 직접 관리
# 레퍼런스 데이터 타입은 메모리를 직접 관리하지 않고 데이터의 주소를 기억함
# 즉, 리스트가 저장되는 방식은 사과|포도|복숭아 가 메모리에 저장되면 해당 주소가
# 리스트의 데이터 주소가 아닌 전혀 다른 곳의 메모리에 저장되고 해당 메모리의 이름이 
# 리스트가 되는 것.

# 기초 데이터 타입 : 위치
# 레퍼런스 데이터 타입 : 네비게이션

# 만약 기존 레퍼런스 데이터 타입에 새로운 데이터가 담긴다면?
# 기존 메모리에 담겨있는 사과|포도|복숭아 가 대체되는게 아니라 전혀 다른 곳에 저장되고
# 기존 과일들은 garbage collector 가 정리한다.

'''
# 리스트(list)

fruits = ['사과,''포도','수박','참외','배','자두','복숭아','바나나']   # length = 8
print(f'fruits: {fruits}')
print(f'type of fruits: {type(fruits)}')
'''

# 리스트와 데이터

# 리스트에 포함되는 데이터는 어떤 자료형이든 상관 없습니다.
# 예를 들어 정수, 실수, 문자(열)이 리스트로 묶일 수도 있습니다.


complexList = [10, 3.14, 'a', 'hello'] 
print(f'complexList: {complexList}')
print(f'type of complexList: {type(complexList)}')
# 이렇게 하나의 리스트에 다양한 데이터 타입의 데이터를 넣을 수 있는 언어는
# 파이썬과 javascript뿐이다. java는 불가.

member = []
print(f'member: {member}')
print(f'type of member: {type(member)}')

# ex) 다음 회의 참석자 명단을 리스트로 선언하고 attendList 변수에 담아보자.
attendList = ['이순철','김병헌','김민우','박찬호','김민태']

# how to 리스트의 아이템 조회
# 특정 아이템 조회

fruits = ['사과,','포도','수박','참외','배','자두','복숭아','바나나']   
print(f'fruit[1]: {fruits[1]}')
print(f'fruit[0]: {fruits[0]}')
print(f'fruit[7]: {fruits[7]}')
# 만약 리스트에 존재하지 않는 인데스를 참조하면 어떻게 될까?
# print(f'fruit[8]: {fruits[8]}')
# 인덱스를 불러올 수 없습니다 ! 에러 ! 


# 리스트 길이(아이템 개수) 조회

# 리스트 길이란 리스트의 아이템 개수를 뜻하는 것으로 len() 함수를 사용하면 알 수 있음.
# 다음은 len() 함수를 이용해 리스트의 길이를 확인하는 코드이다.

# numbers = [1,2,3,4,5]
# print(f'numbers: {numbers}')
# print(f'numbers length: (len{numbers})')

# numbers = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
# # 첫 번째 데이터 조회:
# print(f'첫 번째 데이터: {numbers[0]}')

# # 마지막 데이터 조회:
# print(f'마지막 데이터: {numbers[len(numbers)-1]}')

# # len() 함수는 문자열의 길이를 조회하는데에도 사용된다.
# str = 'helllllllllllllllo'
# print(len(str))


# quiz) 입력한 글자 수 확인하기

# 사용자로부터 메세지를 입력 받고, 입력 받은 문자열의 길이를 출력하는 프로그램을 만들어봅시다.


# msg = input('메세지 입력: ')
# msglen = len(msg)
# print(f'msglen: {msglen}')

# # 리스트 전체 데이터 조회
# balls = ['야구공', '축구공', '탁구공', '골프공', '농구공']
# # print(f'{balls[0]}')

# idx = 0
# for item in balls:                          # item = '야구공', item = '축구공 ......
#     print(f'item: {item}, index: {idx}')
#     idx += 0

# for idx, item in enumerate(balls):
#     print(f'item: {item}, index: {idx}')


# balls = ['야구공', '축구공', '탁구공', '골프공', '농구공']

# i = 0

# while i < len(balls):
#     print(f'item: {balls[i]}, index: {i}')
#     i += 1



# quiz) 다음 리스트에서 마지막 인덱스 값을 출력하는 프로그램을 만드시오.
sports = ['baseball', 'basketball', 'tennis', 'golf', 'soccer']
lenVar = len(sports) - 1          # 5 - 1 => 4
print(sports[lenVar])

# quiz) 다음 리스트에서 'python' 문자열의 인덱스 값을 출력하는 프로그램을 만드시오.
languages = ['c/c++', 'c#', 'python', 'java']
for idx, str in enumerate(languages):
    if str == 'python':
        print(f'python idx: {idx}')

# 하지만 위 방식은 코드량이 늘어나면 과부하가 발생하니 아래 방식으로 찾을 것.

targetIdx = languages.index('python')
print(f'targetIdx: {targetIdx}')


# 아이템 기존 리스트에 삽입
# 리스트 마지막에 삽입
sports = ['football', 'baseball', 'volleyball', 'basketball']
print(f'sports: {sports}')

sports.append('basketball')
print(f'sports: {sports}')      # ['football', 'baseball', 'volleyball', 'basketball']
print(f'sports lenght: {len(sports)}')


# quiz) 취미 추가하기

#취미들을 저장할 리스트를 정의하고 사용자가 입력한 취기가 추가 되는 프로그램을 만들어보자
# 그리고 취미의 개수를 출력하자


hobbies = []

while True:
    hobby = input('취미 입력: ')
    
    hobbies.append(hobby)
    print(f'hobbies: {hobbies}')
    selectedMenuNumber = int(input('1. 취미 추가  2. 종료 : '))
    if selectedMenuNumber == 2:
        print(f'취미 개수: {len(hobbies)}')
        break

# 취미 입력: 축구
# hobbies: ['축구']


# 특정 위치에 아이템 삽입
# 리스트의 원하는 위치에 아이템을 삽입할 때는 insert() 함수를 이용합니다.
countries = ['korea', 'china', 'japan']    # ['korea', 'usa', 'china', 'japan']
countries.insert(1, 'usa')
print(f'countries: {countries}')
# 값 : countries: ['korea', 'usa', 'china', 'japan']


# quiz) 누락된 숫자 추가하기
# numbers = [1, 2, 3, 4, 5, 7, 8, 9]               6, 10
# numbers 리스트를 보고 1~10까지 숫자 중 누락된 숫자를 추가해보자.
numbers = [1, 2, 3, 4, 5, 7, 8, 9]

numbers.insert(5, 6)
print(f'numbers: {numbers}')

numbers.append(10)
print(f'numbers: {numbers}')



# 리스트 연결하기
# 리스트에 또 다른 리스트를 연결할 때는 extend() 함수를 사용합니다.
list1 = [1, 2, 3]
print(f'list1: {list1}')        # [1, 2, 3]

list2 = [10, 20, 30]    
print(f'list2: {list2}')        # [10, 20, 30]

list1.extend(list2)             
print(f'list1: {list1}')        # [1, 2, 3, 10, 20, 30]
print(f'list2: {list2}')        # [10, 20, 30]

list1 = list1 + list2
print(f'list1: {list1}')
print(f'list2: {list2}')
# print(f'list3: {list3}')



# 리스트 아아템 삭제하기
# 리스트 마지막 아이템 삭제
sports = ['football', 'baseball', 'volleyball', 'basketball']
print(f'sport: {sports}')    # ['football', 'baseball', 'volleyball', 'basketball']
sports.pop()                 # pop() 괄호 안에 인덱스를 미표기하면 마지막 아이템 삭제
print(f'sport: {sports}')    # ['football', 'baseball', 'volleyball', 'basketball']
sports.pop(1)                # pop() 괄호 안에 인덱스를 표기하면 해당 인덱스의 아이템 삭지ㅔ
print(f'sport: {sports}')    # ['football', 'volleyball']

removedItem = sports.pop()
print(f'removedItem: {removedItem}')

# pop() 대신 del 키워드를 이용해서 아이템을 삭제할 수 있다.
sports = ['football', 'baseball', 'volleyball', 'basketball']
del sports[2]
print(f'sports:{sports}')



# quiz) sports 리스트에서 'vollyball'을 삭제하는 프로그램을 만들자.
sports = ['football', 'baseball', 'volleyball', 'basketball']
volleyballIdx = sports.index('volleyball')
sports.pop(volleyballIdx)
print(f'sports: {sports}')