from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.messagebox import askyesno
import subprocess
import rpy2.robjects as robjects
import tkinter.ttk
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter
import pandas as pd

nowfile=''

def seeend() :
    text.see(END)
    otext.see(END)

def confirm():
    ans = askyesno(title='Exit', message='Exit Rpad without saving?')
    if ans:
        window.destroy()

def resize(event):
    pixelX=window.winfo_width()/2-yscrollbar.winfo_width()*2
    pixelY1=window.winfo_height()
    pixelY2=window.winfo_height()-itext.winfo_height()
    text["width"]=int(round(pixelX/h1[1]))
    text["height"]=int(round(pixelY1/h1[0]))
    otext["width"]=int(round(pixelX/h2[1]))
    otext["height"]=int(round(pixelY2/h2[0]))
    itext["width"]=int(round(pixelX/h2[1]))
    itext["height"]=7

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
    label = messagebox.showinfo("About", "RPad v0.4 (c) 2023 Hyeok Jeong")

def runcom():
    target = text.get("1.0","insert lineend")
    try : 
        exec(compile(target, '<string>', 'exec'))
    except Exception as e :
        print(e)

def runr():
    itext.delete('1.0', END)
    try :
        tline = text.get('insert linestart', 'insert lineend')
        rline = robjects.r(tline)
        otext.insert(END, rline)
        iline = robjects.r('ls.str()')
        itext.insert('1.0', iline)
        seeend()
        qsave()
    except Exception as e : otext.insert('1.0', e)

def runa():
    otext.delete('1.0', END)
    itext.delete('1.0', END)
    try :
        tline = text.get('1.0', END)
        rline = robjects.r(tline)
        otext.insert(END, rline)
        iline = robjects.r('ls.str()')
        itext.insert('1.0', iline)
        seeend()
        qsave()
    except Exception as e : otext.insert('1.0', e)

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

#Pretendard Variable Medium

def font16():
        font_size_file = open("./data/fontsize.txt", "w", encoding='UTF-8')
        font_size_file.write("16")
        font_size_file.close()
        text.configure(font=("Courier New", 16, "bold"))
        otext.configure(font=("Courier New", 16, "bold"))
        text.update()
        otext.update()
        global h1
        h1=int(round(text.winfo_height()/text["height"])), int(round(text.winfo_width()/text["width"]))
        resize()

def font20():
        font_size_file = open("./data/fontsize.txt", "w", encoding='UTF-8')
        font_size_file.write("20")
        font_size_file.close()
        text.configure(font=("Courier New", 20, "bold"))
        otext.configure(font=("Courier New", 20, "bold"))
        text.update()
        otext.update()
        global h1
        h1=int(round(text.winfo_height()/text["height"])), int(round(text.winfo_width()/text["width"]))
        resize()

def font28():
        font_size_file = open("./data/fontsize.txt", "w", encoding='UTF-8')
        font_size_file.write("28")
        font_size_file.close()
        text.configure(font=("Courier New", 28, "bold"))
        otext.configure(font=("Courier New", 28, "bold"))
        text.update()
        otext.update()
        global h1
        h1=int(round(text.winfo_height()/text["height"])), int(round(text.winfo_width()/text["width"]))
        resize()

def font36():
        font_size_file = open("./data/fontsize.txt", "w", encoding='UTF-8')
        font_size_file.write("36")
        font_size_file.close()
        text.configure(font=("Courier New", 36, "bold"))
        otext.configure(font=("Courier New", 36, "bold"))
        text.update()
        otext.update()
        global h1
        h1=int(round(text.winfo_height()/text["height"])), int(round(text.winfo_width()/text["width"]))
        resize()

def font48():
        font_size_file = open("./data/fontsize.txt", "w", encoding='UTF-8')
        font_size_file.write("48")
        font_size_file.close()
        text.configure(font=("Courier New", 48, "bold"))
        otext.configure(font=("Courier New", 48, "bold"))
        text.update()
        otext.update()
        global h1
        h1=int(round(text.winfo_height()/text["height"])), int(round(text.winfo_width()/text["width"]))
        resize()

