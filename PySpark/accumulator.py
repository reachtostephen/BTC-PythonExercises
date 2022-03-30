from pyspark import SparkContext

sc = SparkContext("local", "Accumulator app")
num = sc.accumulator(10)


def f(n):
    global num
    num += n


li = sc.parallelize([20, 30, 40, 50])

li.foreach(f)
final = num.value
print("The Final Accumulated value --> %i" % final)
