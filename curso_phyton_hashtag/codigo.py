print("O print é uma função que exibe mensagens na tela.")

'''Exemplo de uma exibição de mensagem usando o print'''
'''Você criou um valor e armazenou ele em uma variável, e depois exibiu o valor usando o print'''
faturamento = 10000 # tipo: int -> número inteiro
custo = 6500.00 # tipo: float -> número decimal

novas_vendas = 1000 
faturamento = faturamento + novas_vendas 

imposto = faturamento * 0.1 # sempre que for colocar uma porcentagem, é necessário dividir por 100, ou seja, multiplicar por 0.1 para 10%
Lucro = faturamento - custo - imposto 
margem_lucro = Lucro / faturamento 

print("Faturamento foi de ", faturamento)
print("O custo foi de ", custo)
print("O lucro foi de ", Lucro)
print("A margem de lucro foi de ", round(margem_lucro, 2))
# O round é uma função que arredonda o número para o número de casas decimais especificado, ou seja, arredonda para o número inteiro mais próximo. No caso, arredonda para 0 casas decimais, ou seja, arredonda para o número inteiro mais próximo.

mensagem = "O faturamento da loja foi de  " # tipo: str string -> texto
email = "emailqualquer@dominio.com" # tipo: str string -> texto

teve_lucro = True # tipo: booleano -> verdadeiro ou falso

#Mod -> operador de módulo, que retorna o resto da divisão entre dois números %
resto = 100 % 30 # retorna 1
print("O resto da divisão de 100 por 30 é ", resto)

'''Exemplo de Mod'''
tempo_contrato = 78 # meses
tempo_anos = 78 / 12 # meses dividido por 12 meses por ano
print("O tempo do contrato em anos é ", int(tempo_anos)) # int converte um número decimal em um número inteiro, ou seja, arredonda para baixo.
tempo_meses = 78 % 12 # meses dividido por 12 meses por ano, retorna o resto da divisão, ou seja, o número de meses restantes
print("O tempo do contrato em meses é ", tempo_meses)