from pyspark import SparkContext

sc = SparkContext("local", "Cache app")
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
cache = words.cache()
is_cached = cache.persist().is_cached
print("RDD is cached --> %s" % is_cached)
