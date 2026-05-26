# 객체 = 속성 + 기능
'''
속성(attribue)
num1 = int(input())
num2 = int(input())

기능(function)
def add():
def subtract():
def multiply():
def divide():
'''

# 클래스
# 클래스는 첫글자를 대문자 사용

"""
클래스란?

1. 데이터(속성)와 기능(메서드)을 하나로 묶은 것
2. 객체를 만들기 위한 설계도/틀/템플릿
3. 코드의 재사용성을 높이는 도구
4. 현실 세계의 사물을 코드로 표현하는 방법
"""

class Car:
    # ↓ 데이터 (속성/변수)
    brand = None
    color = None
    speed = 0
    
    # ↓ 기능 (메서드/함수)
    def start(self):
        print("시동 걸기")
    
    def accelerate(self):
        print("가속하기")


class ClassName:              # ← 1. 클래스 선언
    
    # 2. 클래스 변수 (모든 객체가 공유)
    class_variable = "공유됨"
    
    # 3. 생성자 (객체 초기화)
    def __init__(self, param1, param2):
        self.instance_var1 = param1  # 인스턴스 변수
        self.instance_var2 = param2
    
    # 4. 인스턴스 메서드 (일반 메서드)
    def instance_method(self):
        return self.instance_var1
    
    # 5. 클래스 메서드
    @classmethod
    def class_method(cls):
        return cls.class_variable
    
    # 6. 정적 메서드
    @staticmethod
    def static_method():
        return "정적 메서드"
    
    # 7. 비공개 메서드
    def __private_method(self):
        return "외부에서 접근 불가"



# 붕어빵 틀 (클래스)
class 붕어빵틀:
    def __init__(self, 속재료):
        self.속재료 = 속재료
        self.모양 = "붕어 모양"
        self.크기 = "손바닥 크기"
    
    def 굽기(self):
        print(f"{self.속재료} 붕어빵을 굽습니다 🔥")

# 붕어빵 틀로 만든 실제 붕어빵들 (객체)
붕어빵1 = 붕어빵틀("팥")
붕어빵2 = 붕어빵틀("슈크림")
붕어빵3 = 붕어빵틀("피자")

# 각각 다른 붕어빵이지만, 같은 틀로 만들어짐
붕어빵1.굽기()  # 팥 붕어빵을 굽습니다 🔥
붕어빵2.굽기()  # 슈크림 붕어빵을 굽습니다 🔥

# 건물 설계도 (클래스)
class House:
    def __init__(self, address, rooms, color):
        self.address = address    # 주소
        self.rooms = rooms        # 방 개수
        self.color = color        # 외벽 색상
        self.lights_on = False    # 불 켜짐 여부
    
    def turn_on_lights(self):
        self.lights_on = True
        print(f"{self.address} 집에 불이 켜졌습니다 💡")
    
    def turn_off_lights(self):
        self.lights_on = False
        print(f"{self.address} 집 소등 🌙")

# 같은 설계도로 여러 집 짓기 (객체 생성)
my_house = House("서울시 강남구", 3, "흰색")
your_house = House("서울시 마포구", 2, "회색")
friend_house = House("부산시 해운대구", 4, "파란색")

# 각 집은 독립적으로 동작
my_house.turn_on_lights()      # 서울시 강남구 집에 불이 켜졌습니다 💡
your_house.turn_on_lights()    # 서울시 마포구 집에 불이 켜졌습니다 💡

