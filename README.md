

---

# Vinicius Guerra e Ribas -  Energy Sector Analyst
[Energy Engineer (UnB)](https://www.unb.br/) │ [Data Scientist and Analytics (USP)](https://www5.usp.br/)


## [📧 E-mail](mailto:viniciusgribas@gmail.com?Subject=%5BANALISE-ESPACIAL-ANEEL%5D%20-%20Contact) │ [:dart: Linkedin](https://www.linkedin.com/in/vinicius-guerra-e-ribas/) │ [:octocat: GitHub](https://github.com/viniciusgribas) 

---

# [Project Notebook](https://github.com/viniciusgribas/Analise_dados_geracao_BR/blob/main/Analise_Geracao_I/Master_Code.ipynb) [BR 🇧🇷] 

---
># Graphical and Spatial Exploratory Analysis - Brazil Electricity Generation Data from ANEEL [EN 🇬🇧] 

---

## Introduction

>### AUXILIARY BIBLIOGRAPHY
- Files

    - [Electricity Generation Information System (ANEEL SIGA)](https://app.powerbi.com/view?r=eyJrIjoiNjc4OGYyYjQtYWM2ZC00YjllLWJlYmEtYzdkNTQ1MTc1NjM2IiwidCI6IjQwZDZmOWI4LWVjYTctNDZhMi05MmQ0LWVhNGU5YzAxNzBlMSIsImMiOjR9)

    - [Brazilian Government Database](https://dados.gov.br/)

- Interesting Repositories on GitHub

    - [geodata-br](https://github.com/tbrugz/geodata-br)
    
    - [PyData-Book](https://github.com/wesm/pydata-book)
 
- Documentation

    - [Geopandas](https://geopandas.org/en/stable/)
    
    - [Plotly Express](https://plotly.github.io/plotly.py-docs/generated/plotly.express.html#module-plotly.express)

- Helpful Posts: [medium](https://medium.com) e [towardsdatascience](https://towardsdatascience.com):

    - [Best Libraries for Geospatial Data Visualisation in Python](https://towardsdatascience.com/best-libraries-for-geospatial-data-visualisation-in-python-d23834173b35)

    - [How to create and interactive map of Brazil using Plotly.Express-Geojson in Python](https://python.plainenglish.io/how-to-create-a-interative-map-using-plotly-express-geojson-to-brazil-in-python-fb5527ae38fc)
    - [Como criar gráficos interativos utilizando Plotly e Python](https://paulovasconcellos.com.br/como-criar-gr%C3%A1ficos-interativos-utilizando-plotly-e-python-3eb6eda57a2b)
    
    - [A Workflow for Data Visualization](https://towardsdatascience.com/a-workflow-for-data-visualization-c887d57d7ef1)


>### Introductory Remarks


 - The project consists of an exploratory data analysis. The objective of this analysis is to visualize the Brazilian electric generation system in a diagrammatic and spatial way, extracting insights. 

 - Two exploratory analyses are performed both with objects of type `GeoPandas` *(GeoDataFrame)*. In the first analysis a spatial object of type `GeoDataFrame - Points` with Cartesian coordinates (Latitude and Longitude). The second analysis is a spatial object of type `GeoDataFrame - Polygon` with the area of the corresponding geographical regions.

 - The standard report available on ANEEL's website is the [Electricity Generation Information System (ANEEL SIGA)](https://app.powerbi.com/view?r=eyJrIjoiNjc4OGYyYjQtYWM2ZC00YjllLWJlYmEtYzdkNTQ1MTc1NjM2IiwidCI6IjQwZDZmOWI4LWVjYTctNDZhMi05MmQ0LWVhNGU5YzAxNzBlMSIsImMiOjR9). The data for this report is available at [Brazilian Government Database](https://dados.gov.br/), onde foram extraídos e estudados. 

 - Finally the iterative data visualizations were exported in "HTML" files. Available at [`viniciusgribas.github.io`](https://github.com/viniciusgribas/viniciusgribas.github.io/tree/main/GeracaoANEEL_ParteI)

>[PART I PRODUCTS](https://github.com/viniciusgribas/Analise_dados_geracao_BR/tree/main/Analise_Geracao_I):

- [BarChart I](https://viniciusgribas.github.io/GeracaoANEEL_ParteI/Bar_GitHub_@viniciusgribas.html)
     
- [BarChart II](https://viniciusgribas.github.io/GeracaoANEEL_ParteI/Bar2_GitHub_@viniciusgribas.html)

- [DensityChart I](https://viniciusgribas.github.io/GeracaoANEEL_ParteI/Densidade_GitHub_@viniciusgribas.html)

- [DensityChart II](https://viniciusgribas.github.io/GeracaoANEEL_ParteI/Densidade_2_GitHub_@viniciusgribas.html)

- [DensityChart III](https://viniciusgribas.github.io/GeracaoANEEL_ParteI/Densidade_3_GitHub_@viniciusgribas.html)

- [StripChart I](https://viniciusgribas.github.io/GeracaoANEEL_ParteI/Strip_GitHub_@viniciusgribas.html)

- [RadarChart I](https://viniciusgribas.github.io/GeracaoANEEL_ParteI/Polar_GitHub_@viniciusgribas.html)

- [CartesianMap I](https://viniciusgribas.github.io/GeracaoANEEL_ParteI/Points_GitHub_@viniciusgribas.html)

>[PART I - MEDIUM POST]() [BR 🇧🇷] 


---
![image](https://user-images.githubusercontent.com/63691577/161199734-349a05b4-dfd6-40af-898a-7a08a3fd513d.png)

