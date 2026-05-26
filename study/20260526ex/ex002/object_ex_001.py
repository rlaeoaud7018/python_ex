# 클래스(객체를 만들기 위한 틀(설계도)) 문법

class FishBread:

    # 속성(attribute)                # 클래스 선언
    def __init__(self, f, b):       # 클래스 속성 정의
        self.flour = f
        self.bean  = b

    # 기능(function, method)         # 클래스 속성 정의
    def makeFishBread(self):
        print('붕어빵 제조')

# 붕어빵 클래스로부터 객체를 만들어 보자.
myFishBread = FishBread('팥', '밀가루')
friendFishBread = FishBread('호박', '쌀')
hisFishBread = FishBread('꿀', '밀가루')

print(f'내 붕어빵의 속 내용물: {myFishBread.flour}')  # 팥
print(f'내 붕어빵의 반죽: {myFishBread.bean}')  # 팥

print(f'친구 붕어빵의 속 내용물: {friendFishBread.flour}')  # 호박
print(f'친구 붕어빵의 반죽: {friendFishBread.bean}')  # 쌀


# 계산기 클라스
class Calculator:

    # 속성
    def add(self):
        print(f'add: {self.num1 + self.num2}')

    def sub(self):
        print(f'sub: {self.num1 - self.num2}')
    
    def mul(self):
        print(f'mul: {self.num1 * self.num2}')
    
    def div(self):
        print(f'div: {self.num1 / self.num2}')
    
myCalculator = Calculator(10, 20)
friendCalculator = Calculator(100, 200)

print(myCalculator.add())
print(myCalculator.sub())
print(myCalculator.mul())
print(myCalculator.div())



# 인간 클래스
class Human:

    # 속성
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    # 기능
    def walk(self):
        print('걷자!')
    
    def run(self):
        print('달리자!')

    def printMyInfo(self):
        print(f'나의 신장: {self.height}')        
        print(f'나의 체중: {self.weight}')        

human1 = Human(1988, 87)
human2 = Human(165, 49)

human1.printMyInfo()
human2.printMyInfo()

human1 = human2
human1.printMyInfo()

human1.height = 200
human1.weight = 39

human2.printMyInfo()


