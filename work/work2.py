# <- 주석 표시
# \ <- 라인 유지, \ 뒤에는 공백도 포함할 수 없다.
sum = 1 + \
    2
print(sum) 

# 비교하기
# if, elif, else
disaster = True
if disaster :
    print("Woe!!!")
else :
    print("Whee!!!")

####
furry = True
large = False
if furry :
    if large :
        print("It's a yeti!!")
    else :
        print("It's a coke!!")
else :
    if large : 
        print("It's a whale!!")
    else :
        print("It's is human.")

#### 세가지 이상의 경우일 때
# if
# elif
# else

some_list = []
if some_list :
    print ("There's something in here")
else :
    print ("It's empty!!")
    
    
# python 3.8 : 바다코끼리 연산자 (:=)