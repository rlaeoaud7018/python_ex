# TOY 프로젝트 진행

'''
처음 프로그램이 실행되면 다음과 같은 메뉴를 출력한다.
메뉴: 1.회원가입   2.로그인   3.특정 회원 정보 출력   
4.모든 회원 정보 출력   99.종료
사용자가 :
'1.회원가입'을 선택하면 회원ID, 회원PW, 회원Email, 회원Phone 
정보를 입력받아 회원가입 진행한다.
'2.로그인'을 선택하면 회원ID, 회원PW를 입력받아 로그인 '성공' 
또는 '실패'를 출력한다.
'3.특정 회원 정보 출력을 선택하면 회원ID와 회원PW를 입력받아 
일치하는 회원 정보를 모두 출력한다.
'4.모든 회원 정보 출력'를 선택하면 가입되어 있는 모든 회원 정보를 출력한다.
'99.종료'를 선택하면 프로그램 종료 시킨다.
'''



members = {}

flag = True


# 회원가입 
def joinMember():

    memberID = input('회원ID 입력: ')
    memberPW = input('회원PW 입력: ')
    memberPhone = input('회원Phone 입력: ')
    memberEmail = input('회원Email 입력: ')

    members[memberID] = {

        'PW': memberPW,
        'Phone': memberPhone,
        'Email': memberEmail

    }

    print('회원가입 완료')

# 로그인
def loginMember():

    memberID = input('회원ID 입력: ')
    memberPW = input('회원PW 입력: ')

    if memberID in members:
        if members[memberID]['PW'] == memberPW:
            print('로그인 성공')
        else:
            print('로그인 실패')
    else:
        print('ID 또는 PW가 틀렸거나 존재하지 않는 회원입니다.')

# 특정 회원 정보 출력
def printMemberInfo():

    memberID = input('회원ID 입력: ')
    memberPW = input('회원PW 입력: ')

    if memberID in members:
        if members[memberID]['PW'] == memberPW:
            print('---------회원정보---------')

            print(f'회원ID: {memberID}')
            print(f"회원PW: {members[memberID]['PW']}")
            print(f"회원Phone: {members[memberID]['Phone']}")
            print(f"회원Email: {members[memberID]['Email']}")

        else: 
            print('비밀번호가 일치하지 않습니다.')
    else:
        print('ID 또는 PW가 틀렸거나 존재하지 않는 회원입니다.')

# 모든 회원 정보 출력
def printAllMembers():
    if len(members) == 0:
        print('가입된 회원이 없습니다.')
    
    else:
        for memberID in members:

            print('---------회원정보---------')

            print(f'회원ID: {memberID}')
            print(f"회원PW: {members[memberID]['PW']}")
            print(f"회원Phone: {members[memberID]['Phone']}")
            print(f"회원Email: {members[memberID]['Email']}")


# 프로그램 시작

while flag:

    print()
    print('메뉴')
    print('1.회원가입')
    print('2.로그인')
    print('3.특정 회원 정보 출력')
    print('4.모든 회원 정보 출력')
    print('99.종료')

    menu = int(input('메뉴 선택: '))

    if menu == 1:

        joinMember()
    
    elif menu == 2:

        loginMember()

    elif menu == 3:

        printMemberInfo()
    
    elif menu == 4:

        printAllMembers()

    elif menu == 99:

        flag = False
        print('프로그램 종료')

    else:

        print('잘 못 입력했습니다.')

