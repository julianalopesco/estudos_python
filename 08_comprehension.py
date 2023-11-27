# -*- coding: utf-8 -*-
"""Python_08_Comprehension.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kLbBwEswPlOR_nku0ITsV3aapx10j5Mn
"""

#LIST COMPREHENSION

#formato: [resultado_if if cond else resultado_else for item in lista]

#criando a primeira lista
nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

situacao = ["Aprovado(a)" if media >=6 else "Reprovado(a)" for media in medias] #gerando a lista conforme condições
situacao

cadastro = [x for x in [nomes, notas, medias, situacao]] #gerando a lista de listas, forma 1
cadastro

lista_completa = [nomes, notas, medias, situacao] #criando a lista de listas, forma 2
lista_completa

#outro exemplo de list comprehension

alturas = [1.70, 1.80, 1.65, 1.75, 1.90]
pesos = [65, 80, 58, 70, 95]

imc = [round((peso / altura**2), 1) for altura, peso in zip(alturas, pesos)] #gerando a lista com cada IMC do dataset
print(imc)

#DICT COMPREHENTION - ABRANGÊNCIA DE DICIONÁRIOS

lista_completa = [[('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')], #lista de listas com tuplas
                  [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]],
                  [9.0, 7.3, 5.8, 6.7, 8.5], #lista de listas
                  ['Aprovado', 'Aprovado', 'Reprovado', 'Aprovado', 'Aprovado']] #lista de situações

#colunas com os tipos dos dados (exceto nome)

coluna = ["Notas", "Média Final", "Situação"]
cadastro = {coluna[i]: lista_completa[i+1] for i in range(len(coluna))} #criação do dicionário com tipos de dados em chave .formato: {chave: valor for item in lista}
cadastro

#adicionando o nome dos estudantes
cadastro["Estudante"] = [ lista_completa[0][i][0] for i in range(len(lista_completa[0]))] #[expressão for item in lista] 0 = a posição do nome
cadastro