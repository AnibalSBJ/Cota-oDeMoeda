import requests
import pandas as pd
from datetime import datetime
import time

while True:
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()
    cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
    cotacao_euro = requisicao_dic["EURBRL"]["bid"]
    cotacao_btc = requisicao_dic["BTCBRL"]["bid"]

    print(f"{cotacao_dolar} BRL ") 
    print(f"{cotacao_euro} BRL ")
    print(f"{cotacao_btc} BRL")
    print(datetime.now())

    time.sleep(5)