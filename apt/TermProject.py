from select import select
from tkinter import *
from tkinter import font
from typing import MappingView
import sendMail
import subscriptionInfoAPI
import pprint
import tkintermapview
import spam

textForMap = ''
addressForMap = ''
preSearchKeyword = 0
slist = []
houseNameList = dict()
houseStartApply = dict()#접수
houseEndApply = dict()
housePrizeDate = dict()#당첨자 발표일
houseEngineerCompany = dict()#건설업체
contactStartDate = dict()#계약 시작일
contactEndDate = dict()#계약 종료일

py_modules = ['TermProject']

g_Tk = Tk()
g_Tk.geometry("400x580+450+100") # {width}x{height}+-{xpos}+-{ypos}


def event_for_listbox(event): # 리스트 선택 시 내용 출력
    #selection = event.widget.curselection()
    global listBox
    data = listBox.get(listBox.curselection()[0], listBox.curselection()[0])[0]
    global addressForMap
    global textForMap
    addressForMap = data
    global houseNameList
    textForMap = houseNameList[data]

    global InformationBox
    InformationBox.delete(0, InformationBox.size())
    InformationBox.insert(0,addressForMap)
    InformationBox.insert(1,textForMap)
    InformationBox.insert(2,"예약 시작일: " + houseStartApply[data])
    InformationBox.insert(3,"예약 종료일: " + houseEndApply[data])
    InformationBox.insert(4,"청약 당첨자 발표일: " + housePrizeDate[data])
    InformationBox.insert(5,"건설업체: " + houseEngineerCompany[data])
    InformationBox.insert(6,"계약 종료일: " + contactEndDate[data])
    InformationBox.insert(7,"계약 종료일: " + contactEndDate[data])
    print(addressForMap)
    print(textForMap)
    #얘네 싹 다 검색 창밑에 리스트 박스에 출력할 수 있도록 구현 좀요
    print("예약 시작일: " + houseStartApply[data])
    print("예약 종료일: " + houseEndApply[data])
    print("청약 당첨자 발표일: " + housePrizeDate[data])
    print("건설업체: " + houseEngineerCompany[data])
    print("계약 시작일: " + contactStartDate[data])
    print("계약 종료일: " + contactEndDate[data])


def event_for_searchListbox(event): # 리스트 선택 시 내용 출력
    global SearchListBox
    global preSearchKeyword
    preSearchKeyword = SearchListBox.curselection()[0]    
     

#

def InitScreen(): 
    fontTitle = font.Font(g_Tk, size=18, weight='bold', family = '바탕체')
    fontNormal = font.Font(g_Tk, size=15, weight='bold') 
    # 화면 전체 구도 잡기. 
    frameTitle = Frame(g_Tk, padx=10, pady=10, bg='#4AA8D8')
    frameTitle.pack(side="top", fill="x")
    frameCombo = Frame(g_Tk, pady=10, bg='#4AA8D8')
    frameCombo.pack(side="top", fill="x")
    frameEntry = Frame(g_Tk, pady=10, bg='#4AA8D8')
    frameEntry.pack(side="top", fill="x")
    frameList = Frame(g_Tk, padx=10, pady=10, bg='#4AA8D8')
    frameList.pack(side="top", fill="x")
    framePicture = Frame(g_Tk, padx=10, pady=10, bg='#4AA8D8')
    framePicture.pack(side="top", fill="x")
    frameMap = Frame(g_Tk, padx=10, pady=10, bg='#4AA8D8')
    frameMap.pack(side="top", fill="x")
    
