"""
    객체와 클래스
"""

'''
    - 객체(object) : 데이터(변수, 속성이라고 부름)와 코드(함수, 메서드라고 부름)를 포함하는 커스텀 자료구조
    - 객체는 어떤 구체적인 것의 유일한 인스턴스(instance)를 나타낸다.
    - 객체는 명사, 메서드는 동사로 생각하면 됨.
'''

# 클래스 선언하기 : class
'''
    - 아무도 만들어본 적이 없는 새 객체를 생성
'''
class Cat() :
    pass # 클래스가 비어있다는 것을 나타내기 위해 pass를 사용

# 함수처럼 클래스 이름을 호출하여 클래스로부터 객체를 생성할 수 있음.
a_cat = Cat()
another_cat = Cat()


# 속성 
'''
    - 속성 : 클래스나 객체 내부의 변수
    - 객체나 클래스가 생성되는 동안이나 이후에 속성을 할당할 수 있음
'''
class Cat :
    pass

a_cat = Cat()
print(a_cat)

another_cat = Cat()

a_cat.age = 3
a_cat.name = "Mr. Lee"
a_cat.nemesis = another_cat

print (a_cat.age)
print (a_cat.name)
print (a_cat.nemesis)

# 다른 객체에 name 속성 할당
a_cat.nemesis.name = 'Mrs. Lee'
print(a_cat.nemesis.name)

# 메서드 : 클래스 또는 객체의 함수. 

# 초기화 : 객체를 생성할 때 속성을 할당하려면 객체 초기화(initialization) 메서드 __init__()를 사용한다.
class Cat :
    def __init__(self) : #클래스 정의에서 개별 객체를 초기화하는 특수 메서드. self 매개변수는 개별 객체 자신을 참조하도록 지정.
        pass
'''
    - 위 코드는 실제 파이썬 클래스 정의에서 볼 수 있다.
    - 클래스 정의에서 __init__() 을 정의할 때 첫번째 매개변수 이름은 self이어야 한다. (고정 - 일반적으로 사용)
'''    
class Cat :
    def __init__(self,name) : #초기화 메서드
        self.name = name #중요
        
furball =Cat('Grumpy')

print('Our latest addition : ', furball.name) # furball.name은 self.name을 참조


# 상속
'''
    기존 클래스와 새로운 클래스를 써야 할 경우 상속을 통해 해결 가능
'''
# 부모 클래스 상속받기
'''
    - 필요한 것만 추가하거나 변경해서 새 클래스를 정의한다.
    - 그리고 기존 클래스의 행동을 오버라이드[override(재정의)]
    - 기존 클래스는 부모 클래스, 슈퍼 클래스, 베이스 클래스라고 부른다.
    - 새 클래스는 자식 클래스, 서브 클래스, 파생된 클래스라고 부른다.
'''
class Car() :
    pass

class Yugo(Car) :
    pass

# issubclass() 함수를 이용하여 다른 클래스에서 파생되었는지 확인 가능
print(issubclass(Yugo,Car))

# 각 클래스로부터 객체를 생성
give_me_a_car = Car()
give_me_a_yugo = Yugo()

class Car() :
    def exclaim(self) :
        print("I'm a Car!")
    
class Yugo(Car) :
    pass

give_me_a_car = Car()
give_me_a_yugo = Yugo() #특별한 것을 하지 않고 Car 로부터 exclaim() 메서드를 상속받음.

give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

# 메서드 오버라이드
class Car() :
    def exclaim(self) :
        print("I'm a Car!")
    
class Yugo(Car) :
    def exclaim(self) :
        print("I'm a Yugo! Much like a Car, but more-Yugo-ish.")

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
give_me_a_yugo.exclaim() #메서드 오버라이드(기존 동일 이름의 메서드를 쓰는게 아니라 자기 객체에 있는 동일한 함수를 씀)

class Person() :
    def __init__(self, name) :
        self.name = name
        
class MDPerson(Person) :
    def __init__(self, name):
        self.name = "Doctor " + name

class JDPerson(Person) :
    def __init__(self, name):
        self.name = name + ", Esquire"
        
person = Person('Fedd')       
doctor = MDPerson('Fedd')
lawyer = JDPerson('Fedd')

print(person.name)
print(doctor.name)
print(lawyer.name)

# 메서드 추가하기

class Car() :
    def exclaim(self) :
        print("I'm a Car!")
        
class Yugo(Car) :
    def exclaim(self) :
        print("I'm a Yugo! Much like a Car, But more Yugo-ish.")
    def need_a_push(self) :
        print("A little Help here?")
        

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_yugo.need_a_push()


# 부모에게 도움받기 : super()
'''
    - 자식 클래스에서 부모 클래스를 호출할 때 쓰는 방법
'''
class Person() :
    def __init__(self, name) :
        self.name = name
        
class EmailPerson(Person) :
    def __init__(self, name, email) :
        super().__init__(name) #Person.__init__() 메서드를 호출한다.
        self.email = email
        
bob = EmailPerson('Bob Frapples','bob@frapples.com')

print(bob.name)
print(bob.email)

# 이 클래스는 상속의 이점을 활용할 수 없음.
class EmailPerson(Person) :
    def __init__(self, name, email) :
        self.name = name
        self.email = email


# 다중 상속
'''
    - 파이썬의 상속은 메서드 해석 순서(MRO)에 달려있다.
'''
class Animal :
    def says(self) :
        return 'I speak!'

class Horse(Animal) :
    def says(self) :
        return 'Neigh!'
    
class Donkey(Animal) :
    def says(self) :
        return 'Hee-haw!'

class Mule(Donkey, Horse) :
    pass

class Hinny(Horse, Donkey) :
    pass


'''
    Mule 클래스에서 메서드나 속성을 찾을 때 순서
    1. 객체 자신 (Mule 타입)
    2. 객체의 클래스 (Mule)
    3. 클래스의 첫 번째 부모 클래스 (Donkey)
    4. 클래스의 두 번째 부모 클래스 (Horse)
    5. 부모의 부모 클래스 (Animal)
'''

print(Mule.mro())

mule = Mule()
hinny = Hinny()

print(mule.says())
print(hinny.says())

# 믹스인 
'''
    - 클래스 정의에 부모 클래스를 추가하여 상속받을 수 있음
    - 그러나 이를 헬퍼(helper)의 목적으로만 사용할 수 있다. 즉, 다른 상위 클래스와 메서드를 공유하지 않으며 이전 절에서 언급한 메서드 해석 순서의 모호성을 피한다. 이러한 부모 클래스를 믹스인 클래스라고 한다.
'''
class PrettyMixin() :
    def dump(self) :
        import pprint
        pprint.pprint(vars(self))
class Thing(PrettyMixin) :
    pass

t = Thing()
t.name = "Nyarlathotep"
t.feature = "ichor"
t.age = "eldritch"

print(t.dump())

# 자신 : self
'''
    - 파이썬에서 (공백 사용 외에) 어떤 한 비판은 인스턴스 메서드의 첫 번째 인수로 self를 포함해야 함
'''
# 이전 예제의 Car 클래스에서 exclaim() 메서드를 다시 호출
a_car = Car()
print(a_car.exclaim())

"""
    속성 접근
"""

# 직접 접근
'''
    - 속성 값을 직접 가져와서 설정할 수 있음
'''

class Duck :
    def __init__(self, input_name) :
        self.name = input_name
        
        
fowl = Duck('Daffy')
print(fowl.name)

# 누군가 수정한 경우

fowl.name = 'Daphne'
print(fowl.name)