from pyspark import SparkContext
from pyspark.mllib.feature import HashingTF, IDF
from pyspark.mllib.clustering import KMeans
import sys

if __name__ == '__main__':
    k=4
    iter = 10
    sc = SparkContext(appName="Proyecto4Spark")
    files = sc.wholeTextFiles("hdfs:///datasets/gutenberg-txt-es/*.txt")
    namesF = files.keys().collect()
    dicDocuments = files.values().map(lambda document: document.split(" "))
    hashingTF = HashingTF()
    tf = hashingTF.transform(dicDocuments)
    idf = IDF().fit(tf)
    tfidf = idf.transform(tf)
    model = KMeans.train(tfidf, k, maxIterations=iter)
    clusters = model.predict(tfidf).collect()
    groups={}
    for i in range(len(namesF)):
        if clusters[i] in groups:
            groups[clusters[i]].append(namesF[i])
        else:
            groups[clusters[i]]=[namesF[i]]
    
    fileS = sc.parallelize(groups.items())
    fileS.saveAsTextFile("hdfs:///user/msierr37/proyecto4")
