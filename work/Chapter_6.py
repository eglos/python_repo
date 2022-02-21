# 반복하기 : while
print('='*10)
count = 1
while count <= 5 :
    print(count)
    count += 1 # count = count + 1
    
print('='*10)
# 중단 : break
while True : 
    stuff = input("String to capitalize [type q to quit:] ") # 입력 함수
    if stuff == "q" :
        break #위의 if문이 true 일 경우, 반복문 종료
    print (stuff.capitalize())
    
    
# 건너뛰기 : continue
# 정수가 홀수일 때는 그 수의 제곱 출력, 짝수일 때는 다음 반복으로 건너뛰기
print('='*10)
while True :
    value = input("Integer, please [q to quit] :")
    if value == 'q' : #종료
        print("The end")
        break
    number = int(value)
    if number % 2 == 0 : #2로 나눈 나머지가 0 = 짝수
        continue
    print(number, "squared_is ",number*number)
    
# break  확인하기 : else
# while 문에서 else 문 사용이 직관적이지 않을 수 있음. else 문을 그냥 브레이크 체커(break checker)라고 생각.
print('='*10)
numbers = [1,3,5]
position = 0
while position < len(numbers) :
    number = numbers[position]
    if number % 2 == 0 :
        print('Found even number ', number)
        break
    position += 1
else : # break문이 호출되지 않은 경우
        print('No even number found')
        
# 순회 하기 : for 와 in
# 파이썬에서 이터레이터(iterator)는 유용하게 자주 쓰임.
# 데이터가 메모리에 맞지 않더라도 데이터 스트림을 처리할 수 있도록 허용해줌.

word = 'thud'
for letter in word : 
    print(letter) #한번에 한 문자를 생성
 
print('='*10)   

for letter in word : 
    if letter == 'u' :
        break #break 문 추가
    print(letter)
    
print('='*10)   

for letter in word : 
    if letter == 'x' :
        print("Eek! An 'x'!")
        break
    print(letter)
else :
        print("No 'x' in there.")
        
# 숫자 시퀀스 생성하기 : range()
# 1) range() 함수는 리스트나 튜플 같은 자료구조를 생성하여 저장하지 않더라도 특정 범위 내에서 숫자 스트림 반환
# 2) 슬라이스[slice()] 사용법과 비슷
# range(start,stop,step)

for x in range(0,3) : #0부터 (3-1)까지
    print(x)
    

# 2에서 0의 리스트 (거꾸로 진행)
for x in range(2,-1,-1) :
    print(x)


# 연습문제 6.1
list = []
for t in range(3,-1,-1) :
    list.append(t)
    
print(list)

# 연습문제 6.2
guess_me = 7
number = 1

while True :
    if number < guess_me :
        print('too low')
    elif number == guess_me :
        print('found it!')
        break
    else :
        print('oops')
    number += 1
