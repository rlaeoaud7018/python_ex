# 컨테이너형 자료형?
# 여러개의 데이터를 묶어서 관리하는 것을 말한다.
fruit1 = '사과'
fruit2 = '포도'
fruit3 = '복숭아'

fruits = ['사과', '포도', '복숭아']    # 컨테이너: list(리스트)
print(f'fruits: {fruits}')
print(f'fruits type: {type(fruits)}')

# 컨테이너 자료형의 이름은 복수형으로 지정할 것(다수의 자료를 묶어놨기에)

# 파이썬에서 컨테이너 자료형으로는
# 리스트(list), 튜플(tuple), 딕셔너리(dictionary) 가 있다.

# 리스트(list)
fruits = ['사과', '포도', '복숭아'] 

# 인덱스(index): 아이템에 부여된 식별 번호
#    0       1       2
# ['사과', '포도', '복숭아'] 

# 아이템 조회
'''
print(f'fruits[1]: {fruits[1]}')    # 포도
print(f'fruits[2]: {fruits[2]}')    # 복숭아
print(f'fruits[0]: {fruits[0]}')    # 사과
print(f'fruits[3]: {fruits[3]}')    # IndexError: list index out of range
'''

# 리스트의 길이(아이템 개수)
cnt = len(fruits)     # 3
print(f'cnt: {cnt}')

# 리스트의 마지막 아이템의 인덱스 값은 '리스트의 길이 - 1' 이다.
print(f'last data: {fruits[len(fruits)-1]}')

# 리스트의 전체 데이터 조회
# 리스트는 반복 가능한 객체(데이터)입니다. ==> 이리터러블한 이미지
for fruit in fruits:
    print(f'fruit: {fruit}')

for idx, fruit in enumerate(fruits):           # 인덱스, 아이템
    print(f'index: {idx}, fruit: {fruit}')


# by while문 (이렇게도 쓸 수 있다~ 정도만)
i = 0

while 1 < len(fruits):
    print(fruits[1])
    i =+ 1
    break


# 아이템 삽입
fruits = ['사과', '포도', '복숭아']
fruits.append('수박')
print(f'fruits: {fruits}')

# 특정 위치에 삽입
fruits.insert(2, '멜론')  # ['사과', '포도', '멜론', '복숭아']

# 리스트 연결
list1 = [1, 2, 3]
list2 = [10, 20, 30]

list1.extend(list2)     #list1 = [1, 2, 3, 10, 20, 30]
print(f'list1: {list1}')
print(f'list1: {list1}')

# 리스트 연결: +
list3 = list1 +list2        # [1, 2, 3, 10, 20, 30]
print(f'list3: {list3}')

# 아이템 삭제하기
sports = ['football', 'baseball', 'voollyball', 'basketball']

# 마지막 아이템 삭제하기
sports.pop
print(f'sports:{sports}')

# 특정 위치 아이템 삭제하기
sports.pop(1)
print(f'sports: {sports}') # ['football', 'voollyball']

# pop()과 비슷하게 사용할 수 있는 del
del sports[1]
print(f'sports: {sports}')    #  ['football']

# pop() vs del
nums = [1, 2, 3, 4, 5, 6]
deletedNum = nums.pop(3)    # [1, 2, 3, 4, 5, 6]    |   deleted item: 4
print(f'deletedNum: {deletedNum}')

# 특정 아이템 삭제 by 아이템
languages = ['c/c++', 'c#', 'java', 'python']
# languages.pop(2)       ['c/c++', 'c#', 'python']

languages.remove('java')   # ['c/c++', 'c#', 'python']
print(f'languages: {languages}')

# remove()를 이용해서 아이템을 삭제할 때 삭제하려는 아이템의 
# 개수가 2개 이상일 때는 어떻게 해야할까?
languages = ['c/c++', 'c#', 'java', 'python', 'java']
languages.remove('java')
print(f'languages: {languages}')   #  ['c/c++', 'c#', 'python', 'java']
# 처음 java만 삭제된다

# quiz) 과일 리스트에서 야채를 찾아 삭제하기
'''
다음은 냉장고에 있는 과일을 리스트로 나타낸 것입니다.
['사과', '망고', '당근', '수박', '포도', '토마토']
이중 과일이 아닌 '당근'과 '토마토'를 찾아 삭제하는 프로그램을 만들자
'''
fruits = ['사과','망고','당근','수박','포도','참외','토마토']
print(f'fruits: {fruits}')

for item in fruits:
    if item == '당근' or item == '토마토':
        fruits.remove(item)
print(f'fruits: {fruits}')  # ['사과','망고','수박','포도','참외']
