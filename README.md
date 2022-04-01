

---

# Vinicius Guerra e Ribas -  Energy Sector Analyst
[Energy Engineer (UnB)](https://www.unb.br/) │ [Data Scientist and Analytics (USP)](https://www5.usp.br/)


## [📧 E-mail](mailto:viniciusgribas@gmail.com?Subject=%5BANALISE-ESPACIAL-ANEEL%5D%20-%20Contact)│ [:dart: Linkedin](https://www.linkedin.com/in/vinicius-guerra-e-ribas/) │[:octocat: GitHub](https://github.com/viniciusgribas) 

---

# [Project Notebook](https://github.com/viniciusgribas/Analise_Espacial/blob/main/Master_Code.ipynb)

---
># Graphical and Spatial Exploratory Analysis - Brazil Electricity Generation Data from ANEEL [EN 🇬🇧] 

---

## Introduction

>### AUXILIARY BIBLIOGRAPHY
- Files

    - [Shapefile Brasil - UF](http://www.usp.br/nereus/?fontes=dados-shape-files)

    - [Electricity Generation Information System (ANEEL SIGA)](https://app.powerbi.com/view?r=eyJrIjoiNjc4OGYyYjQtYWM2ZC00YjllLWJlYmEtYzdkNTQ1MTc1NjM2IiwidCI6IjQwZDZmOWI4LWVjYTctNDZhMi05MmQ0LWVhNGU5YzAxNzBlMSIsImMiOjR9)

    - [Brazilian Government Database](https://dados.gov.br/)

- Interesting Repositories on GitHub

    - [geodata-br](https://github.com/tbrugz/geodata-br)
    
    - [PyData-Book](https://github.com/wesm/pydata-book)

    


- Documentation

    - [Folium Examples](https://python-visualization.github.io/folium/quickstart.html)

    - [Geopandas](https://geopandas.org/en/stable/)
    
    - [Plotly Express](https://plotly.github.io/plotly.py-docs/generated/plotly.express.html#module-plotly.express)

- Helpful Posts: [medium](https://medium.com) e [towardsdatascience](https://towardsdatascience.com):

    - [How to Create Eye-Catching Maps With Python and Kepler.gl](https://medium.com/nightingale/how-to-create-eye-catching-maps-with-python-and-kepler-gl-e7e897eff8ac)

    - [Best Libraries for Geospatial Data Visualisation in Python](https://towardsdatascience.com/best-libraries-for-geospatial-data-visualisation-in-python-d23834173b35)

    - [How to create and interactive map of Brazil using Plotly.Express-Geojson in Python](https://python.plainenglish.io/how-to-create-a-interative-map-using-plotly-express-geojson-to-brazil-in-python-fb5527ae38fc)


>### Introductory Remarks


 - This project consists of an exploratory data analysis. The goal of this work is to visualize the Brazilian Electric Generation System in a graphic and spatial perspective extracting insights.

 - Two exploratory analyses are performed both with objects of type `GeoPandas` *(GeoDataFrame)*. In the first analysis a spatial object of type `GeoDataFrame - Points` with Cartesian coordinates (Latitude and Longitude). The second analysis is a spatial object of type `GeoDataFrame - Polygon` with the area of the corresponding geographical regions.

 - The standard report available on ANEEL's website is the [Electricity Generation Information System (ANEEL SIGA)](https://app.powerbi.com/view?r=eyJrIjoiNjc4OGYyYjQtYWM2ZC00YjllLWJlYmEtYzdkNTQ1MTc1NjM2IiwidCI6IjQwZDZmOWI4LWVjYTctNDZhMi05MmQ0LWVhNGU5YzAxNzBlMSIsImMiOjR9). The data for this report is available at [Brazilian Government Database](https://dados.gov.br/), onde foram extraídos e estudados. 

 - The file `.shp` was extracted from the USP's database containing the [Shapefiles from Brasil by UF](http://www.usp.br/nereus/?fontes=dados-shape-files)

 - Similarly to the above the files containing the geometry of Brazil in `JSON` were extracted from [Brazil Geojson]('https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson')

 - Highlights include the libraries used for data visualization and manipulation especially the GeoPandas, Folium, and plotly express libraries.
 
 - Finally the iterative data visualizations were exported in "HTML" files. Available at [`viniciusgribas.github.io`](https://github.com/viniciusgribas/viniciusgribas.github.io/tree/main/Analises_Espaciais)

>[PART I - Spatial and Graphical Exploratory Analysis Using Python](https://github.com/viniciusgribas/Analise_Espacial/blob/main/Spatial_Analysis_I/GeoDataFrame_Point.ipynb)


---
![image](https://user-images.githubusercontent.com/63691577/161199734-349a05b4-dfd6-40af-898a-7a08a3fd513d.png)

