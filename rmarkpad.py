from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import keyboard
import os
import string as str
import subprocess

nowfile = ''
rf = open('./r.txt', 'r', encoding='UTF-8')
rpath = rf.readline()
rf.close

def seeend() :
    text.see(END)
    otext.see(END)

def resize(event):
   
    pixelX=window.winfo_width()-yscrollbar.winfo_width()
    pixelY=window.winfo_height()
    text["width"]=int(round(pixelX/h[1]))
    text["height"]=int(round(pixelY/h[0]))
    otext["width"]=int(round(pixelX/h[1]))
    otext["height"]=7

def o_empty():
    otext.delete('1.0', END)
    f = open("./temp.r", 'w', encoding="UTF-8")
    f.write("")
    f.close

def fopen():
	#파일 대화창을 askopenfile을 이용해서 만들고, 동시에 읽는다
    nfile = filedialog.askopenfilename(parent=window)
    file = open(nfile, 'r', encoding='euc-kr')
    global nowfile
    nowfile = file.name
    window.title(nowfile)
    if file != None:
        lines = file.read()
        # 1.0은 line.column이다.
        #line은 1부터 시작하고 column은 0부터 시작함..
        text.insert('1.0', lines)
        file.close()
    o_empty()
    seeend()
        
def save():
	#쓰고 저장하는 기능
    nfile = filedialog.asksaveasfilename(parent=window)
    file = open(nfile, 'w', encoding='euc-kr')
    global nowfile
    nowfile = file.name
    window.title(nowfile)
    if file != None:
        lines = text.get('1.0', END+'-1c') # 마지막에서 1 char 뺀다, \n제거!
        file.write(lines)
        file.close()

def qsave():
    #쓰고 저장하는 기능
    if nowfile != '' :
        try :
            file = open(nowfile, 'w')
            if file != None:
                lines = text.get('1.0', END+'-1c') # 마지막에서 1 char 뺀다, \n제거!
                file.write(lines)
                file.close()
        except : return 0
    elif nowfile == '' :
        save()
        
def exit():
    if messagebox.askokcancel("Quit", "Sure quit?"):
        window.destroy()
        
def about():
    label = messagebox.showinfo("About", "RPad v0.1 (c) 2023 Hyeok Jeong")

def rse():
    label = messagebox.showinfo("Rscript", rpath)

def runcom():
    target = text.get("1.0","insert lineend")
    try : 
        exec(compile(target, '<string>', 'exec'))
    except Exception as e :
        print(e)

def runr():
    otext.delete('1.0', END)
    f = open("./temp.r", 'a', encoding="UTF-8")
    otarget = text.get('1.0', "insert linestart")
    ntarget = text.get("insert linestart", END)
    try :
        otarget = otarget.split(sep="```")
        ntarget = ntarget.split(sep="```")
        ftarget = otarget[len(otarget)-1] + ntarget[0]
        ftarget = ftarget.split(sep='\n', maxsplit=1)
        f.write(ftarget[1])
        f.close()
        output = subprocess.getoutput("\"" + rpath + "\" temp.r")
        otext.insert('1.0', output)
    except : otext.insert('1.0', "Rpad typeerror")
    otext.see(END)

def runa():
    o_empty()
    otext.delete('1.0', END)
    try :
        f = open("./temps.r", 'a', encoding="UTF-8")
        otarget = text.get('1.0', END).split(sep="```")
        for i in range(len(otarget)) :
            if i % 2 != 0 :
                f.write(otarget[i])
        f.close()        
    except : otext.insert('1.0', "Rpad typeerror 1")
    try :
        f1 = open("./temps.r", 'r', encoding='UTF-8')
        f2 = open("./temp.r", 'a', encoding='UTF-8')
        while True :
            inStr = f1.readline()
            if inStr == '' :
                break
            if inStr[0] != "{" :
                f2.write(inStr)
        f1.close()
        f2.close()
    except Exception as e : otext.insert('1.0', e)
    try :
        output = subprocess.getoutput("\"" + rpath + "\" temp.r")
        otext.insert('1.0', output)
    except : otext.insert('1.0', "Rpad typeerror 3")
    seeend()

def cppdf() :
    cpfile = filedialog.askopenfilename(parent=window)
    f = open("./render.r", 'w', encoding="UTF-8")
    f.write("rmarkdown::render(\"" + cpfile + "\", \"pdf_document\")")
    f.close()
    try :
        output = subprocess.getoutput("\"" + rpath + "\" render.r")
        otext.insert('1.0', output)
    except : otext.insert('1.0', "Rpad typeerror")
    otext.see(END)

