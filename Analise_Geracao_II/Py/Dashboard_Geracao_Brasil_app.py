# Library imports

##  Data Manipulation libraries

import pandas as pd
import numpy as np

# Create interative charts and maps
import plotly.express as px
import plotly as plt
import plotly.figure_factory as ff

# Create a Dashboard APP
import streamlit as st


def line(x):
    print(x*50)

@st.cache
def load_data():
    """Function for loading data"""
    df = pd.read_csv(r"C:\Users\vinic\Documents\GitHub\Analise_dados_geracao_BR\Analise_Geracao_II\Notebooks\output\CSV\Generation_Data.csv",encoding='utf-8')

    numeric_df = df.select_dtypes(['float','int'])
    numeric_cols = numeric_df.columns

    text_df = df.select_dtypes(['object'])
    text_cols = text_df.columns

    tipo_ger_column = df['TipoGeracao']

    unique_tipo_ger = tipo_ger_column.unique()

    return (df, numeric_cols, text_cols, unique_tipo_ger)


df, numeric_cols, text_cols, unique_tipo_ger = load_data()


# Title of dashboard
st.title("Stock Dashboard")


# add checknob to sidebar
check_box = st.sidebar.checkbox(label="Display dataset")

if check_box:
    # lets show the dataset
    st.write(df)

# give sidebar a title
st.sidebar.title("Settings")
st.sidebar.subheader("Timeseries settings")
feature_selection = st.sidebar.multiselect(label="Features to plot",
                                           options=numeric_cols)

tipo_ger_dropdown = st.sidebar.selectbox(label="Stock Ticker",
                                      options=unique_tipo_ger)

print(feature_selection)

df = df[df['TipoGeracao']==tipo_ger_dropdown]
df_features = df[feature_selection]

plotly_figure = px.line(data_frame=df_features,
                        x=df_features.index,y=feature_selection,
                        title=(str(tipo_ger_dropdown) + ' ' +'timeline')
                        )

st.plotly_chart(plotly_figure)

plotly_figure2 = fig_SunBurstChart = px.sunburst(df, 
                    path=[px.Constant('BRASIL'),
                    "UF",
                    'TipoGeracao'],
                    values='MdaPotenciaOutorgadaKW',
                    title= "title_SunBurstChart",
                    maxdepth = -1  )
                    
st.plotly_chart(plotly_figure2)