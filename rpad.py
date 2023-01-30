from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.messagebox import askyesno
import subprocess
import pyglet
import rpy2.robjects as robjects

def seeend() :
    text.see(END)
    otext.see(END)

def confirm():
    ans = askyesno(title='Exit', message='Exit Rpad without saving?')
    if ans:
        window.destroy()

def resize(event):
    pixelX=window.winfo_width()-yscrollbar.winfo_width()
    pixelY=window.winfo_height()
    text["width"]=int(round(pixelX/h[1]))
    text["height"]=int(round(pixelY/h[0]))
    otext["width"]=int(round(pixelX/h[1]))
    otext["height"]=7

def o_empty():
    otext.delete('1.0', END)

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
    label = messagebox.showinfo("About", "RPad v0.2 (c) 2023 Hyeok Jeong")

def rse():
    label = messagebox.showinfo("Rscript", rpath)

def runcom():
    target = text.get("1.0","insert lineend")
    try : 
        exec(compile(target, '<string>', 'exec'))
    except Exception as e :
        print(e)

def runr():
    otext.delete('insert linestart', 'insert lineend')
    try:
        tline = text.get('insert linestart', 'insert lineend')
        rline = robjects.r(tline)
        otext.insert('1.0', rline)
        seeend()
        qsave()
    except : otext.insert('1.0', "Rpad typeerror")

def runa():
    otext.delete('1.0', END)
    try:
        tline = text.get('insert linestart', 'insert lineend')
        rline = robjects.r(tline)
        otext.insert('1.0', rline)
        seeend()
        qsave()
    except : otext.insert('1.0', "Rpad typeerror")

def newfile() :
    file = open("./data/templete.Rmd", 'r', encoding="UTF-8")
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

def frse() :
    rsefile = filedialog.askopenfilename(parent=window)
    f = open("./data/r.txt", 'w', encoding="UTF-8")
    f.write(rsefile)
    global rpath
    rpath = rsefile

def mfont():
    try :
        var1 = int(text.get('insert linestart', 'insert lineend'))
        text.configure(font=("Pretendard Variable Medium", var1))
        otext.configure(font=("Pretendard Variable Medium", var1))
        text.update()
        otext.update()
        text.delete('insert linestart', 'insert lineend')
    except : otext.insert('1.0', "fontsize typeerror")

pyglet.font.add_file('./font/PretendardVariable.ttf')

nowfile = ''
rf = open('./data/r.txt', 'r', encoding='UTF-8')
rpath = rf.readline()
rf.close

#창 생성
window = Tk()
window.title('Rpad Beta')
window.geometry('1024x768')
window.iconbitmap('./data/rpadico.ico')
window.resizable(1,1)

text = Text(master=window, undo=True, fg="#CCCCCC", bg="#202020", insertbackground="#CCCCCC", selectbackground="#007F0E")
text.grid(row=0, column=0, sticky=W+N+S+E)
text.configure(font=("Pretendard Variable Medium", 20))

yscrollbar = Scrollbar(window, orient=VERTICAL, command=text.yview)
yscrollbar.grid(row=0, column=1, sticky=N+S+E+W)
text["yscrollcommand"]=yscrollbar.set
text.update()

text.bind("<Control-s>", lambda event: qsave())
text.bind("<Control-o>", lambda event: fopen())
text.bind("<Control-r>", lambda event: runr())
text.bind("<Control-Shift-KeyPress-R>", lambda event: runa())
text.bind("<Control-e>", lambda event: o_empty())
text.bind("<Alt-t>", lambda event: mfont())


otext = Text(master=window, undo=True, fg="#7FFFFF", bg="#202020", insertbackground="#7FFFFF", selectbackground="#007F0E")
otext.grid(row=1, column=0, sticky=W+N+S+E)
otext.configure(font=("Pretendard Variable Medium", 20))

oyscrollbar = Scrollbar(window, orient=VERTICAL, command=otext.yview)
oyscrollbar.grid(row=1, column=1, sticky=N+S+E+W)
otext["yscrollcommand"]=oyscrollbar.set
otext.update()

h=int(round(text.winfo_height()/text["height"])), int(round(text.winfo_width()/text["width"]))

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

#메뉴를 붙인다
menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)
runmenu = Menu(menu)

menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New File", command=newfile)
filemenu.add_command(label="Open...   (Ctrl+O)", command=fopen)
filemenu.add_command(label="Save as...", command=save)
filemenu.add_command(label="Find Rscript", command=frse)
filemenu.add_command(label="Kill queues   (Ctrl+E)", command=o_empty)
filemenu.add_command(label="Quit", command=exit)

menu.add_cascade(label="Run", menu=runmenu)
runmenu.add_command(label="Run current line only...   (Ctrl+R)", command=runr)

helpmenu = Menu(menu, tearoff=0) # 자르는 선

menu.add_cascade(label="About", menu=helpmenu)
helpmenu.add_command(label="About Rpad", command=about)
helpmenu.add_command(label="Rscript", command=rse)

window.bind("<Configure>", resize)

window.protocol( "WM_DELETE_WINDOW", confirm )
window.mainloop()