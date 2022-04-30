
#############################################################################################
# ──────────────────────────────────────────────────────────────────────────────────────────#
# ─██████──██████─██████████████─████████████████───────────────────────────────────────────#
# ─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───────────────────────────────────────────#
# ─██░░██──██░░██─██░░██████████─██░░████████░░██───────────────────────────────────────────#
# ─██░░██──██░░██─██░░██─────────██░░██────██░░██───────────────────────────────────────────#
# ─██░░██──██░░██─██░░██─────────██░░████████░░██───────────────────────────────────────────#
# ─██░░██──██░░██─██░░██──██████─██░░░░░░░░░░░░██───────────────────────────────────────────#
# ─██░░██──██░░██─██░░██──██░░██─██░░██████░░████───────────────────────────────────────────#
# ─██░░░░██░░░░██─██░░██──██░░██─██░░██──██░░██─────────────────────────────────────────────#
# ─████░░░░░░████─██░░██████░░██─██░░██──██░░██████─────────────────────────────────────────#
# ───████░░████───██░░░░░░░░░░██─██░░██──██░░░░░░██─────────────────────────────────────────#
# ─────██████─────██████████████─██████──██████████─────────────────────────────────────────#
# ──────────────────────────────────────────────────────────────────────────────────────────#
# Dashboard_Geracao_Brasil-[23/04/2022]                                                     #
# ──────────────────────────────────────────────────────────────────────────────────────────#
#############################################################################################
# Vinicius Guerra e Ribas                                                                   #
## [Energy Engineer (UnB)] │ [Data Scientist & Analytics (USP)]                             #
#                                                                                           #
# github.com/viniciusgribas                                                                 #
#############################################################################################


# Library imports


##  Data Manipulation libraries


from distutils import text_file
import pandas as pd

import numpy as np

##  Web Scrapping library

import requests


# Create interactive charts and maps
import plotly.express as px
import plotly as plt
import plotly.figure_factory as ff
import plotly.graph_objects as go

# Create a Dashboard APP
import streamlit as st

st.set_page_config(
page_title = 'DASHBOARD_REPORT_GENBR-viniciusgribas',
page_icon='⚡'
)

# Making a load_data() func to improve performance

@st.cache
def load_data():
    # Function do Load Data

    patch = r"https://raw.githubusercontent.com/viniciusgribas/Analise_dados_geracao_BR/main/Analise_Geracao_II/Notebooks/output/CSV/Generation_Data.csv"

    response_API = requests.get(patch)
    
    df = pd.read_csv(patch ,encoding='utf-8')


    numeric_df = df[['MdaPotenciaFiscalizadaKW','MdaGarantiaFisicaKW','MdaPotenciaOutorgadaKW']]
    numeric_cols = numeric_df.columns

    text_df = df[[   'UF',
                     'TipoGeracao',
                     'Fase',
                     'OrigemCombustivel',
                     'FonteCombustivel',
                     'Outorga',
                     'NomeCombustivel',
                     'GeracaoQualificada',] ]
    text_cols = text_df.columns

    uf_column = df['UF']

    unique_uf = uf_column.unique()

    tipo_ger_column = df['TipoGeracao']

    unique_tipo_ger = tipo_ger_column.unique()

    df.DatEntradaOperacao = pd.to_datetime(df.DatEntradaOperacao)
    df.DatInicioVigencia  = pd.to_datetime(df.DatInicioVigencia)
    df.DatFimVigencia = pd.to_datetime(df.DatFimVigencia)
    df.ETL_CreatedDataLoad_At = pd.to_datetime(df.ETL_CreatedDataLoad_At)
    df.ETL_DataBase_LastModified = pd.to_datetime(df.ETL_DataBase_LastModified)
    print('CREATION DATE [',df.ETL_CreatedDataLoad_At[1], ']') # Time this file was generated by the ETL
    print('LAST SERVER UPDATE ON DATA [',df.ETL_DataBase_LastModified[1],']') # Time the host last updated the file

    return (df, numeric_cols, text_cols, unique_tipo_ger,unique_uf)


