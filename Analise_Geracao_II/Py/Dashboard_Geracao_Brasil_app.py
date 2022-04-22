
#---

# Vinicius Guerra e Ribas
## [Energy Engineer (UnB)] │ [Data Scientist & Analytics (USP)]

#---


# Library imports


##  Data Manipulation libraries

from distutils import text_file
import pandas as pd
import numpy as np

# Create interative charts and maps
import plotly.express as px
import plotly as plt
import plotly.figure_factory as ff
import plotly.graph_objects as go

# Create a Dashboard APP
import streamlit as st



# Making a load_data() func to improve performance

@st.cache
def load_data():
    """Function for loading data"""
    df = pd.read_csv(r"https://github.com/viniciusgribas/Analise_dados_geracao_BR/blob/main/Analise_Geracao_II/Notebooks/output/CSV/Generation_Data.csv",encoding='utf-8',index=False)

    numeric_df = df[['MdaPotenciaFiscalizadaKW','MdaGarantiaFisicaKW','MdaPotenciaOutorgadaKW']]
    numeric_cols = numeric_df.columns

    text_df = df[[   'UF',
                     'TipoGeracao',
                     'Fase',
                     'OrigemCombustivel',
                     'FonteCombustivel',
                     'Outorga',
                     'NomeCombustivel',
                     'GeracaoQualificada'] ]
    text_cols = text_df.columns

    uf_column = df['UF']

    unique_uf = uf_column.unique()

    tipo_ger_column = df['TipoGeracao']

    unique_tipo_ger = tipo_ger_column.unique()

    return (df, numeric_cols, text_cols, unique_tipo_ger,unique_uf)


df, numeric_cols, text_cols, unique_tipo_ger, unique_uf = load_data()


# Textual Part
st.write("""
#  Brazil Generation Sector Dashboard 
### A Interative Dashboard App.
# 🇧🇷⚡
---
 """)

with st.expander("Guide📣"):
     st.write("""
     > ⬅️ Explore the "Tools" in the left corner.
    - In the "General Tools" you can view the data and the metadata.
    - The "Insight's & Analysis Tools" tab contains interactive charts.
        - The General Analysis contains fixed variables that make sense with this business type.
        - The Exploratory Analysis contains three types of charts:
            - The "DensityHeatmap" 
    - The "Analyses" tab you can try your own insights.

    """)

#=============================
# GENERAL SETINGS-------
####################
# Add a Sidebar Title 
st.sidebar.write("""
# Vinicius Guerra e Ribas 
#### [📧 E-mail](mailto:viniciusgribas@gmail.com?Subject=%5BGENERATION-SECTOR-DASHBOARD%5D%20-%20Contact) │ [🎯 Linkedin](https://www.linkedin.com/in/vinicius-guerra-e-ribas/) │ [😸 GitHub](https://github.com/viniciusgribas) 
---
""")
####################







st.sidebar.title("⚙️ TOOLS ⬇️ ")
st.sidebar.write("""
---
""")

st.sidebar.subheader("🧰 General Tools")
# add Display Dataset to sidebar
check_box = st.sidebar.checkbox(label="Display Dataset 🗃️")
if check_box:
    # lets show the dataset
    st.write("""# 🗃️ DATASET """)
    st.write(df)

# add Display Metadata to sidebar
check_box = st.sidebar.checkbox(label="Display Metadata 🔎")
if check_box:
    # lets show the dataset
    st.write("""# 🔎 METADATA """)
    st.write( """
| Variable                 | Type        | Meaning                      |
|--------------------------|-------------|------------------------------|
| `MdaGarantiaFisicaKW`      | Numerical   | Physical Guarantee of Energy |
| `MdaPotenciaFiscalizadaKW` | Numerical   | Supervised Electric Power    |
| `MdaPotenciaOutorgadaKW`   | Numerical   | Granted Electric Power       |
| `Empreendimento`           | Categorical | Business Name                |
| `UF`                       | Categorical | Brasil States                |
| `TipoGeracao`              | Categorical | Generation Type              |
| `Fase`                     | Categorical | Operational Phase            |
| `OrigemCombustivel`        | Categorical | Fuel Origin                  |
| `FonteCombustivel`         | Categorical | Fuel Source                  |
| `NomeCombustivel`          | Categorical | Fuel Name                    |
| `Outorga`                  | Categorical | Grant                        |
| `GeracaoQualificada`       | Categorical | Qualified Generation Mode    |
| `DatEntradaOperacao`       | Date-Time   | Operation Start Date         |
| `DatInicioVigencia`        | Date-Time   | Start Date of Contract       |
| `DatFimVigencia`           |   Date-Time | End Date of Contract         |
| `X`                        |  Geographic | Longitude Values             |
| `Y`                        |  Geographic | Latitude Values              |

""")


