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
import shutil
global currentDir 
currentDir = os.getcwd()
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
    temp = list()
    for urls in pl.video_urls:
        temp.append(urls)
    modifiedUrls = temp.copy()
    for elements in names:
        if elements in temp:
            modifiedUrls.remove(elements)
    f = open("./config/setting.txt",'w')
    f.write('playlist Url\n')
    f.write(url+"\n")
    f.write("names\n")
    for i in modifiedUrls:
        f.write(i+"\n")
    f.close()
    return modifiedUrls
def musicDownloader(url):
    if(len(url)==0):
        print('sync already complete')
        return
    if(os.path.isdir(currentDir+"/music")==True):
        shutil.rmtree(currentDir+"/music")
    else:
        os.mkdir('music')
    
#main
print("-------------------")
print("   Python Syncer   ")
print("-------------------")
print("Checking setting file...")
#초기 실행인지 확인
if(os.path.isfile(currentDir+"/config/setting.txt")==True):
    #초기 실행 아님
    print("Setting Detected...")
    print("load setting")
    playlistUrl, names = loadSetting()
    modifiedUrls = nameInsertor(playlistUrl, names)
else:
    print("start setting...")
    playlistUrl, names = createSetting()
    modifiedUrls = nameInsertor(playlistUrl, names)