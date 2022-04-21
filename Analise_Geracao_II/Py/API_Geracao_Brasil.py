# Importing Libraries

# Standard libraries for DataFrame manipulations
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import missingno as msno
# from pandasgui import show
import streamlit as st

# Libraries for API Integration and Web Scrappingg
import requests

# Present the data in maps and graphs
import plotly.express as px
import plotly as plt
import plotly.figure_factory as ff

# Labels

github = "_GitHub_@viniciusgribas.html"

api_base_link = "https://dadosabertos.aneel.gov.br/dataset/6d90b77c-c5f5-4d81-bdec-7bc619494bb9/resource/11ec447d-698d-4ab8-977f-b424d5deee6a/download/siga-empreendimentos-geracao.csv"


# Functions

def line(x):
    print(x*50)

def load_data(api_base_link):
  ## Function for request a API data

    #### Loading a API data
    patch = api_base_link
    response_API = requests.get(patch)

    if (response_API.status_code == 200):
        line('-')
        print('The address was successfully accessed')
    else:
        line('-')
        print('Access failed')

    df = pd.read_csv(patch, sep= ";", header=0, decimal= ',',encoding='UTF-16' )


    numeric_df = df.select_dtypes(['float','int'])
    numeric_cols = numeric_df.columns

    string_df = df.select_dtypes(['object'])
    string_cols = string_df.columns
    
    return(df, numeric_cols, string_cols)

df , numeric_col ,  string_cols  = load_data(api_base_link)

df