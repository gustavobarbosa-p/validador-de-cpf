from tkinter import *

def validar_cpf():

    try:
        cpf_extraido = caixa_de_texto.get()
        cpf = str(cpf_extraido)

        validador = []
        validacao = 10
        soma = 0
        validacao1 = 11
        soma1 = 0
        
        invalidar = 0
        indice = 0
        memoria = []
        
        for i in cpf:
            
            # Vai verificar se os digitos do CPF são todos iguais
            memoria.append(i)
            if len(memoria) > 1 and i == memoria[indice-1]:
                invalidar+=1
            
            # Faz a primeira etapa da validação
            if i != '.' and i != '-':
                caracter_convertido = int(i)
                if validacao > 1:
                    soma += caracter_convertido * validacao
                    validacao-=1
        
                if validacao == 0:
                    validador.append(i)
            # Faz a segunda etapa da validação
            if i != '.' and i != '-':
                caracter_convertido = int(i)
                if validacao1 > 1:
                    soma1 += caracter_convertido * validacao1
                    validacao1-=1
        
                if validacao1 == 1:
                    validador.append(i)
                
                indice+=1
        # Verifica se o CPF é pequeno demais
        if len(cpf) < 11 and len(cpf) > 0:
            exibir['text'] = 'CPF pequeno demais'
            return
        # Verifica se o CPF é grande demais
        if len(cpf) > 14:
            exibir['text'] = "CPF grande demais"
            return
        
        # Cria as variáveis que vão validar o CPF e faz as últimas modificações no CPF
        valida = soma * 10 % 11
        valida1 = soma1 * 10 % 11
        if str(valida) == 10:
            valida = 0
        if str(valida1) == 10:
            valida1 = 0
        
        # Verifica se o CPF é válido
        if str(valida) == validador[0] and str(valida1) == validador[1] and invalidar >= 11:
            exibir['text'] = 'VÁLIDO'
        else:
            exibir['text'] = 'INVÁLIDO'
    # Se o usuário não digitar nada e clicar em "validar"
    except IndexError:
        exibir['text'] = 'ERRO! Digite alguma coisa'
    # Se o usuário não digitar um cpf no formato suportado
    except ValueError:
        exibir['text'] = 'Digite apenas números e caracteres como "." e "-"'

#-------------------------layout-------------------------#
janela = Tk()
janela.title("Validador de CPF")

titulo_principal = Label(janela, text='Digite um CPF:')
titulo_principal.grid(column=0, row=0, padx=15, pady=20)

caixa_de_texto = Entry(janela, font=('arial', 12), bd=2, width=20, justify='left')
caixa_de_texto.grid(column=0, row=1, padx=10, pady=10)

botao = Button(janela, text='Validar', command=validar_cpf)
botao.grid(column=1, row=1, padx=10, pady=10)

exibir = Label(janela, text='')
exibir.grid(column=0, row=2, padx=15, pady=20)
janela.mainloop()