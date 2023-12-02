from tkinter import *
from tkinter import ttk
#cores
fundo = "#3297a8" #blue
cor1 = "#FFFFFF" #white
cor2 = "#e85151" #red
cor3=  "#3b3b3b"
#cria a janela principal
janela= Tk()
janela.title('')
janela.geometry('350x450')
janela.configure(bg=fundo)
#dividindo a janela
frame_cima=Frame(janela,width=325, height=100, bg= cor1, relief='raised') #cria o quadro dentro da janela
frame_cima.grid(row=0,column=0,sticky=NW, padx=10, pady=10)

frame_baixo=Frame(janela,width=350, height=300, bg= cor1, relief='flat') #cria o quadro dentro da janela
frame_baixo.grid(row=1,column=0,sticky=NW)

#linhas verticais
app_= Label (frame_baixo, text = '', height=50, relief= 'flat',pady=5, anchor="center", font = ('ivy 5 bold') ,bg=cor2)
app_.place(x=100,y=15)
app_= Label (frame_baixo, text = '', height=50, relief= 'flat',pady=5, anchor="center", font = ('ivy 5 bold') ,bg=cor2)
app_.place(x=240,y=15)
# linhas horizentais
app_= Label (frame_baixo, text = '', width=300, relief= 'flat',padx=2,pady=1, anchor="center", font = ('ivy 1 bold') ,bg=cor2)
app_.place(x=30,y=100)
app_= Label (frame_baixo, text = '', width=300, relief= 'flat',padx=2,pady=1, anchor="center", font = ('ivy 1 bold') ,bg=cor2)
app_.place(x=30,y=200)
janela.mainloop()
