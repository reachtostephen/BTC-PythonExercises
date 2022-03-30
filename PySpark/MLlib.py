# Recommendation

from __future__ import print_function
from pyspark import SparkContext
from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating

# Rating(int user, int product, double rating)

if __name__ == "__main__":
    sc = SparkContext(appName="PySpark MLlib App")
    data = sc.textFile("test.data")
    ratings = data.map(lambda l: l.split(',')).map(lambda l: Rating(int(l[0]), int(l[1]), float(l[2])))
    rank = 10
    numIterations = 10
    model = ALS.train(ratings, rank, numIterations)  # rank - presumed latent

    testdata = ratings.map(lambda p: (p[0], p[1]))

    predictions = model.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))
    ratesAndpreds = ratings.map(lambda r: ((r[0], r[1]), r[2])).join(predictions)
    # print(ratesAndpreds.collect())
    MSE = ratesAndpreds.map(lambda r: (r[1][0] - r[1][1]) ** 2).mean()
    print("Mean Squared Error = " + str(MSE))

    model.save(sc, "target/tmp/myCollaborativeFilter")
    loadModel = MatrixFactorizationModel.load(sc, "target/tmp/myCollaborativeFilter")
