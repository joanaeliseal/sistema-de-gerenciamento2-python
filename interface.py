from tkinter import *
from tkinter import ttk
#cores
fundo = "#3297a8" #blue
cor1 = "#FFFFFF" #white
cor2 = "#e85151" #red
#cria a janela principal
janela= Tk()
janela.title('')
janela.geometry('350x450')
janela.configure(bg=fundo)
#dividindo a janela

frame_baixo=Frame(janela,width=350, height=350, bg= cor1, relief='flat') #cria o quadro dentro da janela
frame_baixo.grid(row=0,column=0,sticky=NW)
frame_botao= Frame(janela,width=490, height=490, bg= fundo, relief='flat')
frame_botao.grid(row=1,column=0,sticky=NW)
#linhas verticais
app_= Label (frame_baixo, text = '', height=50, relief= 'flat',pady=5, anchor="center", font = ('ivy 5 bold') ,bg=cor2)
app_.place(x=100,y=15)
app_= Label (frame_baixo, text = '', height=50, relief= 'flat',pady=5, anchor="center", font = ('ivy 5 bold') ,bg=cor2)
app_.place(x=240,y=15)
# linhas horizontais
app_= Label (frame_baixo, text = '', width=300, relief= 'flat',padx=2,pady=1, anchor="center", font = ('ivy 1 bold') ,bg=cor2)
app_.place(x=30,y=120)
app_= Label (frame_baixo, text = '', width=300, relief= 'flat',padx=2,pady=1, anchor="center", font = ('ivy 1 bold') ,bg=cor2)
app_.place(x=30,y=240)
#linha 0
b_0= Button(frame_baixo, text= '', width=3, font=('ivy 31 bold'), overrelief=RIDGE,relief='flat', bg= cor1, fg=fundo)
b_0.place(x=13,y=30)
b_1= Button(frame_baixo, text= '', width=3, font=('ivy 31 bold'), overrelief=RIDGE,relief='flat', bg= cor1, fg=fundo)
b_1.place(x=130,y=30)
b_2= Button(frame_baixo, text= '', width=3, font=('ivy 31 bold'), overrelief=RIDGE,relief='flat', bg= cor1, fg=fundo)
b_2.place(x=248,y=30)
b_3= Button(frame_baixo, text= '', width=3, font=('ivy 31 bold'), overrelief=RIDGE,relief='flat', bg= cor1, fg=fundo)
b_3.place(x=13,y=140)
b_4= Button(frame_baixo, text= '', width=3, font=('ivy 31 bold'), overrelief=RIDGE,relief='flat', bg= cor1, fg=fundo)
b_4.place(x=130,y=140)
b_5= Button(frame_baixo, text= '', width=3, font=('ivy 31 bold'), overrelief=RIDGE,relief='flat', bg= cor1, fg=fundo)
b_5.place(x=248,y=140)
b_6= Button(frame_baixo, text= '', width=3, font=('ivy 31 bold'), overrelief=RIDGE,relief='flat', bg= cor1, fg=fundo)
b_6.place(x=13,y=260)
b_7= Button(frame_baixo, text= '', width=3, font=('ivy 31 bold'), overrelief=RIDGE,relief='flat', bg= cor1, fg=fundo)
b_7.place(x=130,y=260)
b_8= Button(frame_baixo, text= '', width=3, font=('ivy 31 bold'), overrelief=RIDGE,relief='flat', bg= cor1, fg=fundo)
b_8.place(x=248,y=260)
b_jogar = Button(frame_botao, text= 'jogar', width=10, height=1, font=('Ivy 10 bold'), overrelief=RIDGE, relief='flat',bg=cor1,fg=cor2)
b_jogar.place(x=130,y=15)
janela.mainloop()
