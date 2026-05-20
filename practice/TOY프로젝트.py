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


'''
-----------------------------------------------------------------
                              초  안 
-----------------------------------------------------------------
'''


members = {}

flag = True


# 회원가입 
def joinMember():                             # 함수 정의

    memberID = input('회원ID 입력: ')          # 정보 입력
    memberPW = input('회원PW 입력: ')
    memberPhone = input('회원Phone 입력: ')
    memberEmail = input('회원Email 입력: ')

    members[memberID] = {                     # 새로운 딕셔너리 --> 멤버스[키값] = {나머지 정보들}

        'PW': memberPW,                       # 기존 입력 정보들
        'Phone': memberPhone,
        'Email': memberEmail

    }

    print('회원가입 완료')

# 로그인
def loginMember():                            # 함수 정의

    memberID = input('회원ID 입력: ')
    memberPW = input('회원PW 입력: ')

    if memberID in members:                       # 만약 멤버ID가 멤버스(딕)에 있다면:
        if members[memberID]['PW'] == memberPW:   # 그리고 만약 멤버스에 있는 멤버 아이디와 사용자가 입력한 'PW'가 멤버PW와 같다면:
            print('로그인 성공')
        else:
            print('로그인 실패')
    else:
        print('ID 또는 PW가 틀렸거나 존재하지 않는 회원입니다.')

# 특정 회원 정보 출력
def printMemberInfo():                            # 함수 정의 

    memberID = input('회원ID 입력: ')              # 정보 확인
    memberPW = input('회원PW 입력: ')

    if memberID in members:                       # 만약 멤버ID가 멤버스(딕)에 있다면:
        if members[memberID]['PW'] == memberPW:   # 그리고 만약 멤버스에 있는 멤버 아이디와 사용자가 입력한 'PW'가 멤버PW와 같다면:
            print('---------회원정보---------')

            print(f'회원ID: {memberID}')                       # 기존 멤버ID    
            print(f"회원PW: {members[memberID]['PW']}")        # 해당 멤버ID 안에 있는 'PW'(35줄) 정보 가져오기
            print(f"회원Phone: {members[memberID]['Phone']}")  # 해당 멤버ID 안에 있는 'Phone'(36줄) 정보 가져오기
            print(f"회원Email: {members[memberID]['Email']}")  # 해당 멤버ID 안에 있는 'Email'(37줄) 정보 가져오기

        else: 
            print('비밀번호가 일치하지 않습니다.')
    else:
        print('ID 또는 PW가 틀렸거나 존재하지 않는 회원입니다.')

# 모든 회원 정보 출력
def printAllMembers():                           # 함수 정의
    if len(members) == 0:                        # 멤버스(딕) 길이가 0이면(등록된 멤버가 없다면) :
        print('가입된 회원이 없습니다.')
    
    else:
        for memberID in members:                 # members 안 회원ID들을 하나씩 꺼내라는 뜻

            print('---------회원정보---------')

            print(f'회원ID: {memberID}')
            print(f"회원PW: {members[memberID]['PW']}")
            print(f"회원Phone: {members[memberID]['Phone']}")
            print(f"회원Email: {members[memberID]['Email']}")


# 프로그램 시작

while flag:                             # while flag = 상태변화가 True 일시 계속 실행

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


'''
-----------------------------------------------------------------
                        상수 사용 및 개선 버젼
-----------------------------------------------------------------
'''


# =========================
# 상수(Constant) 정의
# =========================

SIGN_UP                = 1
SIGN_IN                = 2
PRINT_MEMBER_INFO      = 3
PRINT_ALL_MEMBERS      = 4
SYSTEM_EXIT            = 99


# =========================
# 회원 정보 저장 딕셔너리
# =========================

members = {}

# 프로그램 실행 상태
flag = True


# =========================
# 회원가입 함수
# =========================

def joinMember():

    print('\n[회원가입]')

    memberID = input('회원ID 입력: ')
    memberPW = input('회원PW 입력: ')
    memberPhone = input('회원Phone 입력: ')
    memberEmail = input('회원Email 입력: ')

    # 이미 존재하는 ID 체크
    if memberID in members:
        print('이미 존재하는 회원ID입니다.')
    
    else:

        members[memberID] = {

            'PW': memberPW,
            'Phone': memberPhone,
            'Email': memberEmail

        }

        print('회원가입 완료')


# =========================
# 로그인 함수
# =========================

def loginMember():

    print('\n[로그인]')

    memberID = input('회원ID 입력: ')
    memberPW = input('회원PW 입력: ')

    # 회원 존재 여부 확인
    if memberID in members:

        # 비밀번호 일치 여부 확인
        if members[memberID]['PW'] == memberPW:

            print('로그인 성공')

        else:

            print('비밀번호가 일치하지 않습니다.')

    else:

        print('존재하지 않는 회원입니다.')


# =========================
# 특정 회원 정보 출력 함수
# =========================

def printMemberInfo():

    print('\n[특정 회원 정보 출력]')

    memberID = input('회원ID 입력: ')
    memberPW = input('회원PW 입력: ')

    # 회원 존재 여부 확인
    if memberID in members:

        # 비밀번호 확인
        if members[memberID]['PW'] == memberPW:

            print('\n--------- 회원정보 ---------')

            print(f'회원ID    : {memberID}')
            print(f"회원PW    : {members[memberID]['PW']}")
            print(f"회원Phone : {members[memberID]['Phone']}")
            print(f"회원Email : {members[memberID]['Email']}")

        else:

            print('비밀번호가 일치하지 않습니다.')

    else:

        print('존재하지 않는 회원입니다.')


# =========================
# 모든 회원 정보 출력 함수
# =========================

