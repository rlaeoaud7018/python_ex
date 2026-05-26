import rsp_module as rsp

hands = ['가위', '바위', '보']

userChoice = int(input('0.가위 1.바위 2.보 중 하나를 고르세요: '))

rsp.setUNumber(userChoice)
rsp.setRNumber()

print(f'사용자 선택: {hands[rsp.getUNumber()]}')
print(f'컴퓨터 선택: {hands[rsp.getRNumber()]}')


rsp.compareNumber()


import rsp_module as rsp

hands = ['가위', '바위', '보']

userChoice = int(input('0.가위 1.바위 2.보 중 하나를 고르세요: '))

# 사용자 선택 저장
rsp.setUNumber(userChoice)

# 컴퓨터 랜덤 생성
rsp.setRNumber()

# 출력
print(f'사용자 선택: {hands[rsp.getUNumber()]}')
print(f'컴퓨터 선택: {hands[rsp.getRNumber()]}')

# 결과 판정
rsp.compareNumber()