#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tratamento e limpeza de dados
@author: cafe
"""

import pandas as pd

# Qualidade de dados
# 
# Dados faltantes
dados_faltantes = pd.read_excel("pokemon_data_na.xlsx")
# Como encontrar dados faltantes
print(dados_faltantes.describe())
faltantes = dados_faltantes.isna()
tipo_faltantes = dados_faltantes[["Name","Type 2"]][dados_faltantes["Type 2"].isna()]
print(tipo_faltantes)
hp_faltantes = dados_faltantes[["Name","HP"]][dados_faltantes["HP"].isna()]
print(hp_faltantes)
# Estimando o motivo para o dado não estar presente
# No caso do tipo, é parte do comportamento padrão que alguns pokemons não tenham Tipo 2
# Podemos manter sem o dado, trocar por um valor arbitrário ou usar o valor de Type 1
# A escolha vai depender da análise desejada
# No caso dos pokemons Mega, o HP não foi carregado corretamente. 
# Tratando o dado faltante - estratégias
# Vamos substituir pelo valor do HP do Pokemon equivalente não Mega.
pokemon_hp = hp_faltantes.iloc[0,0]
pokemon = dados_faltantes[dados_faltantes["Name"] == pokemon_hp.split()[1]]
hp_faltantes.loc[hp_faltantes["Name"] == pokemon_hp,"HP"] = pokemon["HP"].values

# Agora vamos fazer para cada pokemon no DataFrame
for pokemon_hp in hp_faltantes["Name"]:
    pokemon = dados_faltantes[dados_faltantes["Name"] == pokemon_hp.split()[1]]
    hp_faltantes.loc[hp_faltantes["Name"] == pokemon_hp,"HP"] = pokemon["HP"].values
    # hp_faltantes["HP"][indice] = pokemon["HP"]  
# Agora vamos colocar os dados de volta no DataFrame original
for pokemon_hp in hp_faltantes["Name"]:
    dados_faltantes.loc[dados_faltantes["Name"] == pokemon_hp,"HP"] = hp_faltantes["HP"][hp_faltantes["Name"] == pokemon_hp]

#%% Outliers
dados_outliers = pd.read_excel("pokemon_data_outliers.xlsx")
# Identificando outliers
# Outliers podem ser identificados por estarem fora dos quartis
print(dados_outliers.describe())
# Vamos começar pelo HP
hp = dados_outliers[["Name","HP"]]
q1 = hp.quantile(0.25)
q3 = hp.quantile(0.75)
iqr = q3-q1
outliers_hp_abaixo = hp[hp["HP"] < (q1-1.5*iqr).values[0]]
outliers_hp_acima = hp[hp["HP"] > (q3+1.5*iqr).values[0]]
print(f"Pokemons acima HP: {outliers_hp_acima.sort_values('HP',ascending=False)}")
print(f"Pokemons abaixo HP: {outliers_hp_abaixo.sort_values('HP',ascending=False)}")
# Agora no ataque
ataque = dados_outliers[["Name","Attack"]]
q1 = ataque.quantile(0.25)
q3 = ataque.quantile(0.75)
iqr = q3-q1
outliers_abaixo = ataque[ataque["Attack"] < (q1-1.5*iqr).values[0]]
outliers_acima = ataque[ataque["Attack"] > (q3+1.5*iqr).values[0]]
print(f"Pokemons acima Attack: {outliers_acima.sort_values('Attack',ascending=False)}")
print(f"Pokemons abaixo Attack: {outliers_abaixo.sort_values('Attack',ascending=False)}")
# Tratando outliers
# Percebemos que os Pokemons MewtwoMega Mewtwo X e DiancieMega Diancie
# estão com o HP e Attack multiplicados por dez. Vamos alterar manualmente.
dados_outliers.loc[dados_outliers["HP"] == 1060,"HP"] = 106
dados_outliers.loc[dados_outliers["Attack"] == 1600,"Attack"] = 160
print(dados_outliers.describe())

