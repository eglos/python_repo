'''
파일과 디렉터리
    - 파일은 일련의 바이트이며 일부 파일 시스템에 저장되어 파일 이름으로 접근
'''

# 파일 입출력
# 생성하기/열기 : open()
'''
    - open() 함수는 다음 내용을 수행
        - 기존 파일 읽기
        - 새 파일 쓰기
        - 기존 파일에 추가하기
        - 기존 파일 덮어쓰기
'''

fout = open('oops.txt','wt') # 상위 경로에 파일이 생김
fout.close()
'''
    fileobj = open(filename, mode)
    
    mode의 첫번째 글자
        r : 파일 읽기
        w : 파일 쓰기 (파일이 존재하지 않으면 파일을 생성하고, 파일이 존재하면 덮어쓴다.)
        x : 파일 쓰기 (파일이 존재하지 않을 경우에만 해당한다.)
        a : 파일 추가하기 (파일이 존재하면 파일의 끝에서부터 쓴다.)
        
    mode의 두번째 글자
        t(또는 아무것도 명시하지 않음) : txt 타입
        b : 이진 타입
'''

# 텍스트 파일 쓰기 : print()
fout = open('oops.txt','wt')
print('Oops, I created a file.', file=fout)
fout.close()

# 텍스트 파일 쓰기 : write()
poem = ''' There was a young lady named Bright,
... Whose speed was far faster than light;
... She started one day
... In a relative way,
... And returned on the previous night.'''

print(len(poem))

fout = open('relativity','wt')
fout.write(poem) #write는 파일에 쓴 바이트를 반환
fout.close()

fout = open('relativity','wt')
print(poem, file=fout, sep='', end='')
fout.close()

# 파일에 쓸 문자열이 크면 특정 단위(chunk)로 나누어서 파일에 쓴다.
fout = open('relativity', 'wt')
size =len(poem)
offset = 0
chunk = 100
while True :
    if offset > size :
        break
    fout.write(poem[offset:offset+chunk])
    offset += chunk
    
fout.close()

# 텍스트 파일 읽기 : read(), readline(), readlines()
fin = open('relativity','rt')
poem = fin.read()
fin.close()
len(poem)


# 한번에 100 문자를 읽은 뒤 각 chunk문자열을 poem 문자열에 추가하여 원본 파일의 문자열을 모두 저장
poem = ''
fin = open('relativity','rt')
chunk = 100
while True :
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment

fin.close()
print(len(poem))

# readline() 함수를 사용하여 파일을 줄 단위로 읽을 수 있다.
poem = ''
fin = open('relativity','rt')
while True :
    line = fin.readline()
    if not line :
        break
    poem += line

fin.close()
print(len(poem))

# readlines()는 한 번에 모든 줄을 읽고, 한 줄로 된 문자열 리스트를 반환한다.
fin = open('relativity','rt')
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')
for line in lines :
    print(line, end='')
    

# 이진 파일 쓰기 : write()
'''
    - 모드(mode)에 'b'를 포함하면 파일은 이진 모드로 열린다.
    - 이때 문자열 대신 바이트를 읽고 쓸 수 있다.
'''

bdata = bytes(range(0,256))
print(len(bdata))
fout = open('bfile','wb')
fout.write(bdata)
fout.close()
print('=================')

fout = open('bfile','wb')
size = len(bdata)
offset = 0
chunk = 100
while True :
    if offset > size :
        break
    fout.write(bdata[offset:offset+chunk])
    offset += chunk
    print(offset)

fout.close()

# 이진 파일 읽기 : read()

fin = open('bfile','rb')
bdata = fin.read()
print('fin len=',len(bdata))
fin.close()

# 자동으로 파일 닫기 : with
'''
    - 열려있는 파일을 닫지 않았을 때, 파이썬은 이 파일이 더 이상 참조되지 않는 것을 확인한 뒤 파일을 닫는다.
    - 파이썬은 파일을 여는 것과 같은 일을 수행하는 컨텍스트 매니저(context manager)가 있다. 
    - 파일을 열 때 'with 표현식 as 변수' 형식을 사용한다.
'''
with open('relativity','wt') as fout : #컨텍스트 매니저 코드 블록의 코드 한 줄이 실행되고 나서 (잘 수행되거나 문제가 있으면 예외 발생) 자동으로 파일을 닫아준다.
    fout.write(poem)

# 파일 위치 찾기 : seek()
'''
    - seek() 함수는 다른 바이트 오프셋으로 위치를 이동
    - seek() 함수 형식은 seek(offset, origin)이며, 두번째 인수 origin에 대한 설명
        * origin이 0일 때, 시작 위치에서 offset 바이트로 이동
        * origin이 1일 때, 현재 위치에서 offset 바이트로 이동
        * origin이 2일 때, 마지막 위치에서 offset 바이트 전 위치로 이동
'''

# 존재 여부 확인하기 : exists()
'''
    - 파일 혹은 디렉터리가 실제로 존재하는지 확인
'''
import os
print(os.path.exists('oops.txt'))

print(os.path.exists('./oops.txt'))

# 유형 확인하기 : isfile()
name = 'oops.txt'
print(os.path.isfile(name))

# 복사하기 : copy()
import shutil
shutil.copy('oops.txt','ohno.txt')

# 이름 바꾸기: rename()
import os
#os.rename('ohno.txt','ohwell.txt')


# 연결하기 : link(), symlink()
'''
    - link() : 저수준의 하드링크
    - symlink() : 새 이름의 원본 파일을 저장하는 대안
'''

#os.link('oops.txt','yikes.txt')
print(os.path.isfile('yikes.txt'))
print(os.path.islink('yikes.txt'))

#os.symlink('oops.txt','jeepers.txt') # 기능이 안됨.  [WinError 1314] 클라이언트가 필요한 권한을 가지고 있지 않습니다
os.path.islink('jeepers.txt')

