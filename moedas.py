import pandas as pd
import os
import matplotlib.pyplot as plt
import requests

code = []
name = []
high = []
low = []
var = []
date = []

i = 0
moeda = ["USD", "EUR", "CAD", "AUD", "ARS", "CNY", "JPY", "BTC","ETH", "MXN", "PEN", "UYU", "COP", "BOB"]
for i in range(0, len(moeda)):
    dados = requests.get(f'https://economia.awesomeapi.com.br/json/last/{moeda[i]}')
    dados = dados.json()
    dados = dados[moeda[i] + "BRL"]
    code.append(dados["code"])
    name.append(dados["name"])
    name[i] = name[i].replace('/Real Brasileiro', '')
    high.append(dados["high"])
    high[i] = high[i].replace('.', ',')
    low.append(dados["low"])
    low[i] = low[i].replace('.', ',')
    var.append(dados["varBid"])
    var[i] = var[i].replace('.', ',')
    date.append(dados['create_date'])
data = {'Nome da Moeda':name, 'Sigla':code, 'Maior preço':high, 'Menor preço':low, 'variação':var, 'data da Modificação':date}
table = pd.DataFrame(data)
print(table)