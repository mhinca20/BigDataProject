# BigDataProject

### This is a project using Spark.

#### ¿Cómo ejecutar los programas?
*Si se quiere correr el programa se debe ejecutar el siguiente comando. $ spark-submit --master yarn --deploy-mode cluster proyecto4.py 

# 1. Realizado por:
1. Mateo Hincapié Zapata - mhinca20@eafit.edu.co
2. Daniel Restrepo Aristizabal - drestr84@eafit.edu.co
3. Marcos David Sierra Gallego - msierr37@eafit.edu.co
### Estudiantes de la Universidad EAFIT

# 2. Introducción:
*En éste repositorio se encuentra un programa que realiza el agrupamiento de archivos por medio del algoritmo de KMeans.
El dataset que se está utilizando es una modificación de Gutenberg en español. Que se encuentra en el Ambari de la materias Tópicos Especiales de Telemática. Éste dataset contiene 461 archivos.
# 3. Palabras clave:
*Una de las palabras clave es la lista 'stopwords' que contiene una serie de palabras que deben ser eliminadas de cada documento leído ya que pueden ser redundantes y sin importancia por ser tan comunes en un texto.*
# 4. Análisis y Diseño de algoritmos:
*Para empezar el programa se hicieron varias lecturas y se vieron algunos vídeos sobre Spark, además se buscaron varios ejemplos de cómo se debía utilizar KMeans y allí encontramos que debíamos utilizar otras bibliotecas como HashingTF e IDF.
#### HashingTF:

#### IDF:

#### KMeans:
*K-means es un método de agrupamiento, que tiene como objetivo la partición de un conjunto de n observaciones en k grupos en el que cada observación pertenece al grupo cuyo valor medio es más cercano. Es un método utilizado en minería de datos. El código para el Kmeans se obtuvo de varios links y repositorios de dónde se trató de entender su funcionamiento y gracias a los cuáles se pudo realizar el KMeans que se encuentra en los programas realizados.*
# 5. Análisis de solución:
*Al correr los dos programas, cada uno con una cantidad de 100 documentos se observaron los siguientes aspectos*
1. ![Comando HTOP corriendo el programa en serial](/imagenes/htopSerial.png)
2. ![Tiempo de ejecución del programa en serial](/imagenes/serialTime.png)
3. ![Comando HTOP corriendo el programa en paralelo](/imagenes/htopParallel.png)
4. ![Tiempo de ejecución del programa en paralelo](/imagenes/parallelTime.png)
# 6.Bibliografía:
1. http://dataconomy.com/2015/04/implementing-the-five-most-popular-similarity-measures-in-python/
2. https://es.wikipedia.org/wiki/K-means
3. https://es.wikipedia.org/wiki/%C3%8Dndice_Jaccard
4. https://goo.gl/LL4CgA
