import pandas as pd
import numpy as np
import string as st
from scipy.stats import mode

# Script created to clean the Bovinos database and do Feature Engineering.

#################################################################################

def clearingQuotes(df):
    df.ANO = df.ANO.map(lambda x: str(x).replace(',', ''))
    df.ANO = df.ANO.map(lambda x: str(x).replace('"', ''))

    df.N_ANALISE = df.N_ANALISE.map(lambda x: str(x).replace(',', ''))
    df.N_ANALISE = df.N_ANALISE.map(lambda x: str(x).replace('"', ''))

    df.SIF = df.SIF.map(lambda x: str(x).replace(',', ''))
    df.SIF = df.SIF.map(lambda x: str(x).replace('"', ''))
    
    df.COD_TIPAN = df.COD_TIPAN.map(lambda x: str(x).replace(',', ''))
    df.COD_TIPAN = df.COD_TIPAN.map(lambda x: str(x).replace('"', ''))

    df.CEP = df.CEP.map(lambda x: str(x).replace('"', ''))
    df.CEP = df.CEP.map(lambda x: str(x).replace(',', '.'))

    df.QTD_ANIMAIS = df.QTD_ANIMAIS.map(lambda x: str(x).replace(',', ''))
    df.QTD_ANIMAIS = df.QTD_ANIMAIS.map(lambda x: str(x).replace('.', ''))

    return df

#################################################################################

def clearing_database(df):
    df = clearingQuotes(df)


    df.CEP2 = df.CEP2.fillna(0)

    df.CEP = df.CEP + df.CEP2.apply(lambda x: "-000" if x == 0 else "-" + str(x).split(".")[0])


    df.RESULTADO = df.RESULTADO.fillna(0.0)
    df.UF = df.UF.fillna("UNKNOWN")

    df.CEP = df.CEP.map(lambda x: str(x).replace('-', ''))
    df.CEP = df.CEP.map(lambda x: str(x).replace('.', ''))
    df.CEP = df.CEP.fillna("UNKNOWN")

    df.NOME_MUN = df.NOME_MUN.fillna("UNKNOWN")
    df.NOME_MUN = df.NOME_MUN.map(lambda x: str(x).replace(' ', '_'))
    
    mean_animals = np.mean(df.QTD_ANIMAIS)
    df.QTD_ANIMAIS = df.QTD_ANIMAIS.fillna(mean_animais) #169


    df['TEMP'] = df.apply(lambda x: 5 if x['STATUS'] == 6 and x['RESULTADO'] > 0 else x['STATUS'], axis = 1)
    df['NSTATUS'] = df.apply(lambda x: 6 if x['TEMP'] == 7 and x['RESULTADO'] == 0.0 else x['TEMP'], axis = 1)

    #ANO,SEMANA,N_ANALISE,SIF,UF,NOME_MUN,CEP,QTD_ANIMAIS,COD_TIPAN,COD_RESIDUO,RESULTADO,STATUS

    df = df[['ANO', 'SEMANA', 'N_ANALISE', 'SIF', 'UF', 'CEP','QTD_ANIMAIS', 'COD_TIPAN', 'COD_RESIDUO', 'RESULTADO' ,'NSTATUS']]

    return df

#################################################################################

def main():
    path = '/home/hialo/UnB/TCC2/data/bovinos/bovinos_firstround.csv'
    target = '/home/hialo/UnB/TCC2/data/bovinos/bovinos_fourthround.csv'

    df = pd.read_csv(path)

    df = clearing_database(df)
    
    pdf = pd.DataFrame(df)

    pdf.to_csv(target, index = False)
    
main()