# 텍스트 파일 함수

# open = 파일 경로, 목적), 'w' = write 쓰기, 'a' = 기존 내용에 이어서 쓰기,   'r' = read 읽기

# open('C:\\kdm\\python\\test.txt', 'w')
# open('C:\kdm\python\\test1.txt', 'w')
# open('C:/kdm/python/test2.txt', 'w')

'''
file = open('C:/kdm/python/test.txt', 'w')      # 파일을 '쓰기' 모드로 open
result = file.write('Hello python!')            # 쓰기(write)
print(f'result: {result}')                      # 13, 쓰여진 문자의 길이 확인 (result 사용은 선택)
file.close()                                    # 파일 닫기(close, 외부자원 해제)


file = open('C:/kdm/python/test.txt', 'r')      # 파일을 '읽기' 모드로 open
readResult = file.read()                        # 읽기(read)
print(f'readResult: {readResult}')              # Hello python!
print(f'readResult type: {type(readResult)}')              
file.close()


=======================================================================================================================
# test.txt 내용을 123으로 변경
=======================================================================================================================


file = open('C:/kdm/python/test.txt', 'r')      # 파일을 '읽기' 모드로 open
readResult = file.read()                        # 읽기(read)
print(f'readResult: {readResult}')              # 123
print(f'readResult type: {type(readResult)}')   # str   
file.close()
'''

# =======================================================================================================================
#  그럼 여기서 숫자를 변경하고 싶다면? 20 => 21
# =======================================================================================================================

'''
file = open('C:/kdm/python/test.txt', 'r')      # 파일을 '읽기' 모드로 open
readResult = file.read()                        # 읽기(read)
print(f'readResult: {readResult}')              # 20
print(f'readResult type: {type(readResult)}')   # str   

readResult = int(readResult)                    # 텍스트 파일을 스트링으로 읽기 때문에 readResult 값을 int로 변환
readResult += 1
print(f'readResult: {readResult}')

file.close()
'''


# =======================================================================================================================
# 'w' 쓰기의 특성
# =======================================================================================================================

'''
file = open('C:/kdm/python/test1.txt', 'w')     # 쓰기
file.write('hello~')                            # 텍스트 파일 내에 hello~ 기록
file.close()

file = open('C:/kdm/python/test1.txt', 'w')     # 쓰기
file.write('hi')                                # hi를 썼더니 이전 기록인 hello~가 사라짐, 즉 'w'는 이전 내용을 덮어쓰는 것
file.close()
'''

# =======================================================================================================================
#  기존 내용을 유지한채 내용을 이어쓰려면?
# =======================================================================================================================

'''
file = open('C:/kdm/python/test1.txt', 'a')     # 쓰기
file.write('hello~')                            # 기존 hi 옆에다  hello~ 작성하게 됨  => hihello
file.close()

# 쓸 내용 앞에 개행을 넣으면 다음줄에 작성함

file = open('C:/kdm/python/test1.txt', 'a')     # 쓰기
file.write('\nhello~')                          # \n 개행을 통해 hi   ------ 다음줄에 hello~
file.close()
'''

'''
# 다른 방식으로 접근하는 방법과 range를 활용한 작성법

with open('C:/kdm/python/test1.txt', 'a') as file:
    for n in range(10):
        file.write('\nhello~')
'''

# =======================================================================================================================
#  예외 처리(보험)
# =======================================================================================================================

# 세상에 모든 프로그램은 100% 완벽할 수가 없다.

'''
print(10 + 20)      # 30
print(10 / 0)       # error
print(10 - 20)      # X
print(10 * 20)      # X
'''

# 예외 처리 기본 문법

'''
try ~ except
'''
'''
print(10 + 20)              # 30
try: 
    print(10 / 0)           # error   
except Exception as e:
    print(f'e: {e}')        # division by zero

print(10 - 20)              # -10
print(10 * 20)              # 200

# try 캐치시 예외가 터질만한 곳만 딱 찍어서 넣어줘야지 잘 돌아감
# 남발시 메모리 낭비 + 안돌아감

try: 
    print(10 + 20)          # 30
    print(10 / 0)           # error 
    print(10 - 20)          # X
    print(10 * 20)          # X

except Exception as e:
    print(f'e: {e}')        # division by zero

# =======================================================================================================================

print(10 + 20)              # 30
try: 
    print(10 / 20)          # 0.5   
except Exception as e:
    print(f'e: {e}')        # 
else:
    print('에러가 발생하지 않으면 실행되는 코드')  # '에러가 발생하지 않으면 실행되는 코드' 출력

print(10 - 20)              # -10
print(10 * 20)              # 200


print(10 + 20)              # 30
try: 
    print(10 / 0)           # error   
except Exception as e:
    print(f'e: {e}')        # 
else:
    print('에러가 발생하지 않으면 실행되는 코드')  # 에러가 발생해서 미출력

finally:
    print('에러가 발생하든 안하든 무조건 실행되는 코드') # 에러가 발생해서 '에러가 발생하든 안하든 무조건 실행되는 코드' 출력

print(10 - 20)              # -10
print(10 * 20)              # 200
'''