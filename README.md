# Análise Exploratória Espacial - Dados de Geração da ANEEL [BR :brazil:] 

---

# Vinicius Guerra e Ribas -  Energy Sector Analyst
[Energy Engineer (UnB)](https://www.unb.br/) │ [Data Scientist and Analytics (USP)](https://www5.usp.br/)


## [:email: E-mail](mailto:viniciusgribas@gmail.com?Subject=%5BANALISE-ESPACIAL-ANEEL%5D%20-%20Contact)│ [:dart: Linkedin](https://www.linkedin.com/in/vinicius-guerra-e-ribas/) │[:octocat: GitHub](https://github.com/viniciusgribas) 

---

# [Project Notebook](https://github.com/viniciusgribas/Analise_Espacial/blob/main/Master_Code.ipynb)

---



## Introdução

>### Fontes
- Arquivos

    - [Shapefile Brasil - Unidades Federativas](http://www.usp.br/nereus/?fontes=dados-shape-files)

    - [Sistema de Informações de Geração da ANEEL SIGA](https://app.powerbi.com/view?r=eyJrIjoiNjc4OGYyYjQtYWM2ZC00YjllLWJlYmEtYzdkNTQ1MTc1NjM2IiwidCI6IjQwZDZmOWI4LWVjYTctNDZhMi05MmQ0LWVhNGU5YzAxNzBlMSIsImMiOjR9)

    - [Banco de dados do Governo](https://dados.gov.br/)

- Repositórios Interessantes no GitHub

    - [geodata-br](https://github.com/tbrugz/geodata-br)
    
    - [PyData-Book](https://github.com/wesm/pydata-book)

    


- Documentação

    - [Folium Examples](https://python-visualization.github.io/folium/quickstart.html)

    - [Geopandas](https://geopandas.org/en/stable/)

- Postagens: [medium](https://medium.com) e [towardsdatascience](https://towardsdatascience.com):

    - [How to Create Eye-Catching Maps With Python and Kepler.gl](https://medium.com/nightingale/how-to-create-eye-catching-maps-with-python-and-kepler-gl-e7e897eff8ac)

    - [Best Libraries for Geospatial Data Visualisation in Python](https://towardsdatascience.com/best-libraries-for-geospatial-data-visualisation-in-python-d23834173b35)

    - [How to create and interactive map of Brazil using Plotly.Express-Geojson in Python](https://python.plainenglish.io/how-to-create-a-interative-map-using-plotly-express-geojson-to-brazil-in-python-fb5527ae38fc)


>### Considerações Iniciais


 - Este projeto consiste em uma análise exploratória de dados. O objetivo desta análise é localizar as principais fontes geradoras de energia elétrica no Brasil e visualiza-la de forma espacial.

 - O relatório padrão, disponibilizado no site da ANEEL de forma pública é o [Sistema de Informações de Geração da ANEEL (ANEEL SIGA)](https://app.powerbi.com/view?r=eyJrIjoiNjc4OGYyYjQtYWM2ZC00YjllLWJlYmEtYzdkNTQ1MTc1NjM2IiwidCI6IjQwZDZmOWI4LWVjYTctNDZhMi05MmQ0LWVhNGU5YzAxNzBlMSIsImMiOjR9). Os dados deste relatório, estão disponibilizados no [Banco de Dados do Governo Brasileiro](https://dados.gov.br/), onde foram extraídos e estudados. 

 - Já os arquivos .shp utilziados, foram extraídos do banco de dados da USP, contendo os [Shapefiles do Brasil por unidades federativas](http://www.usp.br/nereus/?fontes=dados-shape-files)