#=============================
st.sidebar.write("""
---
""")
# AUTHOR INSIGHTS-------

st.sidebar.subheader("💡 Insight's & Analysis Tools")

# General Analyses
check_box = st.sidebar.checkbox(label="General Analyses 📊")
# General Analyses Checkbox
if check_box:
    # lets show the dataset
    st.write("""# 📊 General Analyses""")
    chart_select = st.sidebar.radio(
    label="Select the chart type",
    options=['Map', 'Pie', 'Tree', 'Strip' , 'Polar'])

     #### Cicle Charts to Hierarchical Variables ####
    if chart_select == 'Pie':
        #### Cicle Charts to Hierarchical Variables ####
        st.write("""
        Interactive pie chart with hierarchical variables

        > 💡 Interact with the Chart by clicking on the sectors in the circle
        
        """)
        # Titles
        title_SunBurstChart = "Granted Potency by State and Type of Generation in Brazil"
        # Size
        size = 750

        fig_SunBurstChart = px.sunburst(df, 
            path=[px.Constant('BRASIL'),
                "UF",
                'TipoGeracao'],
            values='MdaPotenciaOutorgadaKW',
            title= title_SunBurstChart,
            width=size,
            height=size,
            maxdepth = -1  
        )

        st.plotly_chart(fig_SunBurstChart)
     #### Cicle Charts to Hierarchical Variables ####
    if chart_select == 'Tree':
        #### Cicle Charts to Hierarchical Variables ####
        st.write("""
        Interactive TreeMap chart with hierarchical variables

        > 💡 Interact with the Chart by clicking on the sectors in the rectangle
        
        """)
        # Titles
        title_treemapChart = "Granted Power [KW] by Phase and Type of Generation in Brazil"
        # Size
        size = 750
        fig_treemapChart = px.treemap(df, 
            path=[px.Constant('BRASIL'),
                "Fase",
                'OrigemCombustivel',
                'FonteCombustivel',
                'UF'
                ],
            values='MdaPotenciaOutorgadaKW',
            title= title_treemapChart,
            width=size,
            height=size,
            maxdepth = -1  )

        st.plotly_chart(fig_treemapChart)

    if chart_select == 'Strip':
            #### Cicle Charts to Hierarchical Variables ####
            st.write("""
                Interactive Strip Chart with categorical and numerical variables.
                > 💡 Interact with the Chart by clicking on the legend color icons or try selecting an area.
            
            """)
            # Title

            title_strip = "Granted Power [KW] and Type of Generation by State"

            # Função para criar a variável do gráfico de pontos iterativo do plotfy

            fig_Strip = px.strip(df,  # Dataframe
            title=title_strip,           # Title
            x="MdaPotenciaOutorgadaKW",  # Numerical Variable
            y="UF",                      # Categorical Variable
            orientation="h",             # Horizontal orientation
            hover_name="Empreendimento", # Business name
            color="TipoGeracao",      # Categorical Variable
            )

            st.plotly_chart(fig_Strip)

    if chart_select == 'Polar':
        #### Cicle Charts to Hierarchical Variables ####
        st.write("""
            Interactive Polar Chart with categorical and numerical variables.
            > 💡 Interact with the Chart by sliding below the picture or try selecting an area.
        
        """)
        # Title

        title_Polar = "Granted Power [KW] and Type of Generation by State"

        # Função para criar a variável do gráfico de pontos iterativo do plotfy

        fig_Polar = px.bar_polar(df, # Dataframe
        title=title_Polar,              # Title
        r="MdaPotenciaOutorgadaKW",     # Numerical Variable
        theta="UF",                     # Categorical Variable
        color="MdaPotenciaOutorgadaKW", # Numerical Variable
        template="seaborn",              # Color Theme 
        animation_frame="TipoGeracao",  # Categorical Variable
        hover_name= 'Empreendimento',
        color_discrete_sequence= px.colors.sequential.Plasma_r # Color Theme 
        ) 

        st.plotly_chart(fig_Polar)

    if chart_select == 'Map':
        #### Cicle Charts to Hierarchical Variables ####
        st.write("""
            Interactive Map of Coordinates.
            > 💡 Interact with the map by sliding below the picture or try selecting an area.
        
        """)
        # Titulo

        title_pointsMap = "Power Granted by Business Location"

        # Função para criar a variável do gráfico de pontos iterativo do plotfy

        fig_pointsMap = px.scatter_mapbox(df,              # DataFrame
        title=title_pointsMap,                                # Titulo
        lat="Y",                                              # Variável do tipo Float Referente à Latitude
        lon="X",                                              # Variável do tipo Float Referente à Longitude
        color="MdaPotenciaOutorgadaKW",                       # Variável Quantitativa Contínua atribuída à cor
        size="MdaPotenciaOutorgadaKW",                        # Variável Quantitativa Contínua atribuída ao tamanho dos círculos
        color_continuous_scale=px.colors.sequential.matter,   # Opção de Cores pré-definidas pelo plotfy
        hover_name = "Empreendimento" ,                       # Apresentar o nome do empreendimento na caixa iterativa
        hover_data = ["MdaPotenciaOutorgadaKW"],              # Variável Quantitativa Contínua atribuída à função
        size_max=80,                                          # Tamanho máximo para os círculos
        zoom=3,                                               # Zoom inicial no mapa
        mapbox_style='open-street-map',                       # Opção de Mapa pré definida pelo plotfy
        animation_frame='TipoGeracao'                         # Variável Qualitativa Atribuída à animação do mapa (Vai dividi-lo)
        )
        st.plotly_chart(fig_pointsMap)

