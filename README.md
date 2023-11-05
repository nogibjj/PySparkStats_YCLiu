[![Python Continuous Integration with Github Actions](https://github.com/nogibjj/PySparkStats_YCLiu/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/PySparkStats_YCLiu/actions/workflows/main.yml)

## Use PySpark To Transform and Query Data

This repository demonstrates using **PySpark to transform and query a large dataset**. PySpark is the API for Apache Spark. Thanks to the idea of the reselient distributed dataset(RDD), Spark can be used for to manipulate data efficiently on larger dataset because it can distribute work on multiple (cores) of machines. 

The **dataset used** for demonstration is the **transaction records of an E-Commerce company in UK**, downloaded from [kaggle](https://www.kaggle.com/datasets/gabrielramos87/an-online-shop-business), with ~0.54 million rows of data with the following columns: TransactionNo, Date, ProductNo, ProductName, Price, Quantity, CustomerNo, Country.

Below is an overview of the repository:
   
1. **Main functions for querying on Dataset**
   <br>a. _main.py_: load transactionn dataset and **query the aggregated revenue of the a product**. Specifically, it executes the following:
   <br>         1. Start a spark session.
   <br>`spark = SparkSession.builder.appName("PySpark").config("spark.some.config.option", "some-value").getOrCreate()`<br>
   <br>         2. Load dataset.
   <br>`Dataset = spark.read.csv("SalesTransactionV4a.csv", header=True, inferSchema=True)`<br>
   <br>         3. Create column _Revenue_ by **multiplying the unit price and quantity sold** of a given product.
   <br>`Dataset = Dataset.withColumn('Revenue', Dataset.Price*Dataset.Quantity)`<br>
   <br>         4. **Aggregate the Revenue of each product** using the column name _SumRevenue_.
   <br>`ProductRevenue = Dataset.groupBy("ProductNo","ProductName").sum("Revenue").withColumnRenamed("sum(Revenue)", "SumRevenue")`<br>
   <br>         5. **Create view** and **query the product of interest**.
   <br>`ProductRevenue.createOrReplaceTempView("ProductRevenue")
    results_view = spark.sql("SELECT * FROM ProductRevenue WHERE ProductNo = '22491'")
    results_view.show()`<br>
    
   **Resulting table**
   
   | ProductNo | ProductName | SumRevenue |
   |---|---|---|
   |22491| Pack Of 12 Coloured Pencil | 43233.17 |

<br>         5. **Output the revenue** of  **the product of interest**.
    <br>`RevenueOutput = results_view.collect()[0][2]`
    <br>`return RevenueOutput`<br>

   <br>d. _test_main.py_: Run all steps in main.py and test if the output number is correct.
   
3. **Github actions setup for continuous integration**
  <br>e. _.github/workflows/cicd.yml_: Quality control actions are triggered when pushed/ pulled to main branch. After setting up the environment, actions of **installing packages**, **linting**, **testing**, **formatting** would be executed in order (specified in Makefile). 

4. **Other files for development environment settings**
  <br>f. _.devcontainer_: set up the environment for development.
  <br>g. _.gitignore_: specify file names to ignore.
  <br>h. _requirements.txt_: list required packages for the project.

5. **Description of the project**
   <br>i. _README.md_: THIS FILE, explaining the purpose and structure of the directory, with screenshot of example output.


