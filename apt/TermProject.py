from tkinter import *
from tkinter import font
from typing import MappingView
import sendMail
import subscriptionInfoAPI
import pprint
#import atpMapRegion

g_Tk = Tk()
g_Tk.geometry("400x600+450+100") # {width}x{height}+-{xpos}+-{ypos}
def event_for_listbox(event): # 리스트 선택 시 내용 출력
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        print(data) 
def InitScreen(): 
    fontTitle = font.Font(g_Tk, size=18, weight='bold', family = '바탕체')
    fontNormal = font.Font(g_Tk, size=15, weight='bold')
    # 화면 전체 구도 잡기. 
    frameTitle = Frame(g_Tk, padx=10, pady=10, bg='#ff0000')
    frameTitle.pack(side="top", fill="x")
    frameCombo = Frame(g_Tk, pady=10, bg='#00ff00')
    frameCombo.pack(side="top", fill="x")
    frameEntry = Frame(g_Tk, pady=10, bg='#0000ff')
    frameEntry.pack(side="top", fill="x")
    frameList = Frame(g_Tk, padx=10, pady=10, bg='#ffff00')
    frameList.pack(side="top", fill="x")
    framePicture = Frame(g_Tk, padx=10, pady=10, bg='red')
    framePicture.pack(side="top", fill="x")
    frameMap = Frame(g_Tk, padx=10, pady=10, bg='red')
    frameMap.pack(side="top", fill="x")
    
# title 부분
    MainText = Label(frameTitle, font = fontTitle, text="[집 한번 사볼까?]")
    MainText.pack(side="left", fill="x")
    sendEmailButton = Button(frameTitle, font = fontNormal, text='이메일') 
    sendEmailButton.pack(side='right', padx=10, fill='y')
    sendEmailButton.bind('<Button-1>', emailWindow)
    global SearchListBox 
    LBScrollbar = Scrollbar(frameCombo)
    SearchListBox = Listbox(frameCombo, \
    font=fontNormal, activestyle='none', width=10, height=1, borderwidth=12, relief='ridge', yscrollcommand=LBScrollbar.set) 
    slist = ["서울", "경기도", "강원도", "부산","동탄"]
    for i, s in enumerate(slist): SearchListBox.insert(i, s)
    SearchListBox.pack(side='left', padx=10, expand=True)
    LBScrollbar.pack(side="left")
    LBScrollbar.config(command=SearchListBox.yview)
    global InputLabel
    InputLabel = Entry(frameCombo, font = fontNormal, \
     width = 10, borderwidth = 12, relief = 'ridge')
    InputLabel.pack(side="left", padx=10, expand=True)
    SearchButton = Button(frameCombo, font = fontNormal, \
    text="검색", command=onSearch)
    SearchButton.pack(side="right", padx=10, expand=True, fill='y')
    # 사용자 입력 부분
    
    
    # 목록 부분
    global listBox
    LBScrollbar = Scrollbar(frameList)
    listBox = Listbox(frameList, selectmode='extended',\
        font= fontNormal, width=5, height=5, \
        borderwidth=5, relief='ridge')
    listBox.bind('<<ListboxSelect>>', event_for_listbox)
    listBox.pack(side='left', anchor='n', expand=True, fill="x")
    # listBox2 = Listbox(frameList, selectmode='extended',\
    #     font= fontNormal, width=8, height=5, \
    #     borderwidth=5, relief='ridge')
    # listBox2.bind('<<ListboxSelect>>', event_for_listbox)
    # listBox2.pack(side="right", padx=10, expand=True, fill='y')
    #사진 부분
    global graph
    PictureBox = Listbox(framePicture, selectmode='extended',\
        font= fontNormal, width=5, height=5, \
        borderwidth=5, relief='ridge')
    PictureBox.bind('<<ListboxSelect>>', event_for_listbox)
    PictureBox.pack(side='left', anchor='n', expand=True, fill="x")
    GraphBox = Listbox(framePicture, selectmode='extended',\
        font= fontNormal, width=8, height=5, \
        borderwidth=5, relief='ridge')
    GraphBox.bind('<<ListboxSelect>>', event_for_listbox)
    GraphBox.pack(side="right", padx=10, expand=True, fill='y')
    #지도 부분
    MapButton = Button(frameMap, font = fontNormal, \
    text="지도", command=onSearch)
    MapButton.pack(side="right", padx=10, expand=True, fill='y')

def onSearch(): # "검색" 버튼 이벤트처리
    global SearchListBox
    sels = SearchListBox.curselection()
    iSearchIndex = 0 if len(sels) == 0 else SearchListBox.curselection()[0]
    if iSearchIndex == 0: 
        SearchLibrary()
    elif iSearchIndex == 1:
        pass 
    elif iSearchIndex == 2:
        pass 
    elif iSearchIndex == 3:
        global InputLabel
        print(InputLabel.get())
        #subscriptionInfoAPI.getsellAptInfo(sels) # 연결 안됨
        pass # 유틸리티 함수: 문자열 내용 있을 때만 사용


def getStr(s): 
    return '' if not s else s
def SearchLibrary(): # "검색" 버튼 -> "도서관"
    i=1
    res = subscriptionInfoAPI.getsellAptInfo(InputLabel.get())
    if res['data'] != None:
        for x in res['data']:
            x["HOUSE_NM"]
            x["HSSPLY_ADRES"]
            a = str(x["HSSPLY_ADRES"])
            if a.find('(') != -1:
                re = a.find('(')
                a = list(a)
                del(a[re:len(a)])        
                a = str(a)
                #print(a)

                
        listBox.insert(i-1, a)
    i = i+1


#이메일 버튼 클릭시 불리는 콜백 함수
def emailWindow():
    inputReceiveMail = '' # 이메일 입력 받고서 이 변수에 저장
    inputText = ''#내용을 여기에 삽입
    inputAptName = ''#메일에 들어갈 아파트 이름
    inputRegion= ''#아파트 위치

    #sendMail.clickEmail(inputReceiveMail, inputAptName, inputRegion)
    




## 서울 검색시 결과

#root = Tk()
#root.geometry(f"{600}x{600}") 
# res = subscriptionInfoAPI.getsellAptInfo("서울")
# if res['data'] != None:
#     for x in res['data']:
#         print(x["HOUSE_NM"])
#         print(x["HSSPLY_ADRES"])
#         a = str(x["HSSPLY_ADRES"])
#         if a.find('(') != -1:
#             re = a.find('(')
#             a = list(a)
#             del(a[re:len(a)])        
#             a = str(a)
#         print(a)
        #m = atpMapRegion.mapWidget(root)
        #m.set_address(a)
#root.mainloop() 
#root.mainloop() 
#print(listBox)
InitScreen() # 화면 전체 구성
g_Tk.mainloop()