check_box = st.sidebar.checkbox(label="Exploratory Analyses 🔭")
if check_box:
    # lets show the dataset
    st.write("""# 🔭 Exploratory Analyses""")
    chart_options = st.sidebar.radio(
    label="Select the type of chart for your analysis",
    options=['DensityHeatmap','Bar','Scatterplots'])

    if chart_options == 'DensityHeatmap':
        st.write("""
            Density and Bar Diagrams with categorical variables.    
            > 💡 Interact with the map by hovering the mouse over or try selecting an area.
        
        """)
        # Titulo
        st.sidebar.subheader("Density Heatmap Settings")

        x = st.sidebar.selectbox("X axis", options=text_cols)
        y = st.sidebar.selectbox("Y axis", options=text_cols)

        title_Densidade = "Density and Bar Diagrams with categorical variables"

        fig_dens = px.density_heatmap(df,  # Dataframe
        title=title_Densidade,                # Titulo
        x=x,                               # Variável Qualitativa Nominal
        y=y,                      # Variável Qualitativa Nominal
        #z= "MdaPotenciaOutorgadaKW" ,           # Variável Quantitativa Contínua
        marginal_x="histogram",               # Tipo de diagrama adicional para o eixo X
        marginal_y="histogram",               # Tipo de diagrama adicional para o eixo Y
        text_auto=True                        # Contagem para cada uma das células
        )
        st.plotly_chart(fig_dens)

    if chart_options == 'Bar':
        st.write("""
            Bar Chart with one numeric variable and two categorical.  
            > 💡 Interact with the map by hovering the mouse over or try selecting an area.
        
        """)
        # Titulo
        st.sidebar.subheader("Bar Chart Settings")

        x = st.sidebar.selectbox("X axis", options=text_cols)
        y = st.sidebar.selectbox("Y axis", options=numeric_cols)
        color_value = st.sidebar.selectbox("Color", options=text_cols)
        title_BarChart = "Bar Chart with Numeric and Categorical Variables" 

        fig_BarChart = px.bar(df,  # Dataframe
        title=title_BarChart,                # Titulo
        x=x,                               # Variável Qualitativa Nominal
        y=y,                      # Variável Qualitativa Nominal
        #z= "MdaPotenciaOutorgadaKW" ,           # Variável Quantitativa Contínua
        color=color_value,               # Tipo de diagrama adicional para o eixo X
        )
        st.plotly_chart(fig_BarChart)

    if chart_options == 'Scatterplots':

        st.write("""
            Scatterplots chart with two numeric variable and one categorical.  
            > 💡 Interact with the map by hovering the mouse over or try selecting an area.
        
        """)

        st.sidebar.subheader("Scatterplot Settings")

        x_values = st.sidebar.selectbox('X axis', options=numeric_cols)
        y_values = st.sidebar.selectbox('Y axis', options=numeric_cols)
        color_value = st.sidebar.selectbox("Color", options=text_cols)
        plot = px.scatter(data_frame=df, x=x_values, y=y_values, color=color_value)
        # display the chart
        st.plotly_chart(plot)


st.sidebar.write("""
---
""")

# Info & Repository

st.sidebar.subheader("📚 Info & Repository")





st.sidebar.write("""
---
##### I invite you to share your insights with me. 
##### Hope you enjoy the App! 😁
---
[V: 1.04221]
""")