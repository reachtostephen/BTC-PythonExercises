from pyspark.context import SparkContext
from pyspark.serializers import MarshalSerializer

sc = SparkContext("local", "serialization app", serializer=MarshalSerializer())
data = sc.parallelize(list(range(1000))).map(lambda x: 2 * x).take(10)  # take - First n elements
print(data)
sc.stop()
