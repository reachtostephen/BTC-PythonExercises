import db_connect
import queries
import pandas as pds


engine = db_connect.Engine()
engine_conn = engine.db

query_obj = queries.Queries(engine_conn)
studentScores = [(57, 61, 76, 56, 67),
                 (77, 67, 65, 78, 62),
                 (65, 71, 56, 63, 70)
                 ]
dataFrame = pds.DataFrame(studentScores,
                          index=(1211, 1212, 1213),
                          columns=("Physics", "Chemistry", "Biology", "Mathematics", "Language"))

query_obj.create("Students", dataFrame)
query_obj.select("Students")

del engine