df, numeric_cols, text_cols, unique_tipo_ger, unique_uf = load_data()

#################
#  START HEAD   #
#################

# Simple Text
st.write("""
---
####  Vinicius Guerra e Ribas
###### [📧 E-mail](mailto:viniciusgribas@gmail.com?Subject=%5BGENERATION-SECTOR-DASHBOARD-REPORT%5D%20-%20Contact) │ [🎯 Linkedin](https://www.linkedin.com/in/vinicius-guerra-e-ribas/) │ [😸 GitHub](https://github.com/viniciusgribas) 
---
# 🇧🇷⚡
#  Brazil Generation Sector Dashboard 
### A Interactive Dashboard Report.

---
 """)

## Guide Expander
with st.expander("❗ GUIDE ❗"):
     st.write("""
     > ↖️ Explore the **⚙️ Tools** in the top left corner.
    - 📣 In **🧰 General Tools** you can view the database, metadata information and the basics relationships between categorical variables.

    - 📣 The **💡 Insight's & Analysis Tools** tab contains interactive charts divided into two sections:
        - The "General Analysis" contains analyses that make sense for this business type.
        - The "Try Analysis" tab allows the user to input variables.

    - 📣 The **📚 Info & Repository** tab contains information about this dashboard report and its repository.

    - 📍 Always remember to put the charts in full screen, this will make your analysis easier.

    - 📍 You can leave only one, all or zero checkboxes in the sidebar at left.



    """)

#################
#  END   HEAD   #
#################

########################
# START SIDEBAR HEAD   #
########################

# Sidebar simple Text
st.sidebar.write("""
    > # ⚙️ TOOLS ⬇️ 
""")
st.sidebar.write("""
---
""")

# GENERAL TOOLS
st.sidebar.write("""
    > ## 🧰 General Tools
    """)
# add  Dataset to sidebar
check_box = st.sidebar.checkbox(label=" Dataset 🗃️")
if check_box:
    # lets show the dataset
    st.write("""# 🗃️ DATASET """)
    st.write(df)

# add  Metadata to sidebar
check_box = st.sidebar.checkbox(label=" Metadata 🔎")
if check_box:
    # lets show the dataset
    st.write("""# 🔎 VARIABLE METADATA """)
    st.write( """

 | Variable                 | Type        | Meaning                      |
 |--------------------------|-------------|------------------------------|
 | MdaGarantiaFisicaKW      | Numerical   | Physical Guarantee of Energy |
 | MdaPotenciaFiscalizadaKW | Numerical   | Supervised Electric Power    |
 | MdaPotenciaOutorgadaKW   | Numerical   | Granted Electric Power       |
 | Empreendimento           | Categorical | Business Name                |
 | UF                       | Categorical | Brasil States                |
 | TipoGeracao              | Categorical | Generation Type              |
 | Fase                     | Categorical | Operational Phase            |
 | OrigemCombustivel        | Categorical | Fuel Origin                  |
 | FonteCombustivel         | Categorical | Fuel Source                  |
 | NomeCombustivel          | Categorical | Fuel Name                    |
 | Outorga                  | Categorical | Grant                        |
 | GeracaoQualificada       | Categorical | Qualified Generation Mode    |
 | DatEntradaOperacao       | Date-Time   | Operation Start Date         |
 | DatInicioVigencia        | Date-Time   | Contract Start Date       |
 | DatFimVigencia           | Date-Time   | Contract End Date         |
 | X                        | Geographic  | Longitude Values             |
 | Y                        | Geographic  | Latitude Values              |
 |  ETL_CreatedDataLoad_At    |  Date-Time   | DataFrame creation date      |
 |  ETL_DataBase_LastModified |  Date-Time   | DataFrame Last Updated       |

""")

