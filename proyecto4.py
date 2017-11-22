from pyspark import SparkContext
from pyspark.mllib.feature import HashingTF, IDF
from pyspark.mllib.clustering import KMeans
import sys

if __name__ == '__main__':
    #se inicializan el k y el numero de iteraciones para el k-means
    k=4
    iter = 10
    #se inicia el contexo de spark
    sc = SparkContext(appName="Proyecto4Spark")
    #se leen los archvos en el formato clave valor, la clave es el nombre del documento y el valor todo su contenido
    files = sc.wholeTextFiles("hdfs:///datasets/gutenberg-txt-es/*.txt")
    #se obtienen los nombres de todos los documentos
    namesF = files.keys().collect()
    #se obtienen las palabras de todos los documentos
    dicDocuments = files.values().map(lambda document: document.split(" "))
    #Se inicia el objeto hash para hacer el tf e idf
    hashingTF = HashingTF()
    #Se obtiene la frecuencia de palabras en cada documento
    tf = hashingTF.transform(dicDocuments)
    #Se obtiene la importancia de cada palabra en los documentos 
    idf = IDF().fit(tf)
    #se multiplica la frecuencia por la importancia de la palabra para obtener la matriz 
    tfidf = idf.transform(tf)
    #se obtiene el modelo de los cluster con la matriz tfidf
    model = KMeans.train(tfidf, k, maxIterations=iter)
    #se predice el modelo para obtener los cluster a los que pertenece cada archivo
    clusters = model.predict(tfidf).collect()
    #Se relaciona el nombre de cada documento con el cluster al que pertenece
    #y se guarda en un diccionario como clave cada cluster y como valor un arreglo con los documentos que pertenecen a el
    groups={}
    for i in range(len(namesF)):
        if clusters[i] in groups:
            groups[clusters[i]].append(namesF[i])
        else:
            groups[clusters[i]]=[namesF[i]]
    #Se convierte el diccionario con la respuesta a RDD para poderlo guardar como un archivo en HDFS
    fileS = sc.parallelize(groups.items())
    fileS.saveAsTextFile("hdfs:///user/msierr37/proyecto4")
    #Aqui se cierra el SparkContext
    sc.stop()