def cpdocx() :
    cpfile = filedialog.askopenfilename(parent=window)
    f = open("./render.r", 'w', encoding="UTF-8")
    f.write("rmarkdown::render(\"" + cpfile + "\", \"word_document\")")
    f.close()
    try :
        output = subprocess.getoutput("\"" + rpath + "\" render.r")
        otext.insert('1.0', output)
    except : otext.insert('1.0', "Rpad typeerror")
    otext.see(END)

def cphtml() :
    cpfile = filedialog.askopenfilename(parent=window)
    f = open("./render.r", 'w', encoding="UTF-8")
    f.write("rmarkdown::render(\"" + cpfile + "\", \"html_document\")")
    f.close()
    try :
        output = subprocess.getoutput("\"" + rpath + "\" render.r")
        otext.insert('1.0', output)
    except : otext.insert('1.0', "Rpad typeerror")
    otext.see(END)

def frse() :
    rsefile = filedialog.askopenfilename(parent=window)
    f = open("./r.txt", 'w', encoding="UTF-8")
    f.write(rsefile)
    global rpath
    rpath = rsefile

def newfile() :
    file = open("./templete.Rmd", 'r', encoding="UTF-8")
    global nowfile
    nowfile = ''
    window.title("Rpad Beta - Unsaved Document")
    if file != None:
        lines = file.read()
        # 1.0은 line.column이다.
        #line은 1부터 시작하고 column은 0부터 시작함..
        text.insert('1.0', lines)
        file.close()
    o_empty()
    seeend()


#창 생성
window = Tk()
window.title('RPad Beta')
window.geometry('1024x768')
window.iconbitmap('rpadico.ico')
window.resizable(1,1)

text = Text(window, undo=True)
text.grid(row=0, column=0, sticky=W+N+S)
text.configure(font=("Consolas", 16, "bold"))

yscrollbar = Scrollbar(window, orient=VERTICAL, command=text.yview)
yscrollbar.grid(row=0, column=1, sticky=N+S+E+W)
text["yscrollcommand"]=yscrollbar.set
text.update()


otext = Text(window, undo=True)
otext.grid(row=1, column=0, sticky=W+N+S)
otext.configure(font=("Consolas", 16, "bold"))

oyscrollbar = Scrollbar(window, orient=VERTICAL, command=otext.yview)
oyscrollbar.grid(row=1, column=1, sticky=N+S+E+W)
otext["yscrollcommand"]=oyscrollbar.set
otext.update()

h=int(round(text.winfo_height()/text["height"])), int(round(text.winfo_width()/text["width"]))

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
#text.pack()

#메뉴를 붙인다
menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)
runmenu = Menu(menu)
cpmenu = Menu(menu)

menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New File", command=newfile)
filemenu.add_command(label="Open...   (Ctrl+O)", command=fopen)
filemenu.add_command(label="Save as...   (Ctrl+Shift+S)", command=save)
filemenu.add_command(label="Find Rscript.exe", command=frse)
filemenu.add_command(label="Kill queues   (Ctrl+E)", command=o_empty)
filemenu.add_command(label="Quit   (Alt+F4)", command=exit)

menu.add_cascade(label="Run", menu=runmenu)
runmenu.add_command(label="Run current block only...   (Ctrl+R)", command=runr)
runmenu.add_command(label="Run all blocks...   (Ctrl+Shift+R)", command=runa)

menu.add_cascade(label="Knit", menu=cpmenu)
cpmenu.add_command(label="Word Document (.docx)", command=cpdocx)
cpmenu.add_command(label="Html Document (.html)", command=cphtml)

helpmenu = Menu(menu, tearoff=0) # 자르는 선

menu.add_cascade(label="About", menu=helpmenu)
helpmenu.add_command(label="About RPad", command=about)
helpmenu.add_command(label="Rscript.exe", command=rse)

window.bind("<Configure>", resize)
    
keyboard.add_hotkey("ctrl+s", lambda: qsave())
keyboard.add_hotkey("ctrl+shift+s", lambda: save())
keyboard.add_hotkey("ctrl+o", lambda: fopen())
keyboard.add_hotkey("alt+F4", lambda: quit())
keyboard.add_hotkey("ctrl+r", lambda: runr())
keyboard.add_hotkey("ctrl+shift+r", lambda: runa())
keyboard.add_hotkey("ctrl+e", lambda: o_empty())

window.mainloop()

#단어 찾기
#단어 치환
#앞으로 마크
#뒤로 마크