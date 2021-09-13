DAY 3 
TASK 1
Today's Task- Data Cleaning, find count of missing values in each column, describe the dataset (mean,median etc ).

--> At first we imported libraries pandas ,numpy, matplotlib and seaborn for handling and visualizing data.

--> Then we read our "train.csv" file (variable=df) on which cleaning was to be performed .

--> Then first we checked the the type of data we have to deal with the help of "info()" function.

--> We then checked the count of null values present in every column with the help of "isnull().sum()" function.

--> Then we made copy of our data(df1).
******************** DATA CLEANING BEGINS *********************

--> Now we started cleaning our features in order from "wind_speed" to "year".

--> For every feaature we again found the number of null values.

--> If the data was an object type , we converted it into numeric type with the help of "to_numeric()".

--> TThen we plotted our raw data with the help of distplot function from seaborn.

--> We then checked for anomalies in the specified feature.

--> Then we updated our data by removing those anomalies .

For example- Their were negative values in "wind_speed" , "pressure" and "year"
             Their were also anomalies in feature "hour" like values being greater than 23 which is not possible.
             

--> Now to handle null values we used "interpolate()" function from pandas.
    We used methods "linear" and "polynomial" with "order 5" .
    Interpolation is a type of estimation, a method of constructing (finding) new data points based on the range of a discrete set of known data points.
    Pandas dataframe.interpolate() function is basically used to fill NA values in the dataframe or series.
    It uses various interpolation technique to fill the missing values rather than hard-coding the value.

--> For the specific categorical feature "wind_direction" we filled its null values with "mode" of that feature. 
    
--> After cleaning and adding interpolated datapoints we again plotted the distplot with of new data with.
    KDE of data was also super imposed on the graph.
    A kernel density estimate (KDE) plot is a method for visualizing the distribution of observations in a dataset, analagous to a histogram.
    Rather than using discrete bins, a KDE plot smooths the observations with a Gaussian kernel, producing a continuous density estimate.

--> Now we again checked for null values if present,any. Which were not found.
    Which indicated that cleaning has been successfull. 

******************** DATA CLEANING DONE *********************


--> After cleaning we compared the original data(df) with our new cleaned data (df1).
    We compared their shape and null values.
    Count of null values came out to be O for each feature, which indicated that our data is cleaned.
  
******************** DATA DESCRIPTION *********************
   
   
--> Now we printed the description of our cleaned data through we mentioned mean,count,standar deviation,quartiles,max and min value 
    for that each feature with the help of describe() method.
   
******************** LABEL ENCODING *********************

--> Now to handle categorical feature that is "wind_direction" we took Label Encoder from sklearn.preprocessing library.

--> Label Encoding refers to converting the labels into a numeric form so as to convert them into the machine-readable form.
    Machine learning algorithms can then decide in a better way how those labels must be operated.
    It is an important pre-processing step for the structured dataset in supervised learning.

Now our cleaned data is stored in df3 variable.

df =Original data.
df1=Copy of original data to perform cleaning.
df3=Final Cleaned data.


    