check_box = st.sidebar.checkbox(label="Categorical Variables Relations 🧭")
if check_box:
    # lets show the dataset
    st.write("""# 🧭 INTERACTIVE HIERARCHY""")
    st.write("""
        Interactive alluvial diagram with hierarchical variables

        > 💡 Interact with the Chart by dragging the headlines
        
        """)
    fig = px.parallel_categories(df,
        dimensions  = ['GeracaoQualificada','Fase','Outorga','OrigemCombustivel','TipoGeracao','FonteCombustivel','NomeCombustivel'],
        labels ={'GeracaoQualificada','Fase','Outorga','OrigemCombustivel','TipoGeracao','FonteCombustivel','NomeCombustivel'}
        )
    st.plotly_chart(fig)

st.sidebar.write("""
---
""")

# INSIGHTS E ANALYSIS TOOLS
st.sidebar.write("""
> ## 💡 Insight's & Analysis Tools
""")

##########################
#  START GENERAL ANALYSES  #
##########################
st.sidebar.write("""
 -  ### General Analyses 📊
 """)
#----------------------
## GEOGRAPHICAL ANALYSES
#----------------------

check_box = st.sidebar.checkbox(label="Geographical 🗺️")
if check_box:
    # Cartesian Coordinate Map
    st.write("""
    ##  Interactive Cartesian Coordinate Map 🗺️

    > 💡 interact with the map by moving your cursor and zooming in, or filter the generation types in the legends.



    """)
    df_map = df.get(df['X']!=0.0)
    fig_pointsMap = px.scatter_mapbox(df_map,                                         
        lat="Y",                                              
        lon="X",                                              
        color="TipoGeracao",                       
        size="MdaPotenciaOutorgadaKW",                        
        color_continuous_scale=px.colors.sequential.matter,   
        hover_name = "Empreendimento",                
        hover_data = ["MdaPotenciaOutorgadaKW"],
        title= 'Iterative Cartesian Coordinate Map',              
        size_max=80,                                          
        zoom=3,                                               
        mapbox_style='open-street-map',                      
        animation_frame='Fase'                        
        )

    st.plotly_chart(fig_pointsMap)
#----------------------
## TIMELINE ANALYSES
#----------------------
check_box = st.sidebar.checkbox(label="Timeline 📆")
if check_box:
    #FIXED MESSAGE
    st.write("""
    ##  Interactive Timeline Chart's 📆

    > 💡 interact with the map by moving your cursor and zooming in, or filter the generation types in the legends.

    > 📍 In the sidebar on the left, select one of DataTime variables:
     | Variable                 | Type        | Meaning                      |
     |--------------------------|-------------|------------------------------|
     | DatEntradaOperacao       | Date-Time   | Operation Start Date         |
     | DatInicioVigencia        | Date-Time   | Contract Start Date       |
     | DatFimVigencia           | Date-Time   | Contract End Date         |

     > 📍 Remember to put on full screen for better viewing.


    """)
    df_data = df.get(df['DatInicioVigencia']>'1901')    
    df_data = df.get(df['DatFimVigencia']>'1901')
    df_data_op = df.get(df['DatEntradaOperacao']>'1901')

    chart_select = st.sidebar.radio(
    label="Select one of DataTime variables:",
    options=['DatEntradaOperacao','DatInicioVigencia','DatFimVigencia'])

