import re
from tkinter import *

def validar_cpf():
    cpf = caixa_de_texto.get()
    cpf = re.sub('[^0-9]', '', cpf)

    validacao1 = 10
    soma1 = 0
    validacao2 = 11
    soma2 = 0

    indice = 0
    memoria = []
    invalidar = 0

    for i in cpf:
        memoria.append(i)
        if indice >= 1 and i == memoria[indice-1]:
            invalidar+=1

        if len(cpf) == 11 and validacao1 != 0 and indice < 9:
            soma1 += int(i) * validacao1
        if len(cpf) == 11 and validacao2 != 0 and indice < 10:
            soma2 += int(i) * validacao2
        
        validacao1-=1
        validacao2-=1
        indice+=1
    
    if len(cpf) == 11 and invalidar != 10 and soma1*10 % 11 == int(memoria[9]) and soma2*10 % 11 == int(memoria[10]):
        exibir['text'] = 'Válido'
        exibir['bg'] = '#1aff1a'
    else:
        exibir['text'] = 'Inválido'
        exibir['bg'] = '#ff3333'

janela = Tk()
janela.title('Validador de CPF')

texto_principal = Label(janela, text='Digite um CPF')
texto_principal.grid(column=0, row=0, padx=20, pady=10)

caixa_de_texto = Entry(janela, bd=2, width=20, justify='left')
caixa_de_texto.grid(column=0, row=1, padx=10, pady=10)

botao = Button(janela, text='Validar', command=validar_cpf)
botao.grid(column=1, row=1, padx=10, pady=10)

exibir = Label(janela, text='', bg='#f2f2f2')
exibir.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()