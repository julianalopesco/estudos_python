#Pokedex no Excel
#Script que insere imagens de uma pasta dentro de células de uma planilha do Excel, a partir do ID. 
#Necessário pip install: pandas, pillow, xlsxwriter

import pandas as pd
from PIL import Image
import re

# Carregando os dados da planilha Excel em um DataFrame do pandas
df = pd.read_excel('E:/Documentos/Estudos/planilha pokemon/Planilha do narrador (1).xlsx',sheet_name='Pokemons')
df = df.iloc[:831,:20] #range de linhas e colunas que serão filtrados

# Criando um novo arquivo do excel usando o XlsxWriter como parâmetro.
writer = pd.ExcelWriter('E:/Documentos/Estudos/Python - Começando com a linguagem/pokedex_img.xlsx', engine='xlsxwriter')

# Convertendo o dataframe para um formato de Excel e escrevendo os dados
df.to_excel(writer, sheet_name='Pokemons', index = False) #False: retira o índice do dataframe da planilha
df.ID = df.ID.apply(lambda x: f"{x:03}") #formata o id da planilha para o mesmo formato do nome das imgs

# Recebendo o xlsxwriter workbook e worksheet object.
workbook  = writer.book
worksheet = writer.sheets['Pokemons'] #acessa a planilha 
worksheet.set_default_row(60) # define o tamanho da linha

# Inserindo a imagem.
digito = "\D"
for index,row in df.iterrows(): #insere em todas as linhas
    #carregando a imagem
    image_name = f'E:/Documentos/Estudos/planilha pokemon/Imagens Pokemon/{row.ID}.png'
    img = Image.open(image_name)
    img.thumbnail((70, 70)) #define o tamanho da imagem 
    img.save(f'E:/Documentos/Estudos/planilha pokemon/pokemons_mini/{row.ID}.png', 'PNG', quality=100) #salva uma versão menor das imgs
    worksheet.insert_image(f'T{index+2}', f'E:/Documentos/Estudos/planilha pokemon/pokemons_mini/{row.ID}.png') #insere a img a partir do id

# Fecha o Pandas Excel writer e gera o arquivo de Excel
writer.close()

# Imprimindo uma mensagem para indicar o final do processo
print('Processo concluído com sucesso.')