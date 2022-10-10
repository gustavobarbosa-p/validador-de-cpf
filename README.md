# validador-de-cpf
Algoritmo que verifica se um CPF é válido ou inválido (com layout)

As regras para validar um cpf estão descritas em https://dicasdeprogramacao.com.br/algoritmo-para-validar-cpf/

# Correção de bug

Corrigi o problema de não validação de um <strong>cpf válido</strong> (porque troquei um sinal de "menor que (<)" por um de "maior que (>)". Ainda tá acontecendo um bug ao digitar um cpf formatado que quando você apaga o último carácter ele dá um IndexError mas vou corrigir.7
