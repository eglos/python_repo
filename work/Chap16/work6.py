import xml.etree.ElementTree as et
# import os
# currentpath = os.getcwd()
# print(currentpath)
# print('===================')
tree =et.ElementTree(file='C:/Users/Mine/Desktop/git/python_repo/work/Chap16/menu.xml')
root = tree.getroot()
print(root.tag)

for child in root :
    print('tag:', child.tag, 'attributes:', child.attrib)
    for grandchild in child :
        print('\ttag:', grandchild.tag, 'attributs:', grandchild.attrib)
'''
    - tag : tag 문자열
    - attrib : 속성의 딕셔너리
'''
'''
    기타 표준 파이썬 XML 라이브러리
        - xml.dom : 자바 스크립트 개발자에게 친숙한 문서 객체 모델(Document Object Model)은 웹 문서를 계층 구조로 나타낸다. 이 모듈은 전체 XML 파일을 메모리에 로딩하여 XML 모든 항목을 접근할 수 있다.
        - xml.sax : XML용 API(Simple API for XML)는 즉시 XML을 파싱하므로 한 번에 전체 XML 파일을 메모리에 로딩하지 않는다. 매우 큰 XML 스트림을 처리해야 한다면 이 모듈을 사용하는 것이 좋다.
'''

