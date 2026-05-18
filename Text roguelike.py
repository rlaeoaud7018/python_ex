import random

# ==========================
# 게임 시작
# ==========================

print('======================')
print('    Dungeon Escape    ')
print('  Text Roguelike RPG'  )
print('======================')

print('1. 게임 시작')
print('2. 종료')

choice = input(' :')

if choice == '1':
    start_game = True
else:
    start_game = False

if not start_game:
    print('게임을 종료합니다.')
    quit()

playerName = input("모험가의 이름을 입력하세요: ")
print('직업을 선택하세요.')
print('1. 전사')
print('2. 궁수')

job = input('선택: ')

# ==========================
# 직업 설정
# ==========================

if job == '1':
    playerJob = '전사'
    playerHP = 120
    playerAtk = 25

else:
    playerJob = '궁수'
    playerHP = 90
    playerAtk = 35

gold = 0

def show_status():
    global player_hp
    global player_atk
    global player_gold
    global potion
    global floor

    print("=======================")
    print(f'이름: {player_name}')
    print(f'체력: {player_hp}')
    print(f'공격력: {player_atk}')
    print(f'포션: {potion}')
    print(f'골드: {player_gold}')
    print(f'현재 층: {floor}')
    print("=======================")

