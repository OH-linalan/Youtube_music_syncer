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
def loadSetting():
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
    print(playlistUrl)
    print(names)
