# Proyecto-Data-Engineering
Proyecto para una empresa, en el área de análisis de datos  Data Engineering, donde se busca realizar las transformaciones requeridas y disponibilizar los datos mediante la elaboración y ejecución de una API.

##PROYECTO DE DATA ENGINEERING

El proyecto de ingenieria de datos tiene como objetivo la transformacion, extraccion y carga de los distintos data set suministrados para la ejecución del proyecto, posterior a esto, se busca que una vez la data se encuentre limpia, pueda ser cargada en un framework FastAPI para su posteior consumo, cumpliendo con unas consultas basicas o requerimientos exigidos por gerencia.

Se suministran 4 data set relacionados a diferentes plataforma de streaming Netflix, Amazon Prime, Disney + y Hulu, en donde se debe hacer un ETL. 

En el ETL se pide generar una columna llamada "ID"  que contenga la primera letra de la plataforma  junto con el "show id" el cual es otra columna del csv, tambien se solicita, que en la columna "rating" los valores nulos sean remplazados por la letra "G". Se solicita que en la columna "date added" tenga el formato AAAA-mm-dd, ademas de que todas las columnas de texto se encuentren en minusculas. En la columna "duration", se solicita que sea separa en 2; una columna que contenga el tipo de dato (minutos o temporadas) y otra que contenga el numero asociado a la duración.

Una vez sea realizado el ETL y se ha concatenado los 4 data set, se solicita realizar las siguientes consultas:

1. Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma

2. Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

3. La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

4. Película que más duró según año, plataforma y tipo de duración

5. Cantidad de series y películas por rating

 Finalmentes, se debe disponibilizar las consultas con la data limpia en un framework FastAPI, para el posterior consumo de la data.

