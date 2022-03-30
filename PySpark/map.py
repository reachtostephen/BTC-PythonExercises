from pyspark import SparkContext

sc = SparkContext("local", "Map app")
words = sc.parallelize(
    ["scala",
     "java",
     "hadoop",
     "spark",
     "akka",
     "spark vs hadoop",
     "pyspark",
     "pyspark and spark"]
)
words_map = words.map(lambda a: (a, 1))
mapped_words = words_map.collect()
print("Key Value pair is set as --> %s" % mapped_words)
