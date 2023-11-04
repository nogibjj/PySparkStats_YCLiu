[![Python application test with Github Actions](https://github.com/nogibjj/PandasStats_YCLiu/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/PandasStats_YCLiu/actions/workflows/main.yml)

## A simple library that generates descriptive stats on Using pandas DataFrame.

The statsYC tool contains the following functions to generate stats from pandas DataFrame:

1. **calMean**: returns the **mean** of a numeric column.
  <br> The function takes the following 2 inputs:
  <br> 1. A pandas DataFrame 
  <br> 2. A column name
  <br> and outputs the **mean** of the column.
  <br> If the input **column** is **not in the DataFrame** or the datatype of the column is **not numerical**, the function **raise errors**.

2. **calMedian**: returns the **median** of a numeric column.
  <br> The function takes the following 2 inputs:
  <br> 1. A pandas DataFrame 
  <br> 2. A column name
  <br> and outputs the **median** of the column.
  <br> If the input **column** is **not in the DataFrame** or the datatype of the column is **not numerical**, the function **raise errors**.

3. **calSD**: returns the **standard deviation** of a numeric column.
  <br> The function takes the following 2 inputs:
  <br> 1. A pandas DataFrame 
  <br> 2. A column name
  <br> and outputs the **standard deviation** of the column.
  <br> If the input **column** is **not in the DataFrame** or the datatype of the column is **not numerical**, the function **raise errors**.

4. **countItemOcc**: returns the **count of occurrences** of the input item in the input column.
  <br> The function takes the following 3 inputs:
  <br> 1. A pandas DataFrame 
  <br> 2. A column name
  <br> 3. An item (e.g. a string or a number)
  <br> and outputs the **number of occurrences of the item** in the column.
  <br> If the input column is **not in the DataFrame**, the function **raise errors**.

5. **calItemRate**: returns the **count of occurrences over count of all non-NA rows** of the input item in the input column.
  <br> The function takes the following 3 inputs:
  <br> 1. A pandas DataFrame 
  <br> 2. A column name
  <br> 3. An item (e.g. a string or a number)
  <br> and outputs the **number of occurrences of the string over total number of non-None rows** in the column.
  <br> If the input column is **not in the DataFrame**, the function **raise errors**.

6. **printNumStats**: a simple visualization tool to print the **mean and median** of a column in a clear format.
  <br> The function takes the following 2 inputs:
  <br> 1. A pandas DataFrame 
  <br> 2. A column name
  <br> and it **returns the mean and median** of the numerical column in the following format (string):
  <br> In *Input* column, the mean is *MeanRoundedTo2Digits* and the median is *MedianRoundedTo2Digits*.          

7. **printOccStats**: a simple visualization tool to **print the count and rate of occurrence of an item** of a column in a clear format.
  <br> The function takes the following 3 inputs:
  <br> 1. A pandas DataFrame 
  <br> 2. A column name
  <br> 3. An item (e.g. a string or a number)
  <br> and it **returns the count and rate of occurrences of an item** of the input item in the input column in the following format (string):
  <br> In *Input* column, the number of occurrences is *CountItemOccurrence*, or *RateOfItemOccurrenceRoundedTo2Digits* of total samples.        

The **outputStats** script applies the **statsYC tool** to generate example summaries to a PDF file (which is **SummaryReport.pdf** in this repository).

<br><br>All functions were **linted**, **tested**, and **formatted** when pushed to the repository and passed all the steps.
