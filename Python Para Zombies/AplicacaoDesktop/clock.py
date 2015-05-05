#Relogio desktop

import tkinter #Modulo padrão para fazer aplicação Desktop
from time import strftime
#Por Luciano Rabalho

clock = tkinter.Label()

clock.pack()
clock['font'] = 'Helvetica 120 bold'
clock['text'] = strftime(' %H: %M: %S')

def tictac():
    agora = strftime(' %H: %M: %S')
    if agora != clock ['text']:
        clock['text'] = agora
    clock.after(100,tictac)

tictac()
clock.mainloop() #Faz com que o programa fique executando até receber um evento(Fechar a janela ou pressionar alt+F4)