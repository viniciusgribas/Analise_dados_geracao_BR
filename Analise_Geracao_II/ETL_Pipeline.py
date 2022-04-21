# Library imports

##  Data Manipulation libraries

import pandas as pd
import numpy as np
import missingno as msno

##  Web Scrapping library

import requests

## Others
from pathlib import Path  # Create a new output file
from datetime import datetime # Show the real time data
import os


def line(x):
    print(x*50)

# ======== ETL-PROCESS ========

# DATA EXTRACTION

## Assign path 

patch = r"https://dadosabertos.aneel.gov.br/dataset/6d90b77c-c5f5-4d81-bdec-7bc619494bb9/resource/11ec447d-698d-4ab8-977f-b424d5deee6a/download/siga-empreendimentos-geracao.csv"

## Applying a server request

response_API = requests.get(patch)

# Check the file availability, if the value is 200 it was succeeded.

line('*')
print("Status Code")
line('.')
print(response_API.status_code)
if response_API.status_code == 200:
    print("SUCCESS")
else: 
    print("FAILED")

# Look up the requested address information

line('*')
print('HEADERS')
line('.')
print(response_API.headers)

## Note the following information:
# 'Content-Type': 'text/csv'

# The encoding information can be obtained via the .encoding command
line('*')
print('ENCODING')
line('.')
print(response_API.encoding)
line('*')

# Creating a dataframe
df = pd.read_csv(patch, sep= ";", header=0, decimal= ',',encoding="UTF-16")


## DATA TRANSFORMATION

# Using the .drop() function to delete unwanted columns

df = df.drop(columns=['DatGeracaoConjuntoDados','IdeNucleoCEG','CodCEG','DscPropriRegimePariticipacao','DscSubBacia','DscMuninicpios'] )

# Changing the null values in those columns:

## For the 'IdGeracaoQualificada' column the 'nan' values was replaced by "Não"
## Given that is a Binary Type Variable

df.IdcGeracaoQualificada.fillna('Não',inplace=True)

## For the 'DatInicioVigencia' column the 'nan' values was replaced by 0
## Given that is a Date-Time Type Variable

df.DatInicioVigencia.fillna(0,inplace=True)
pd.to_datetime(df.DatInicioVigencia)

## For the 'DatFimVigencia' column the 'nan' values was replaced by 0
## Given that is a Date-Time Type Variable

df.DatFimVigencia.fillna(0,inplace=True)
pd.to_datetime(df.DatFimVigencia)

## For the 'DatEntradaOperacao' column the 'nan' values was replaced by 0
## Given that is a Date-Time Type Variable

df.DatEntradaOperacao.fillna(0,inplace=True)
pd.to_datetime(df.DatEntradaOperacao)

# The sum of null values

print(df.isnull().sum())

## DATA LOAD

# Setting the final patch and the filename

filepath = Path('output/CSV/Generation_Data.csv')  

# Creating a new file

filepath.parent.mkdir(parents=True, exist_ok=True)  

# Export the DF to a CSV with the UTF-8 encoding

df.to_csv(filepath, encoding='utf-8', index=False)  

# Final Message

print('CREATION DATE [',datetime.now().strftime("%Y.%m.%d - %H:%M:%S"), ']\nOUTPUT PATCH [',os.getcwd(), filepath,'] directory')

