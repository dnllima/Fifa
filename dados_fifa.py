#importando as bibliotecas
import pandas as pd

#caminho do arquivo do csv
df_fifa = pd.read_csv(r'C:\\data-integration\\fifa\\Dataset\\ds_fifa.csv')

#analisar se tem dados no csv
if df_fifa.empty:
    raise ValueError(f"o dataframa {df_fifa} esta vazio,analisar")


#mostrando o arquivo em tela 
print(df_fifa)