# DatEntradaOperacao
    if chart_select == 'DatEntradaOperacao':
        st.write("""
        ---
        # DatEntradaOperacao
        ## Operation Start Date 
        ---
        """)
        fig_box = px.box(df_data_op,
        title='DatEntradaOperacao',
        x='TipoGeracao',
        y="DatEntradaOperacao",
        hover_name='Empreendimento',
        color='TipoGeracao',
        points="all",
        width= 1000,
        height= 600,
        animation_frame='Fase'
        
        )

        st.plotly_chart(fig_box)

        st.write("""
        ---
        """)        
        fig_histogram = px.histogram(df_data_op,
            title='DatEntradaOperacao',
            x="DatEntradaOperacao",
            marginal='violin',
            color = 'Fase',
            barmode='group',
            animation_frame='TipoGeracao',
            labels='TipoGeracao',
            range_y = (0,200),
            width= 1000,
            height= 600 
        )

        st.plotly_chart(fig_histogram)
        
        st.write("""
       ---
        """)
        fig_dens = px.density_heatmap(df_data_op, 
        title='Timeline - GrantedPower - DatEntradaOperacao',                
        x="DatEntradaOperacao",                               
        y="TipoGeracao",                     
        z= "MdaPotenciaOutorgadaKW" ,         
        marginal_x="histogram",              
        marginal_y="histogram",               
        text_auto=True,
        width= 1500,
        height= 800,
        animation_frame='Fase'               
        )
        st.plotly_chart(fig_dens)

# DatInicioVigencia
    if chart_select == 'DatInicioVigencia':
        st.write("""
        ---
        # DatInicioVigencia
        ## Contract Start Date 
        ---
        """)
        fig_box = px.box(df_data,
        title='DatInicioVigencia',
        x='TipoGeracao',
        y="DatInicioVigencia",
        hover_name='Empreendimento',
        color='TipoGeracao',
        points="all",
        width= 1000,
        height= 600,
        animation_frame='Fase'
        
        )

        st.plotly_chart(fig_box)

        st.write("""
        ---
        """)        
        fig_histogram = px.histogram(df_data,
            title='DatInicioVigencia',
            x="DatInicioVigencia",
            marginal='violin',
            color = 'Fase',
            barmode='group',
            animation_frame='TipoGeracao',
            labels='TipoGeracao',
            range_y = (0,200),
            width= 1000,
            height= 600 
        )

        st.plotly_chart(fig_histogram)
        
        st.write("""
       ---
        """)
        fig_dens = px.density_heatmap(df_data, 
        title='Timeline - GrantedPower - DatInicioVigencia',                
        x="DatInicioVigencia",                               
        y="TipoGeracao",                     
        z= "MdaPotenciaOutorgadaKW" ,         
        marginal_x="histogram",              
        marginal_y="histogram",               
        text_auto=True,
        width= 1500,
        height= 800,
        animation_frame='Fase'               
        )
        st.plotly_chart(fig_dens)

# DatFimVigencia
    if chart_select == 'DatFimVigencia':
        st.write("""
        ---
        # DatFimVigencia
        ## Contract End Date  
        ---
        """)
        fig_box = px.box(df_data,
        title='DatFimVigencia',
        x='TipoGeracao',
        y="DatFimVigencia",
        hover_name='Empreendimento',
        color='TipoGeracao',
        points="all",
        width= 1000,
        height= 600,
        animation_frame='Fase'
        
        )

        st.plotly_chart(fig_box)

        st.write("""
        ---
        """)        
        fig_histogram = px.histogram(df_data,
            title='DatFimVigencia',
            x="DatFimVigencia",
            marginal='violin',
            color = 'Fase',
            barmode='group',
            animation_frame='TipoGeracao',
            labels='TipoGeracao',
            range_y = (0,200),
            width= 1000,
            height= 600 
        )

        st.plotly_chart(fig_histogram)
        
        st.write("""
       ---
        """)
        fig_dens = px.density_heatmap(df_data, 
        title='Timeline - GrantedPower - DatFimVigencia',                
        x="DatFimVigencia",                               
        y="TipoGeracao",                     
        z= "MdaPotenciaOutorgadaKW" ,         
        marginal_x="histogram",              
        marginal_y="histogram",               
        text_auto=True,
        width= 1500,
        height= 800,
        animation_frame='Fase'               
        )
        st.plotly_chart(fig_dens)

#----------------------
## CLUSTER ANALYSES
#----------------------
check_box = st.sidebar.checkbox(label="Cluster 🔗")
if check_box:
    #FIXED MESSAGE
    st.write("""
    ##  Interactive Cluster Chart's 🔗

    > 💡 interact with the graph by clicking on the desired section.

    > 📍 Remember to put on full screen for better viewing.


    """)

