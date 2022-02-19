# 가변성
# 타입에 따라 값을 변경할 수 있다.


# 파이썬에서 데이터 값을 명시하는 두가지 방법 : 1) 리터럴 2) 변수

#예약어 명령어
help("keywords")
#또는
import keyword
from re import X
keyword.kwlist

#y = x + 12 는 x 값이 없으므로 에러 발생

a = 7
print(a)

b = a
print(b)

type(7)

# class : 객체의 정의


# 두 개 이상의 변수 이름에 동시에 값 할당
one = two = three = 1
print(one)
print(two)
print(three)

# boolean
# bool은 0이 아닌 값은 True로 return

t = bool(1)
print(t)


# 정수
# 첫번째 숫자 이후 모든 위치에 언더바(_) 사용 가능
x = 5_11
print(x) # 511


# 진수

value = 65
print(bin(value))

print(oct(value))

print(hex(value))

print(chr(65))