# title 부분
    MainText = Label(frameTitle, font = fontTitle, text="[집 한번 사볼까?]")
    MainText.pack(side="left", fill="x")
    sendEmailButton = Button(frameTitle, font = fontNormal, text='이메일', command = emailWindow)
    sendEmailButton.pack(side='right', padx=10, fill='y')
   # sendEmailButton.bind('<Button-1>', emailWindow)
    global SearchListBox 
    global slist    
    LBScrollbar = Scrollbar(frameCombo)
    SearchListBox = Listbox(frameCombo, font=fontNormal, activestyle='none', width=10, height=1, borderwidth=12, relief='ridge', yscrollcommand=LBScrollbar.set) 
    slist = ["서울", "부산","대전", "대구", "울산", "광주", "인천", "세종", "경기", "강원", "전남", "전북",  "경남", "경북", "제주"]
    for i, s in enumerate(slist): 
        SearchListBox.insert(i, s)
    SearchListBox.pack(side='left', padx=10, expand=True)
    SearchListBox.bind('<<ListboxSelect>>', event_for_searchListbox)
    LBScrollbar.pack(side="left")
    LBScrollbar.config(command=SearchListBox.yview)
    global InputLabel
    InputLabel = Entry(frameCombo, font = fontNormal, \
     width = 10, borderwidth = 12, relief = 'ridge')
    InputLabel.pack(side="left", padx=10, expand=True)
    SearchButton = Button(frameCombo, font = fontNormal, \
    text="검색", command=SearchHouse)
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
    global InformationBox
    InformationBox = Listbox(framePicture, selectmode='extended',\
        font= fontNormal, width=5, height=8, \
        borderwidth=5, relief='ridge')
    #InformationBox.bind('<<ListboxSelect>>', event_for_listbox)
    InformationBox.pack(side='left', anchor='n', expand=True, fill="x")


    # GraphBox = Listbox(framePicture, selectmode='extended',\
    #     font= fontNormal, width=8, height=5, \
    #     borderwidth=5, relief='ridge')
    # GraphBox.bind('<<ListboxSelect>>', event_for_listbox)
    # GraphBox.pack(side="right", padx=10, expand=True, fill='y')
    #지도 부분
    MapButton = Button(frameMap, font = fontNormal, \
    text="지도", command= mapClicked)
    MapButton.pack(side="right", padx=10, expand=True, fill='y')

def onSearch(): # "검색" 버튼 이벤트처리
    # global SearchListBox
    # sels = SearchListBox.curselection()
    # iSearchIndex = 0 if len(sels) == 0 else SearchListBox.curselection()[0]
    # if iSearchIndex >= 5: 
    #     pass
    # else:
    SearchHouse()    
        #subscriptionInfoAPI.getsellAptInfo(sels) # 연결 안됨
        # 유틸리티 함수: 문자열 내용 있을 때만 사용
    



def getStr(s): 
    return '' if not s else s


def SearchHouse(): # "검색" 버튼 -> "도서관"
    i=1
    global houseNameList
    global houseStartApply
    global houseEndApply
    global housePrizeDate
    global houseEngineerCompany
    global contactStartDate
    global contactEndDate
    houseNameList.clear()
    houseStartApply.clear()
    houseEndApply.clear()
    housePrizeDate.clear()
    houseEngineerCompany.clear()
    contactStartDate.clear()
    contactEndDate.clear()
    global preSearchKeyword
    global slist
    res = subscriptionInfoAPI.getsellAptInfo(slist[preSearchKeyword])    
    global listBox
    listBox.delete(0, listBox.size())
    listBox.insert(0, spam.start())
    if res['data'] != None:
        houseNameListT = []
        for x in res['data']:
            a = str(x["HSSPLY_ADRES"])
            if a.find('(') != -1:
                re = a.find('(')
                temp = a[:re - 1]
                a = temp
                print(a)
            if a in houseNameListT:
                continue
            global InputLabel
            if InputLabel.get() != '':
                if InputLabel.get() in a:
                    houseNameListT.append(a)
                    houseNameList[a] = x["HOUSE_NM"]
                    houseStartApply[a] = x["RCEPT_BGNDE"]
                    houseEndApply[a] = x["RCEPT_ENDDE"]
                    housePrizeDate[a] = x["PRZWNER_PRESNATN_DE"]
                    houseEngineerCompany[a] = x["CNSTRCT_ENTRPS_NM"]
                    contactStartDate[a] = x["CNTRCT_CNCLS_BGNDE"]
                    contactEndDate[a] = x["CNTRCT_CNCLS_ENDDE"]
                    listBox.insert(i, a)
                    i = i+1
                
                    
            else:
                houseNameListT.append(a)
                houseNameList[a] = x["HOUSE_NM"]
                houseStartApply[a] = x["RCEPT_BGNDE"]
                houseEndApply[a] = x["RCEPT_ENDDE"]
                housePrizeDate[a] = x["PRZWNER_PRESNATN_DE"]
                houseEngineerCompany[a] = x["CNSTRCT_ENTRPS_NM"]
                contactStartDate[a] = x["CNTRCT_CNCLS_BGNDE"]
                contactEndDate[a] = x["CNTRCT_CNCLS_ENDDE"]
                listBox.insert(i, a)
                i = i+1

            if i==-1:
                listBox.delete(0, listBox.size())
                listBox.insert(0,"검색 결과가 없습니다!" )
        listBox.insert(i, spam.end())
   