# Sunburst Chart
    st.write("""
    ---
    """)

    fig_SunBurstChart = px.sunburst(df, 
    path=[px.Constant('BRASIL'),
    'Fase',
    "UF",
    'TipoGeracao'],
    values='MdaPotenciaOutorgadaKW',
    title= 'Sunburst Chart: Granted Power by Phase, Type of Generation and States in Brazil',
    width=750,
    height=750,
    maxdepth = -1  )
    st.plotly_chart(fig_SunBurstChart)
# Treemap Chart
    st.write("""
    ---
    """)
    fig_treemapChart = px.treemap(df, 
    path=[px.Constant('BRASIL'),
    "Fase",
    'OrigemCombustivel',
    'FonteCombustivel',
    'UF'
    ],
    values='MdaPotenciaOutorgadaKW',
    title= 'TreeMap Chart: Granted Power by Phase, Type of Generation and States in Brazil',
    width=750*2,
    height=750,
    maxdepth = -1  )
    st.plotly_chart(fig_treemapChart)      

#----------------------
##  Cross-Variables ANALYSES
#----------------------
check_box = st.sidebar.checkbox(label="Cross-Variables 🧮")
if check_box:
    #FIXED MESSAGE
    st.write("""
    ##  Interactive Cross-Variables Chart's 🧮 - Categorical and Numerical

    > 💡 interact with the graph by clicking on the desired section.

    > 📍 Remember to put on full screen for better viewing.


    """)

# bar Chart
    st.write("""
    ---
   ##### 🔷 Two Categorical Variables and One Numerical Variables
    
    ---

    """)
    fig_BarChart = px.bar(df, 
    x="UF",                      
    y="MdaPotenciaOutorgadaKW",  
    color="TipoGeracao",         
    hover_name='Fase',
    title='Bar Chart - Power Granted by States, Generation Type and Phase',        
    width=800,                   
    height=1000,                 
    animation_frame='Fase'
    )
    st.plotly_chart(fig_BarChart)

# strip chart
    st.write("""
    ---
    ##### 🔷 Three Categorical Variables and One Numerical Variables
    ---

    """)

    fig_Strip = px.strip(df,  
    x="MdaPotenciaOutorgadaKW",  
    y="UF",                      
    orientation="h",            
    hover_name="Empreendimento",
    title = 'Strip Chart - Power Granted by States, Generation Type, Phase and Business',
    color="TipoGeracao",      
    animation_frame='Fase'
    )
    st.plotly_chart(fig_Strip)

# 3d chart
    dfGuarantee=df.get(df.MdaGarantiaFisicaKW > 0)

    st.write("""
    ---
    ##### 🔷 Three Categorical Variables and Two Numerical Variables
    ---

    """)
    fig_Strip3d = px.scatter_3d(dfGuarantee,
    x='MdaPotenciaOutorgadaKW',
    y='MdaGarantiaFisicaKW',
    z='UF',
    color='TipoGeracao',
    title= '3D Chart - Granted Power and Physical Guarantee by States, Generation Type, Phase and Business',
    hover_name='Empreendimento',
    symbol='TipoGeracao', 
    animation_frame='Fase')
    
    st.plotly_chart(fig_Strip3d)
     


##########################
#  END GENERAL ANALYSES  #
##########################

##########################
#  START TRY ANALYSES  #
##########################

st.sidebar.write("""
 - ### Try Analyses 🧪
 """)

