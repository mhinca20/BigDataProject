from pyspark import SparkContext
from pyspark.mllib.clustering import KMeans
import sys

if __name__ == '__main__':
    dir = sys.argv[1]
    k=2
    iter = 10
    sc = SparkContext(appName="Proyecto4Spark")
    files = sc.wholeTextFiles(dir)
    namesF = files.keys().collect()
    dicDocuments = files.values().map(lambda document: document.split(" ")
