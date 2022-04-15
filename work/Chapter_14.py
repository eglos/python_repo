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
    