check_box = st.sidebar.checkbox(label="Multi-Variables 🔬")
if check_box:
    # lets show the dataset
    st.write("""
    #  Try Analyses 🧪
    
    > 💡 interact with the graph by clicking on the desired section.

    > 📍 Remember to put on full screen for better viewing.
    
    """)

    chart_options = st.sidebar.radio(
    label="Select the type of chart for your analysis",
    options=['DensityHeatmap','Bar','3D Scatterplots'])

    if chart_options == 'DensityHeatmap':
        st.write("""
            Density and Bar Diagrams with categorical variables.    
            > 💡 Interact with the map by hovering the mouse over or try selecting an area.
        
        """)
        # Titulo
        st.sidebar.subheader("Density Heatmap Settings")

        x = st.sidebar.selectbox("X axis", options=text_cols)
        y = st.sidebar.selectbox("Y axis", options=text_cols)
        z = st.sidebar.selectbox("Z axis", options=numeric_cols)

        title_Densidade = "Density and Bar Diagrams with categorical variables"

        fig_dens = px.density_heatmap(df,  
        title=title_Densidade,              
        x=x,                              
        y=y,                      
        z= z,           
        marginal_x="histogram",               
        marginal_y="histogram",              
        text_auto=True,                      
        width= 1500,
        height= 800,
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

    if chart_options == '3D Scatterplots':

        st.write("""
            Scatterplots chart with two numeric variable and one categorical.  
            > 💡 Interact with the map by hovering the mouse over or try selecting an area.
        
        """)

        st.sidebar.subheader("Scatterplot Settings")

        x_values = st.sidebar.selectbox('X axis', options=numeric_cols)
        y_values = st.sidebar.selectbox('Y axis', options=numeric_cols)
        z_values = st.sidebar.selectbox('Z axis', options=text_cols)
        symbol_values =st.sidebar.selectbox("symbol", options=text_cols)
        color_value = st.sidebar.selectbox("Color", options=text_cols)

        plot = px.scatter_3d(data_frame=df,
        x=x_values,
        y=y_values,
        z=z_values,
        hover_name='Empreendimento',
        symbol=symbol_values,
        color=color_value)
        # show the chart
        st.plotly_chart(plot)


st.sidebar.write("""
---
""")
##########################
#  END TRY ANALYSES  #
##########################


# Info & Repository

st.sidebar.subheader("📚 Info & Repository")
with st.sidebar.expander("Info 🦉"):
    st.write("""
     This Dashboard Report is  Data Engineering solution 
    developed to provide Brazilian Electric Generation data in a dashboard type report, 
    prioritizing to be iterative, dynamic and autonomous. 
    Accessible by specialists in a timely manner.

    A Report made with ❤️ by [viniciusgribas](https://github.com/viniciusgribas)
""")



with st.sidebar.expander("Repository 😸"):
    st.write("""

    The workflow adopted is presented in the following repositories:

[🔶 ETL PROCESS ⚙️](https://viniciusgribas.github.io/Dashboard_Report_Brasil_GenData/ELT_Notebook.html)

[🔶 EXPLORATORY ANALISYS 🧪](https://viniciusgribas.github.io/Dashboard_Report_Brasil_GenData/Exploratory_Analysis.html)

[🔶 DASHBOARD PYTHON FILE 📱](https://raw.githubusercontent.com/viniciusgribas/Analise_dados_geracao_BR/main/Analise_Geracao_II/Py/Dashboard_Geracao_Brasil_app.py)

""")


st.sidebar.write("""
---
##### *I invite you to share your insights with me.* 
##### *Hope you enjoy the App!* 😁

#### [*Please feel free to contact me.*](mailto:viniciusgribas@gmail.com?Subject=%5B-GENERATION-SECTOR-DASHBOARD%5D%20-%20Insights)
---
#### Brazil Generation Sector Dashboard
##### A Interactive Dashboard Report.
####  Vinicius Guerra e Ribas
###### [📧 E-mail](mailto:viniciusgribas@gmail.com?Subject=%5BGENERATION-SECTOR-DASHBOARD-REPORT%5D%20-%20Contact) │ [🎯 Linkedin](https://www.linkedin.com/in/vinicius-guerra-e-ribas/) │ [😸 GitHub](https://github.com/viniciusgribas) 
---

[V: 2.0220430]
""")