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
    dados = requests.get(f'https://economia.awesomeapi.com.br/json/daily/{moeda[i]}/15')
    dados = dados.json()
    #dados = dados[moeda[i] + "BRL"]
    for j in range(0,15):
        code.append(dados[0]["code"])
        name.append(dados[0]["name"])
        name[i] = name[i].replace('/Real Brasileiro', '')
        high.append(dados[j]["high"])
        high[j] = high[j].replace('.', ',')
        low.append(dados[j]["low"])
        low[j] = low[j].replace('.', ',')
        var.append(dados[j]["varBid"])
        var[j] = var[j].replace('.', ',')
        date.append(dados[0]['create_date'])
data = {'Nome da Moeda':name, 'Sigla':code, 'Maior preço':high, 'Menor preço':low, 'variação':var, 'data da Modificação':date}
table = pd.DataFrame(data)
