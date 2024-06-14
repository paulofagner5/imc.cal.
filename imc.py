from tkinter import*
from tkinter import ttk

co0= '#ffffff'
co1= '#444466'
co2= '#4065a1'

janela = TK() 
janela.title('')
janela.geometry('295x230')
janela.configure(bg=co0)

frame_cima= Frame(janela, width=295, height=50, bg=co0, pady =0, padx =0, relief ='flat')
frame_cima.grid(row=0, colown=0, sticky=NSEW)

frame_baixo= Frame(janela, width=295, height=180, bg=co0, pady =0, padx =0, relief ='flat')
frame_baixo.grid(row=1, colown=0, sticky=NSEW)

app.nome = Label(frame, cima, text='Calculadora de IMC', width=23, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 16 bold'), bg=co0, fg=co1)
app.nome.place(x=0, y=0)

app.linha= Label(frame, cima, text='', width=400, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 1'), bg=co2, fg=co1)
app.linha.place(x=0, y=35)


l.peso = Label(frame, baixo, text='Digite seu peso:', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
l.peso.gride(row=0, colown=0, sticky=NSEW, pady=10, padx=3)
e.peso = Entry(frame, baixo, width=5, relief='solid', font=('Ivy 10 bold') justify= 'center')
e.peso.gride(row=0, colown=1, sticky=NSEW, pady=10, padx=3)


l.altura = Label(frame, baixo, text='Digite sua altura:', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
l.altura.gride(row=0, colown=0, sticky=NSEW, pady=10, padx=3)
e.altura = Entry(frame, baixo, width=5, relief='solid', font=('Ivy 10 bold') justify= 'center')
e.altura.grid(row=0, colown=1, sticky=NSEW, pady=10, padx=3)

l.resultado = Label(frame, baixo, text='---', width=37, height=5, padx=6, pady=12, relief='flat', anchor='center', font=('Ivy 24 bold'), bg=co2, fg=co0)
l.resultado.place(x=175, y=10)

l.resultado_texto = Label(frame, baixo, text='O seu IMC e: abaixo do peso!', width=37, height=5, padx=6, pady=12, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1 )
l.resultado_texto.place(x=0, y=90)

b.calcular_texto = Button(frame, baixo, text='Calcular', width=34, height=1, overrelief=SOLID, padx=6, pady=12, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co2, fg=co0 )
b.calcular_texto.grid(row=4, colown=0 , sticky=NSEW, pady=60, padx=5, colownspan=30)





janela.mainloop()