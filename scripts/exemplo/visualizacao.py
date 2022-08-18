# -*- coding: utf-8 -*-
"""
Visualização de dados
"""

import pandas as pd

dados = pd.read_csv("pokemon_data.csv")
# Análise exploratória dos dados
colunas = dados.columns
selecionados = dados['Name'][71:75]

# Análise de estatística descritiva
sumario = dados.describe()
print(sumario)
print(sumario['HP'])

print(f"A média do HP é {dados['HP'].mean()}")

water = dados[dados["Type 1"] == "Water"]
print(f"A média do HP Water é {water['HP'].mean()}")

agrupados = dados[['HP',
                   'Type 1']].groupby('Type 1').mean().sort_values('HP',ascending=False)

# Visualização de dados
## Relacionamentos
# Scatter
colors=['#145da0','#0c2d48','#2e8bc0','#b1d4e0']
ax = dados.plot.scatter(x="Attack",y="Defense",c=colors[2])

# Bolhas
# dados['HP'] = dados['HP']*0.5
# dados['Sp. Atk'] = dados['Sp. Atk']*5
dados.plot.scatter(x="Attack",y="Defense",s="HP",alpha=0.5)

# Comparação
# Linha
dados[['#',"HP"]].plot(x='#',y='HP')
# Barras
dados[100:101].plot.bar(ylim=[0,160],xlabel=dados["Name"][100])

# Distribuição
# Histograma
dados['HP'].plot.hist()
# dados['HP'].plot.box()

agrupados.plot.box()









