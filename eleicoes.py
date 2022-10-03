import requests
import json
import pandas as pd
import schedule
import time
from datetime import datetime

def resultado_eleicao():
    data = requests.get('https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')    
    json_data = json.loads(data.content)    
    hora_atual = datetime.now()
    candidato = []
    votos = []
    porcentagem = []

    for informacoes in json_data['cand']:
        if informacoes['seq'] in ['1','2','3','4','5','7']:
            candidato.append(informacoes['nm'])
            votos.append(informacoes['vap'])
            porcentagem.append(informacoes['pvap'])            
    df_eleicao = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns=['Candidato', 'Nº de Votos', 'Porcentagem'])        
    print('-' * 40 )
    print(f'Atualizado em {hora_atual}')    
    print('-' * 40 )
    print(df_eleicao)    

resultado_eleicao()
schedule.every(15).seconds.do(resultado_eleicao)


while True:
    schedule.run_pending()
    time.sleep(0.15)