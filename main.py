from pyspark.sql import SparkSession


def QueryProdRev():
     # create spark session
     spark = SparkSession.builder.appName("PySpark")\
         .config("spark.some.config.option", "some-value")\
         .getOrCreate()
     # load dataset
     Dataset = spark.read.csv("SalesTransactionV4a.csv", header=True, inferSchema=True)
     # add new column
     Dataset = Dataset.withColumn('Revenue', Dataset.Price*Dataset.Quantity)
     # create new dataframe
     ProductRevenue = Dataset.groupBy("ProductNo","ProductName")\
         .sum("Revenue")\
         .withColumnRenamed("sum(Revenue)", "SumRevenue")
     # create view for sql query
     ProductRevenue.createOrReplaceTempView("ProductRevenue")
     
     # display query result
     results_view = spark.sql("SELECT * FROM ProductRevenue WHERE ProductNo = '22491'")
     results_view.show()
     
     # output revenue of a product
     RevenueOutput = results_view.collect()[0][2]
     return RevenueOutput

if __name__ == "__main__":
     QueryProdRev()