def printAllMembers():

    print('\n[전체 회원 정보 출력]')

    # 회원 수 확인
    if len(members) == 0:

        print('가입된 회원이 없습니다.')

    else:

        # 회원ID 하나씩 반복
        for memberID in members:

            print('\n--------- 회원정보 ---------')

            print(f'회원ID    : {memberID}')
            print(f"회원PW    : {members[memberID]['PW']}")
            print(f"회원Phone : {members[memberID]['Phone']}")
            print(f"회원Email : {members[memberID]['Email']}")


# =========================
# 프로그램 시작
# =========================

while flag:

    print('\n==============================')
    print(' 회원 관리 프로그램 ')
    print('==============================')
    print(f'{SIGN_UP}. 회원가입')
    print(f'{SIGN_IN}. 로그인')
    print(f'{PRINT_MEMBER_INFO}. 특정 회원 정보 출력')
    print(f'{PRINT_ALL_MEMBERS}. 모든 회원 정보 출력')
    print(f'{SYSTEM_EXIT}. 종료')

    menu = int(input('메뉴 선택: '))

    # 회원가입
    if menu == SIGN_UP:

        joinMember()

    # 로그인
    elif menu == SIGN_IN:

        loginMember()

    # 특정 회원 정보 출력
    elif menu == PRINT_MEMBER_INFO:

        printMemberInfo()

    # 전체 회원 정보 출력
    elif menu == PRINT_ALL_MEMBERS:

        printAllMembers()

    # 프로그램 종료
    elif menu == SYSTEM_EXIT:

        flag = False
        print('프로그램 종료')

    # 잘못 입력
    else:

        print('잘못 입력했습니다.')



'''
-----------------------------------------------------------------
                          교수님 강의 버젼
-----------------------------------------------------------------
'''

SIGN_UP                 = 1
SIGN_IN                 = 2
PRINT_MY_INFO           = 3
PRINT_ALL_MEMBER_INFO   = 4
SYSTEM_SHUTDOWN         = 99

DEV_MOD = True

members = {}            # Database

if DEV_MOD:

    uIds = ['gildong', 'chanho', 'saeri']
    uPws = ['1234', '5678', '9012']
    uMails = ['gildong@gmail.com', 'chanho@naver.com', 'saeri@daum.net']
    uPhones = ['010-1234-5678', '010-9999-8888', '010-7777-6666']

    for n in range(len(uIds)):      # 3회 반복 ( 0, 1, 2 )
        members[uIds[n]] = {
            'uId': uIds[n],
            'uPw': uPws[n],
            'uMail': uMails[n],
            'uPhone': uPhones[n]
        }

# functions START
def getSelectedMenuNum():
    selectedMenuNum = int(input('1.회원가입    2.로그인    3.나의 정보 출력     4.모든 회원 정보 출력    99.종료'))
    return selectedMenuNum

def setNewMember(uId, uPw, uMail, uPhone):
    members[uId] = {
                'uId': uId,
                'uPw': uPw,
                'uMail': uMail,
                'uPhone': uPhone
            }
def isMember(uId):
    if uId in members:
            print(f'{uId}는(은) 이미 사용중 입니다. 다시 확인하세요.')
            return True
    else:
        return False

def printAllMemberInfo(value):
    for key1, value1 in value.items():
                print(f'{key1}: {value1}')
# functions END


flag = True
while flag:
    
    userSelectedMenuNum = getSelectedMenuNum()

    if userSelectedMenuNum == SIGN_UP:              # 1.회원가입
        uId = input('Input member ID: ')
        if not isMember(uId):        # False: 회원이 없는경우(회원가입 진행O)   True: 회원이 있는경우(회원가입 진행X)
            uPw = input('Input member PW: ')
            uMail = input('Input member EMAIL: ')
            while True:
                if '@' not in uMail:
                    print('입련한 이메일 주소가 형식에 맞지 않습니다. ')
                    uMail = input('Input member EMAIL: ')
                else:
                    break

            uPhone = input('Input member PHONE: ')

            setNewMember(uId, uPw, uMail, uPhone)

            print('SIGN-UP SUCCESS!!')

            if DEV_MOD: print(f'members: {members}')

    elif userSelectedMenuNum == SIGN_IN:            # 2.로그인 
        signInCount = 1
        while True:
            uId = input('Input member ID: ')
            uPw = input('Input member PW: ')

            if uId in members:
                uInfo = members[uId]
                if uInfo['uPw'] == uPw:
                    print('SIGN-IN SUCCESS!!')
                else:
                    print('SIGN-IN FAIL!!')
                    signInCount += 1
                    if signInCount > 3:
                        print('3회 이상 틀렸어요!!')
                        break
            else:
                print('존재 하지 않은 ID입니다. 다시 확인하세요.')
        

    elif userSelectedMenuNum == PRINT_MY_INFO:      # 3.나의 정보 출력  
        uId = input('Input member ID: ')
        uPw = input('Input member PW: ')

        if uId in members:
            uInfo = members[uId]
            if uInfo['uPw'] == uPw:
                print('SIGN-IN SUCCESS!!')

                print('-' * 30)
                for key, value in uInfo.items():
                    print(f'{key}: {value}')
                print('-' * 30)

            else:
                print('SIGN-IN FAIL!!')
        else:
            print('존재 하지 않은 ID입니다. 다시 확인하세요.')

    elif userSelectedMenuNum == PRINT_ALL_MEMBER_INFO:      # 4.모든 회원 정보 출력
        for key, value in members.items():
            print(f'{key}님의 정보 ----------------')
            printAllMemberInfo(value)
            print('-' * 30)

    elif userSelectedMenuNum == SYSTEM_SHUTDOWN:    # 99.종료
        flag = False
        print('Good bye~')