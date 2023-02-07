from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.messagebox import askyesno
import subprocess
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter

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
    itext["height"]=5

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
    label = messagebox.showinfo("About", "RPad v0.5 (c) 2023 Hyeok Jeong")

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
        iline = robjects.r('ls()')
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
        iline = robjects.r('ls()')
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
window.configure(bg="#303030")

label1 = Label(window, text='Script', font=('Arial', 14))
label2 = Label(window, text='Output', font=('Arial', 14))
label3 = Label(window, text='Data', font=('Arial', 14))

label1.grid(row=0, column=0, columnspan=2)
label2.grid(row=0, column=2, columnspan=2)
label3.grid(row=2, column=2, columnspan=2)

text = Text(master=window, undo=True)
text.grid(row=1, column=0, rowspan=3, sticky=W+N+S)
text.configure(font=("Courier New", open("./data/fontsize.txt", "r", encoding='UTF-8').readlines(), "bold"))

yscrollbar = Scrollbar(window, orient=VERTICAL, command=text.yview)
yscrollbar.grid(row=1, column=1, rowspan=3, sticky=N+S+W)
text["yscrollcommand"]=yscrollbar.set

text.bind("<Control-s>", lambda event: qsave())
text.bind("<Control-Shift-KeyPress-S>", lambda event: save())
text.bind("<Control-o>", lambda event: fopen())
text.bind("<Control-r>", lambda event: runr())
text.bind("<Control-Shift-KeyPress-R>", lambda event: runa())
text.bind("<Control-e>", lambda event: o_empty())
#text.bind("<Control-Up>", lambda event: sfont(cfontsize, 5))
#text.bind("<Control-Down>", lambda event: sfont(cfontsize, -5))


otext = Text(master=window, undo=True)
otext.grid(row=1, column=2, sticky=N+E+S)
otext.configure(font=("Courier New", open("./data/fontsize.txt", "r", encoding='UTF-8').readlines(), "bold"))

oyscrollbar = Scrollbar(window, orient=VERTICAL, command=otext.yview)
oyscrollbar.grid(row=1, column=3, sticky=N+S+W)
otext["yscrollcommand"]=oyscrollbar.set

itext = Text(master=window, undo=True)
itext.grid(row=3, column=2, sticky=N+E+S)
itext.configure(font=("Courier New", open("./data/fontsize.txt", "r", encoding='UTF-8').readlines(), "bold"))

iyscrollbar = Scrollbar(window, orient=VERTICAL, command=itext.yview)
iyscrollbar.grid(row=3, column=3, sticky=N+S+W)
itext["yscrollcommand"]=iyscrollbar.set

text.configure(bg="#202020", fg="#AAAAAA", insertbackground="#AAAAAA")
itext.configure(bg="#202020", fg="#AAAAAA")
otext.configure(bg="#202020", fg="#AAAAAA")
label1.configure(bg="#303030", fg="#AAAAAA")
label2.configure(bg="#303030", fg="#AAAAAA")
label3.configure(bg="#303030", fg="#AAAAAA")


text.update()
otext.update()
itext.update()
label1.update()
label2.update()
label3.update()

h1=int(round(text.winfo_height()/text["height"])), int(round(text.winfo_width()/text["width"]))
h2=int(round(otext.winfo_height()/otext["height"])), int(round(otext.winfo_width()/otext["width"]))

window.bind("<Configure>", resize)

#메뉴를 붙인다
menubar = Menu(window, background="#303030", fg="#AAAAAA")
menubar.config(background="#303030", fg="#AAAAAA", activebackground="#202020",activeforeground='yellow',font=("Courier New", 12, "bold"))
filemenu = Menu(menubar, tearoff=0, background="#303030", fg="#FFFFFF", font=("Courier New", 12, "bold"), borderwidth=0)
runmenu = Menu(menubar, tearoff=0, background="#303030", fg="#FFFFFF", font=("Courier New", 12, "bold"), borderwidth=0)
fontmenu = Menu(menubar, tearoff=0, background="#303030", fg="#FFFFFF", font=("Courier New", 12, "bold"), borderwidth=0)
helpmenu = Menu(menubar, tearoff=0, background="#303030", fg="#FFFFFF", font=("Courier New", 12, "bold"), borderwidth=0)

menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New File", command=newfile)
filemenu.add_command(label="Open...   (Ctrl+O)", command=fopen)
filemenu.add_command(label="Save...    (Ctrl+S)", command=qsave)
filemenu.add_command(label="Save as...    (Ctrl+Shift+S)", command=save)
filemenu.add_command(label="Empty Output   (Ctrl+E)", command=o_empty)
filemenu.add_command(label="Quit", command=exit)

menubar.add_cascade(label="Run", menu=runmenu)
runmenu.add_command(label="Run current line only...   (Ctrl+R)", command=runr)
runmenu.add_command(label="Run all...   (Ctrl+Shift+R)", command=runa)

menubar.add_cascade(label="Font", menu=fontmenu)
fontmenu.add_command(label="16pt", command=font16)
fontmenu.add_command(label="20pt", command=font20)
fontmenu.add_command(label="28pt", command=font28)
fontmenu.add_command(label="36pt", command=font36)
fontmenu.add_command(label="48pt", command=font48)
fontmenu.add_command(label="72pt", command=font72)

menubar.add_cascade(label="About", menu=helpmenu)
helpmenu.add_command(label="About Rpad", command=about)

window.config(menu=menubar)
window.protocol( "WM_DELETE_WINDOW", confirm )
window.mainloop()