"""
파이썬 유튜브 재생목록 매니저
ver 0.0.1
사용 library: 
 pytube
이름 규칙
변수, 함수 : camelCase
클래스 : PascalCase
상수 : UPPER_CASE
비공개 멤버 변수 : 밑줄로 시작하는 접두사
"""
import pytube
import os

#class
#function
def loadSetting():#초기 실행이 아닐 때 세팅을 불러오는 함수
    f=open("./config/setting.txt",'r')
    temp1 = f.readline()
    playlistUrl = f.readline()
    temp2 = f.readline()
    names = list()
    while(True):
        data = f.readline()
        if not data: break
        names.append(data.strip())
    return playlistUrl, names
    f.close()
def createSetting():#초기 실행일 때 세팅을 만드는 함수
    os.mkdir("config")
    f = open("./config/setting.txt",'w')
    f.write('playlist Url\n')
    playlistUrl=input("Enter url of playlist to sync : ")
    f.write(playlistUrl+'\n')
    f.close()
    print("setting complete...")
    names = list()
    return playlistUrl, names
def nameInsertor(url, names):#이미 다운 받은 곡들을 배제한다
    print('Looking for songs to download...')
    pl = pytube.Playlist(url)
    #url 따서 이름 추출 후 기존 names 와 비교
#main
print("-------------------")
print("   Python Syncer   ")
print("-------------------")
print("Checking setting file...")
currentDir = os.getcwd()
#초기 실행인지 확인
if(os.path.isfile(currentDir+"/config/setting.txt")==True):
    #초기 실행 아님
    print("Setting Detected...")
    print("load setting")
    playlistUrl, names = loadSetting()
else:
    print("start setting...")
    playlistUrl, names = createSetting()