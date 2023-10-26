#sets: coleção de dados não-ordenados e sem repetições

#CRIAÇÃO DE SETS
carros = {'Jetta', 'Passat', 'Crossfox','Uninho Mille'}
print(carros)

#Criando um set com elemntos diferentes
elementos_diferentes = {2017, "Onix", 37123.04, True}
print(elementos_diferentes)

#Exibindo os elementos de uma outra forma
for i in carros:
    print(i)

#OPERAÇÕES COM SETS
#Criando sets para as operações
acessorios_passat = {'Rodas de Ligas', 'Travas Eletricas', 'Piloto Automatico','Central Multmidia'}
print(acessorios_passat)

acessorios_crossfox = {'Piloto Automatico', 'Teto Panoramico', '4x4','Central Multmidia'}
print(acessorios_crossfox)

acessorios_jetta = {'Controle de Estabilidade', 'Cambio Automatico', 'Travas Eletricas', 'Rodas de Ligas'}
print(acessorios_jetta)

#Verificando se os elementos são disjuntos
set.isdisjoint(acessorios_passat, acessorios_crossfox)

#Verificando os elementos em comum dos conjuntos
acessorios_passat & acessorios_crossfox
acessorios_passat & acessorios_jetta

#2a forma:
set.intersection(acessorios_passat, acessorios_crossfox)

#Unindo os elementos dos conjuntos
acessorios_passat | acessorios_crossfox

#2a forma:
set.union(acessorios_passat,acessorios_crossfox)

#Verificando se um elemento está dentro do set
'Crossfox'in carros