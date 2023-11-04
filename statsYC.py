def calMean(df, clmn):
    ''' 
    The function takes the following 2 inputs:
    1. A pandas DataFrame 
    2. A column name
    and outputs the mean of the column.    
    '''
    if clmn not in df.columns:
        raise ValueError("ValueError. Input column not in input DataFrame.")
    try:
        return df[clmn].mean()
    except Exception as e:
        raise ValueError("ValueError. Check if input column is of datatype int or float.") from e
    

def calMedian(df, clmn):
    ''' 
    The function takes the following 2 inputs:
    1. A pandas DataFrame 
    2. A column name
    and outputs the median of the column.    
    '''    
    if clmn not in df.columns:
        raise ValueError("ValueError. Input column not in input DataFrame.")
    try:
        return df[clmn].median()
    except Exception as e:
        raise ValueError("ValueError. Check if input column is of datatype int or float.") from e

def calSD(df, clmn):
    ''' 
    The function takes the following 2 inputs:
    1. A pandas DataFrame 
    2. A column name
    and outputs the standard deviation of the column.    
    '''    
    if clmn not in df.columns:
        raise ValueError("ValueError. Input column not in input DataFrame.")
    try:
        return df[clmn].std()
    except Exception as e:
        raise ValueError("ValueError. Check if input column is of datatype int or float.") from e

def countItemOcc(df, clmn, item):
    ''' 
    The function takes the following 3 inputs:
    1. A pandas DataFrame 
    2. A column name
    3. An item (e.g. a string or a number)
    and outputs the number of occurrences of the item in the column.
    '''        
    if clmn not in df.columns:
        raise ValueError("ValueError. Input column not in input DataFrame.")
    return df[df[clmn]==item].shape[0]

def calItemRate(df, clmn, item):
    '''
    The function takes the following 3 inputs:
    1. A pandas DataFrame 
    2. A column name
    3. An item (e.g. a string or a number)
    and outputs the number of occurrences of the string over total number of non-None rows in the column.
    '''        
    if clmn not in df.columns:
        raise ValueError("ValueError. Input column not in input DataFrame.")
    return (df[df[clmn]==item].shape[0]*100)/(df.dropna(subset=[clmn]).shape[0])

def printNumStats(df, clmn):
    '''
    The function takes the following 2 inputs:
    1. A pandas DataFrame 
    2. A column name
    and it prints out the mean and median of the numerical column in the following format:
    "In InputColumn column, the mean is *MeanRoundedTo2Digits* and the median is *MedianRoundedTo2Digits*."
    '''    
    clmnMean = round(calMean(df, clmn), 2)
    clmnMedian = round(calMedian(df, clmn), 2)
    Clmn_s = "In {} column, ".format(clmn)
    Summary_s = 'the mean is {} and the median is {}.'.format(str(clmnMean),str(clmnMedian))
    return Clmn_s + Summary_s 
    
          
def printOccStats(df, clmn, item):
    '''
    The function takes the following 3 inputs:
    1. A pandas DataFrame 
    2. A column name
    3. An item (e.g. a string or a number)
    and it returns the following:
    "In InputColumn column, the number of occurrences of Item is CountItemOccurrence, or RateOfItemOccurrenceRoundedTo2Digits of total samples."          
    '''
    ItemOcc = countItemOcc(df, clmn, item)
    ItemOccPercent = calItemRate(df, clmn, item)
    Clmn_s = "In {} column, ".format(clmn)
    Summary_s = 'the number of occurrences of {} is {}, or {}% of total samples.'.format(item, ItemOcc,str(round(ItemOccPercent, 2)))
    return Clmn_s + Summary_s