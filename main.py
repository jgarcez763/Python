import pandas as pd
import re
from os import system
from pathlib import Path



# Deixa o xlsx global para todas as funções
global df
df = pd.read_excel(Path('pokemon_data.xlsx'))

# Busca o texto escrito na coluna selecionada e exporta
def buscaExcel(column, busca):

	
	search = df.loc[df[column].astype(str).str.contains(busca,flags=re.I, regex=True)]
	print(search)
	search.to_html(Path('lista.html'))

	system("call lista.html")
	print()

# Lista as colunas do arquivo
def listColumns():
	columnsList = []
	for col in df.columns:
		columnsList.append(col)
	return columnsList

# Exibe as colunas para seleção
def selectColumn(list):
	print("selecione a coluna que deseja buscar")
	index = 1
	for col in list:
		print(f'{index} - {col}')
		index +=1
	select = int(input("Digite a coluna: "))
	return(list[select - 1])

# Laço de repetição para o script não fechar
while True:
	print("Selecione uma opção:")
	print("1 - Busca")
	print("2 - Para fechar")
	option = input("")
	
	
	if option == "1":
		listcol = listColumns()
		colunaSelecionada = selectColumn(listcol)
		
		busca = str(input("texto para busca: "))

		buscaExcel(colunaSelecionada,busca)
	else:
		break