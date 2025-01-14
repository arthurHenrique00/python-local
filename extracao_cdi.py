import csv
import json
import os
import time
from datetime import datetime
from random import random
from sys import argv

import pandas as pd
import requests
import seaborn as sns

URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados'

def extracao_cdi():
    try:
        response = requests.get(url=URL)
        response.raise_for_status()
    except requests.HTTPError as exc:
        print("Os dados não foram encontrados, mas a execução continuará.")
        return None
    except Exception as exc:
        print("Ocorreu um erro, a execução será parada.")
        raise exc
    else:
        return json.loads(response.text)[-1]['valor']

def gerar_csv():
    dado = extracao_cdi()

    for _ in range(0, 10):
        date_time = datetime.now()
        data = datetime.strftime(date_time, '%Y/%m/%d')
        hora = datetime.strftime(date_time, '%H:%M:%S')

        cdi = float(dado) + (random() - 0.5)

        if not os.path.exists('./taxa-cdi.csv'):
            with open(file='./taxa-cdi.csv', mode='w', encoding='utf8') as fp:
                fp.write('data,hora,taxa\n')

        with open(file='./taxa-cdi.csv', mode='a', encoding='utf8') as fp:
            fp.write(f'{data},{hora},{cdi}\n')

        time.sleep(1)

    print("CSV gerado com sucesso.")

def grafico(nome_grafico):
    df = pd.read_csv('./taxa-cdi.csv')

    grafico = sns.lineplot(x=df['hora'], y=df['taxa'])
    _ = grafico.set_xticklabels(labels=df['hora'], rotation=90)
    grafico.get_figure().savefig(f"{nome_grafico}.png")
    print(f"Gráfico salvo como {nome_grafico}.png")

def main():
    if len(argv) < 2:
        print("Forneça o nome do gráfico como parâmetro.")
        return

    nome_grafico = argv[1]

    gerar_csv()

    grafico(nome_grafico)

if __name__ == "__main__":
    main()
