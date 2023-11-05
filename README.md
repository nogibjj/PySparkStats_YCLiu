[![Python application test with Github Actions](https://github.com/nogibjj/PandasStats_YCLiu/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/PandasStats_YCLiu/actions/workflows/main.yml)

## Use PySpark To Transform and Query Data

This repository demonstrates using **PySpark to transform and query large dataset**. PySpark is the API for Apache Spark. Thanks to the idea of the reselient distributed dataset(RDD), Spark can be used for to manipulate data efficiently on larger dataset because it can distribute work on multiple (cores) of machines. The **dataset used** for demonstration is the **transaction records of an E-Commerce company in UK**, downloaded from [kaggle](https://www.kaggle.com/datasets/gabrielramos87/an-online-shop-business).

Below is an overview of the repository:
   
1. **Main functions for querying on Dataset**
   <br>a. _main.py_: execute command-line-like functions from ./mylib to create a database, tables, and to query on the created database. Specifically, it does the following:
   <br>         1. **Read** dataset.
   <br>d. _test_main.py_: Run all steps in main.py and test if the output query is correct.
   
2. **Github actions setup for continuous integration**
  <br>e. _.github/workflows/cicd.yml_: Quality control actions are triggered when pushed/ pulled to main branch. After setting up the environment, actions of **installing packages**, **linting**, **testing**, **formatting** would be executed in order (specified in Makefile). 

3. **Other files for development environment settings**
  <br>f. _.devcontainer_: set up the environment for development.
  <br>g. _.gitignore_: specify file names to ignore.
  <br>h. _requirements.txt_: list required packages for the project.

4. **Description of the project**
   <br>i. _README.md_: THIS FILE, explaining the purpose and structure of the directory, with screenshot of example output.