def font72():
        font_size_file = open("./data/fontsize.txt", "w", encoding='UTF-8')
        font_size_file.write("72")
        font_size_file.close()
        text.configure(font=("Courier New", 72, "bold"))
        otext.configure(font=("Courier New", 72, "bold"))
        text.update()
        otext.update()
        global h1
        h1=int(round(text.winfo_height()/text["height"])), int(round(text.winfo_width()/text["width"]))
        resize()

#창 생성
window = Tk()
window.title('Rpad Beta')
window.geometry('1024x768')
window.iconbitmap('./data/rpadico.ico')
window.resizable(1,1)

text = Text(master=window, undo=True, fg="#CCCCCC", bg="#202020", insertbackground="#CCCCCC")
text.grid(row=0, column=0, rowspan=2, sticky=W+N+S)
text.configure(font=("Courier New", open("./data/fontsize.txt", "r", encoding='UTF-8').readlines(), "bold"))

yscrollbar = Scrollbar(window, orient=VERTICAL, command=text.yview)
yscrollbar.grid(row=0, column=1, rowspan=2, sticky=N+S+W)
text["yscrollcommand"]=yscrollbar.set

text.bind("<Control-s>", lambda event: qsave())
text.bind("<Control-Shift-KeyPress-S>", lambda event: save())
text.bind("<Control-o>", lambda event: fopen())
text.bind("<Control-r>", lambda event: runr())
text.bind("<Control-Shift-KeyPress-R>", lambda event: runa())
text.bind("<Control-e>", lambda event: o_empty())
#text.bind("<Control-Up>", lambda event: sfont(cfontsize, 5))
#text.bind("<Control-Down>", lambda event: sfont(cfontsize, -5))


otext = Text(master=window, undo=True, fg="#7FFFFF", bg="#202020", insertbackground="#7FFFFF")
otext.grid(row=0, column=2, sticky=N+E+S)
otext.configure(font=("Courier New", open("./data/fontsize.txt", "r", encoding='UTF-8').readlines(), "bold"))

oyscrollbar = Scrollbar(window, orient=VERTICAL, command=otext.yview)
oyscrollbar.grid(row=0, column=3, sticky=N+S+W)
otext["yscrollcommand"]=oyscrollbar.set

itext = Text(master=window, undo=True, fg="#FFFF00", bg="#202020", insertbackground="#FFFF00")
itext.grid(row=1, column=2, sticky=N+E+S)
itext.configure(font=("Courier New", open("./data/fontsize.txt", "r", encoding='UTF-8').readlines(), "bold"))

text.update()
otext.update()
itext.update()

h1=int(round(text.winfo_height()/text["height"])), int(round(text.winfo_width()/text["width"]))
h2=int(round(otext.winfo_height()/otext["height"])), int(round(otext.winfo_width()/otext["width"]))

window.bind("<Configure>", resize)

#메뉴를 붙인다
menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu, tearoff=0)
runmenu = Menu(menu, tearoff=0)
fontmenu = Menu(menu, tearoff=0)
helpmenu = Menu(menu, tearoff=0)

menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New File", command=newfile)
filemenu.add_command(label="Open...   (Ctrl+O)", command=fopen)
filemenu.add_command(label="Save...    (Ctrl+S)", command=qsave)
filemenu.add_command(label="Save as...    (Ctrl+Shift+S)", command=save)
filemenu.add_command(label="Empty Output   (Ctrl+E)", command=o_empty)
filemenu.add_command(label="Quit", command=exit)

menu.add_cascade(label="Run", menu=runmenu)
runmenu.add_command(label="Run current line only...   (Ctrl+R)", command=runr)
runmenu.add_command(label="Run all...   (Ctrl+Shift+R)", command=runa)

menu.add_cascade(label="Font", menu=fontmenu)
fontmenu.add_command(label="16pt", command=font16)
fontmenu.add_command(label="20pt", command=font20)
fontmenu.add_command(label="28pt", command=font28)
fontmenu.add_command(label="36pt", command=font36)
fontmenu.add_command(label="48pt", command=font48)
fontmenu.add_command(label="72pt", command=font72)

menu.add_cascade(label="About", menu=helpmenu)
helpmenu.add_command(label="About Rpad", command=about)

window.protocol( "WM_DELETE_WINDOW", confirm )
window.mainloop()