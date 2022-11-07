from tkinter import *
from cpf import *

def validar_cpf():
    entrada = caixa_de_texto.get()
    cpf_digitado = Cpf(entrada)
    cpf_digitado.clean_cpf()

    if not cpf_digitado.is_sequence() and cpf_digitado.cpf_valido():
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
