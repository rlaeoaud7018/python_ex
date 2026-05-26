# quiz) 단위환산 프로그램
'''
mm 단위의 길이를 입력하면 cm, m, inch, ft 등으로 단위가 
변환되어 출력되는 함수가 포함된 프로그램을 만들어 봅시다.
'''

def convertUnit(lenMm):
    
    unitDic = {}

    unitDic['cm'] = lenMm * .1
    unitDic['m'] = lenMm * .001
    unitDic['inch'] = lenMm * .03937
    unitDic['ft'] = lenMm * .003281

    return unitDic

def printLength(lengths):
    for len in lengths.keys():
        print(f'{len}: {lengths[len]}{len}')

inputMmDataint = (input('길이(mm)를 입력하세요. '))
resultData = convertUnit(inputMmDataint)
printLength(resultData)



# quiz) 할인된 상품 가격포 표시 출력 프로그램
'''
한빛 마트는 고객 감사의 일환으로 ‘오늘의 할인’ 이벤트를 진행할 계획입니다. 아래
의 상품 가격표를 참고해서 ‘오늘의 할인율’을 입력하면 할인된 가격이 출력되는 프
로그램을 만들어 봅시다.
'''

# 상품 원가

standardPrice = {

    '쌀': 9900,
    '상추': 1900,
    '고추': 2900,
    '마늘': 8900,
    '통닭': 5600,
    '햄': 6900,
    '치즈': 3900

}


# 할인 가격 계산 함수

def getDiscountPrice(rate):

    dcPrice = {}

    # 상품 하나씩 반복
    for goodsName in standardPrice.keys():

        # 할인 가격 계산
        disPrice = int(
            standardPrice[goodsName] * (1 - (rate / 100))        )

        # 할인 가격 저장
        dcPrice[goodsName] = disPrice

    return dcPrice


# 가격 출력 함수

def printPrice(priceList):

    print('\n[ 할인 가격표 ]')

    for goodsName, goodsPrice in priceList.items():

        print(
            f'{goodsName}: '
            f'{standardPrice[goodsName]}원 '
            f'--> '
            f'{goodsPrice}원'
        )


# 할인율 입력

inputRateData = int(input('오늘의 할인율 입력(%): '))


# 할인 가격 계산

discountPrice = getDiscountPrice(inputRateData)


# 결과 출력

printPrice(discountPrice)


# quiz) 영어사전
englishDictionary = {
    'apple': '사과',
    'chair': '의자',
    'doll': '인형',
    'book': '책',
    'piano': '피아노',
    'clock': '시계',
}

def printWord(engWord):
    print(f'{engWord}: {englishDictionary[engWord]}')

printWord(input('찾고자 하는 영어 단어 입력'))



