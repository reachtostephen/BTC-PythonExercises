from pyspark import SparkContext
from pyspark import SparkFiles
from dotenv import load_dotenv

import os
load_dotenv()

file_dir = os.getenv("filedir")
file_name = "forsparkfile.R"

sc = SparkContext("local", "SparkFile App")
sc.addFile(file_name)

print("Absolute Path in Spark --> %s" %SparkFiles.get(file_name))
