# 데이터 중에서 실수는 현존하는 어떤 언어도 완벽하게 
# 다룰 수 없다.

'''
print(0.1 + 0.2)     # 예상 값 0.3
0.30000000000000004  # 실제 

.1
.2
.3
.4
.5
.6
.7
.8
.9
1.0
'''

# 0.1 부터 1.0까지 다 더하면 생각하는 숫자가 나올까?
# 아님, 실수는 저장하는 순간부터 데이터가 틀어짐

'''
flt = .1 

while True:
    print(f'flt: {flt}')
    flt += .1

    if flt >= 1:
        break
'''

total = .1 + .2            # expectation: .3
print(f'total: {total}')   # total: 0.30000000000000004
if total > .3:
    print('total은 3보다 크다')

