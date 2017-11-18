# BigDataProject

### This is a project using Spark.

#### ¿Cómo ejecutar los programas?
*Si se quiere correr el programa se debe ejecutar el siguiente comando.

$ spark-submit  --master yarn --deploy-mode cluster  --executor-memory 2G  --num-executors 4 proyecto4.py 

# 1. Realizado por:
1. Mateo Hincapié Zapata - mhinca20@eafit.edu.co
2. Daniel Restrepo Aristizabal - drestr84@eafit.edu.co
3. Marcos David Sierra Gallego - msierr37@eafit.edu.co
### Estudiantes de la Universidad EAFIT

# 2. Introducción:
*En éste repositorio se encuentra un programa que realiza el agrupamiento de archivos por medio del algoritmo de KMeans.
El dataset que se está utilizando es una modificación de Gutenberg en español, la cual se encuentra en hdfs en un site de la materias Tópicos Especiales de Telemática. Éste dataset contiene 461 archivos.
# 3. Palabras clave:
* Dataset: Conjunto de datos que reside en memoria.
* KMeans
* Text Mining
* Data Mining
* Hashing TF
* TFIDF
# 4. Análisis y Diseño de algoritmos:
*Para empezar el programa se hicieron varias lecturas y se vieron algunos vídeos sobre Spark, además se buscaron varios ejemplos de cómo se debía utilizar KMeans y allí encontramos que debíamos utilizar otras bibliotecas como HashingTF e IDF.*
#### HashingTF: 
*En machine learning, la característica hashing, también conocida como el truco hash [1] (por analogía con el truco del kernel), es una forma rápida y eficiente de vectorizar características, es decir, convertir características arbitrarias en índices en un vector o matriz. Funciona aplicando una función hash a las características y utilizando sus valores hash como índices directamente, en lugar de buscar los índices en una matriz asociativa.*

#### TFIDF: 
*En la recuperación de información, tf-idf o TFIDF, abreviatura de term frequency–inverse document frequency, es una estadística numérica que pretende reflejar qué tan importante es una palabra para un documento en una colección o corpus. [1] A menudo se utiliza como un factor de ponderación en las búsquedas de recuperación de información, extracción de texto y modelado de usuarios. El valor de tf-idf aumenta proporcionalmente al número de veces que aparece una palabra en el documento, pero a menudo se compensa con la frecuencia de la palabra en el corpus, lo que ayuda a ajustar el hecho de que algunas palabras aparecen con más frecuencia en general. Hoy en día, tf-idf es uno de los esquemas de ponderación de términos más populares; El 83% de los sistemas de recomendación basados en texto en el dominio de las bibliotecas digitales usan tf-idf.*

#### KMeans:
*K-means es un método de agrupamiento, que tiene como objetivo la partición de un conjunto de n observaciones en k grupos en el que cada observación pertenece al grupo cuyo valor medio es más cercano. Es un método utilizado en minería de datos. El código para el Kmeans se obtuvo de varios links y repositorios de dónde se trató de entender su funcionamiento y gracias a los cuáles se pudo realizar el KMeans que se encuentra en los programas realizados.*
# 5. Análisis de solución:
*Pruebas con cantidades de datos diferentes corriendo en el DCA 192.168.10.75*
1. ![6 archivos](/Imagenes/6archivos.png)
2. ![12 archivos](/Imagenes/12archivos.png)
3. ![24 archivos](/Imagenes/24archivos.png)
4. ![80 archivos](/Imagenes/80archivos.png)
5. ![89 archivos](/Imagenes/89archivos.png)
6. ![126 archivos](/Imagenes/126archivos.png)
7. ![150 archivos](/Imagenes/150archivos.png)
8. ![461 archivos](/Imagenes/461archivos.png)
# 6. Comparación con HPC
1. ![Gráfica BigData vs HPC](/Imagenes/grafica.png)
# 6.Bibliografía:
1. https://spark.apache.org/docs/2.2.0/mllib-clustering.html
2. https://es.wikipedia.org/wiki/K-means
3. https://spark.apache.org/docs/1.0.1/api/java/org/apache/spark/mllib/clustering/KMeans.html
4. https://spark.apache.org/docs/2.2.0/mllib-feature-extraction.html
5. https://spark.apache.org/docs/1.1.1/api/java/org/apache/spark/rdd/RDD.html
6. https://spark.apache.org/docs/2.0.1/api/java/org/apache/spark/rdd/RDD.html
