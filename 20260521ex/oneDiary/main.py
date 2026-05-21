'''
oneDiary
    - member service
        - sign-up, sign-in, modify, delete
    - diary service
        - write, read
'''

from config_dir import config
from member import session

flag = True

while flag:

    menuNum = ''
    if session.signInedMemberId == '':
        # sign-out 일때
        menuNum = int(input('1.sign-up  2.sign-in  99.end'))
    else:
        # sign-in 일때
        menuNum = int(input('3.modify  4.delete  5.sign-out  99.end'))


    if menuNum == config.SIGN_UP:
        print('1.sign-up')
        uId = print('please input new member ID: ')
        uPw = print('please input new member PW: ')
        uMail = print('please input new member MAIL: ')
        uPhone = print('please input new member PHONE: ')

    elif menuNum == config.SIGN_IN:
        print('2.sign-in')
    elif menuNum == config.MEMBER_MODIFY:
        print('3.modify')
    elif menuNum == config.MEMBER_DELETE:
        print('4.delete')
    elif menuNum == config.SIGN_OUT:
        print('5.sign-out')
    elif menuNum == config.SYSTEM_OUT:
        print('99.end')
        flag = False
    
