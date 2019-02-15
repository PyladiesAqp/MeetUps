# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 09:50:35 2019

@author: PAULA
"""

import pandas as pd
import matplotlib.pyplot as plt 

#importar archivo
juegos = pd.read_csv("ign.csv")

#Una vez que hemos importado el archivo podemos presentar el nombre de las columnas en el 
#dataset.
print(juegos.columns)

#Para presentar las 4 primeras filas del dataset utilizaremos el método head
print(juegos.head(4))

#Para visualizar el número total de registros del dataset usaremos shape
print(juegos.shape)

#El resultado anterior indica que existen 18625 filas y 11 columnas. 
#Adicionalmente podemos visualizar la información de una o más columnas usando [] y 
#mostrar solo los 5 primeros registros del dataset
print(juegos[['score', 'release_year']].head())


#En Pandas el método corr permite determinar la correlación entre las columnas. 
#Al analizar la correlación podemos determinar si los juegos que han sido lanzados 
#recientemente (release_year) tienen una mejor calificación e incluso tomar en cuenta
# el mes del año y su influencia en la calificación (score) que recibió el juego.
print(juegos.corr())

#Como se puede visualizar en el resultado, ninguna de las columnas numéricas 
#tiene una correlación (ninguno de los valores numéricos en negrilla se acercan a 
#1) con el score lo cual indica que la fecha en la que fue liberado el juego no tiene 
#ninguna relación con la calificación del juego. 


#Operaciones Lógicas, podemos usar operadores para seleccionar registros que cumplan ciertas condiciones. 
#Extraer los videojuegos que tengan un score mayor que 6
print(juegos[juegos['score'] > 6])
 
#Extraer los videojuegos que tengan un score menor que 6
print(juegos[juegos['score'] < 6])
 
#Extraer los 5 primeros videojuegos que tengan un score mayor a 7 y que la plataforma sea Xbox
print(juegos[(juegos['score'] > 7) & (juegos['platform'] == "Xbox One")].head())


#Gráficos de los datos
#librería matplotlib, grafico pie

print('##################################')
print('##################################')
print('##################################')
juegos['platform'].value_counts()[:10].plot.pie(autopct='%1.1f%%',shadow=True)
fig=plt.gcf()
fig.set_size_inches(7,7)

#– Presenta las 10 primeras plataformas con más número de juegos
#juegos[‘platform’].value_counts()[:10]
#– Permite seleccionar pie como tipo de gráfico.
#plot.pie()
