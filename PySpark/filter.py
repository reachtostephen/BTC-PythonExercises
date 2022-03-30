from pyspark import SparkContext

sc = SparkContext("local", "Filter app")
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

words_filter = words.filter(lambda x: 'spark' in x)
filtered_words = words_filter.collect()
print("Filtered RDD --> %s" % filtered_words)