def mapClicked():
    mapRoot = Toplevel()
    mapRoot.geometry(f"{600}x{600}") 
    mapwidget = tkintermapview.TkinterMapView(mapRoot, width=800, height=500, corner_radius=0)
    mapwidget.pack()
    global addressForMap
    global textForMap
    marker_1 = mapwidget.set_address(addressForMap, marker=True)
    if not marker_1:
        mapwidget.destroy()
        mapRoot.destroy()
        #지도를 표시할 수 없습니다 표기gui에 표시할거
        global g_Tk    
        toplevel=Toplevel(g_Tk)
        frameTitle = Frame(toplevel, padx=10, pady=10, bg='#bfff00')
        frameTitle.pack(side="top", fill="x")
        fontNormal = font.Font(toplevel, size=15, weight='bold')
        toplevel.geometry("330x70+820+100")
        global guibox
        guibox = Listbox(frameTitle, selectmode='extended',\
        font= fontNormal, width=5, height=8, \
        borderwidth=5, relief='ridge')
    #InformationBox.bind('<<ListboxSelect>>', event_for_listbox)
        guibox.pack(side='left', anchor='n', expand=True, fill="x")
        guibox.delete(0, guibox.size())
        guibox.insert(0,"지도gui를 띄울 수 없습니다!");
        return
    marker_1.set_text(textForMap)
    mapwidget.set_zoom(15)
    

#이메일 버튼 클릭시 불리는 콜백 함수
def emailWindow():
    global g_Tk    
    toplevel=Toplevel(g_Tk)
    frameTitle = Frame(toplevel, padx=10, pady=10, bg='#bfff00')
    frameTitle.pack(side="top", fill="x")
    fontNormal = font.Font(toplevel, size=15, weight='bold')
    global InputEmail 
    toplevel.geometry("550x70+820+100")
    InputEmail = Entry(frameTitle, font = fontNormal, \
    width = 30, borderwidth = 12, relief = 'ridge')
    InputEmail.pack(side="left", padx=10, expand=True)
    SearchButton = Button(frameTitle, font = fontNormal, \
    text="발송", command=onEmail)
    SearchButton.pack(side="right", padx=10, expand=True, fill='y')
    global EmailBox
    EmailBox = Listbox(frameTitle, selectmode='extended',\
        font= fontNormal, width=5, height=8, \
        borderwidth=5, relief='ridge')
    #InformationBox.bind('<<ListboxSelect>>', event_for_listbox)
    EmailBox.pack(side='left', anchor='n', expand=True, fill="x")
     
    
def onEmail():
    inputReceiveMail = InputEmail.get() # 이메일 입력 받고서 이 변수에 저장
    global EmailBox
    if inputReceiveMail.find('@') == -1:
        EmailBox.delete(0, EmailBox.size())
        EmailBox.insert(0,"실패")
        #여기에 메일 주소 잘못됐다고 나오는 출력
        
        return
    inputText = ''#내용을 여기에 삽입
    global textForMap
    global addressForMap
    inputAptName = textForMap#메일에 들어갈 아파트 이름
    inputRegion= addressForMap#아파트 위치
    # mapRoot = Toplevel()
    # mapRoot.geometry(f"{600}x{600}") 
    # mapwidget = tkintermapview.TkinterMapView(mapRoot, width=800, height=500, corner_radius=0)
    # mapwidget.pack()
    # marker_1 = mapwidget.set_address(inputRegion, marker=True)
    # if not marker_1:
    #     mapwidget.destroy()
    #     mapRoot.destroy()
    #     # 이때 청약 주소 정보가 정확하지 않아 보낼 수 없습니다. 출력
    #     return
    # else:
    #     mapwidget.destroy()
    #     mapRoot.destroy()
    if inputAptName == '' or inputRegion == '':
       pass
       #내용을 검색 후 이용해주세요. 출력
    else:
        sendMail.clickEmail(inputReceiveMail,aptName = inputAptName, region = inputRegion, startApply = houseStartApply[inputRegion], \
           EndApply = houseEndApply[inputRegion], housePrizeDate = housePrizeDate[inputRegion], houseEngie = houseEngineerCompany[inputRegion],\
                contactStart = contactStartDate[inputRegion], contactEnd = contactEndDate[inputRegion])
        EmailBox.delete(0, EmailBox.size())
        EmailBox.insert(0,"성공")



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
