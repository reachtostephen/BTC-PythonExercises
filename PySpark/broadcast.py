from pyspark import SparkContext

sc = SparkContext("local", "broadcast app")
words = sc.broadcast(['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu'])
data = words.value
print("The Broadcasted words are --> %s" % data)
print("Second value in the data --> %s" % data[1])
