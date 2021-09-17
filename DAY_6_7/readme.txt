DAY 6_7
TASKS :



Model training and evaluation.


The dataset is of the weather condition of a particular place over some years, one hour at a time.

Our task is to predict the PM2.5 concentration on a test dataset.



Here are the tasks  that were  needed to completed:-

1. Train atleast two models to predict PM2.5 and decide a the final model from the trained models for prediction.


2. For each model print it's accuracy(out of 100 in %)(r2 is preferred), the errors(mean squared, mean absolute etc).

3. Tell us why did you select a particular model for final prediction with stats/proofs to support your answer.

4. After finalising the model predict PM2.5 concentration on test dataset that you had made in test_train_split and plot a graph of actual vs predicted to show comparison and how accurately the model is predicting.
-Actual data is the values of PM2.5 in the test dataset that you have made.
-Predicted data is the values predicted by your finalized model.

5. Explain the observation that you can make from the actual vs predicted graph.

6. Predict output on 10 different inputs and print them. These inputs are your inputs that you will give to the model after the model is fully trained and ready for deployment. The inputs values depends on you. You can take any input values.

7. Optimize your model as much as possible for better accuracy keeping in mind the case of underfitting and overfitting.


TASK 1:
       --> First we used Train_Test_Split to divide the dataset  into train and test data sets .
       --> Then we preprocessed the data using PowerTransformer().
       --> PowerTransformer was both used on features and labels.
       --> Then we created three models named: 
              
              1) ExtraTreeRegressor
              2) RandomTreeRegressor
              3) RandomTreeRegressor with RandomisedSearchCV
             
                
         **RandomisedSearchCV was used to tune the hyperparameters.
             
       
TASK 2:
       --> Then we printed the R2_score,MeanAbsoluteError and MeanSquaredError,then choosing the best one among the three.
       --> The best modle came out to be RandomTreeRegressor with RandomisedSearchCV
       
TASK 3:
       --> The main reason was the accuracy which we obtained from this model was the best as compared to other models.
           The reason why we obatined best accuracy was Randomized Search CV which gave us the hyper-parameters to tune 
           the classifier that is Random Tree Regressor.
TASK 4:
       --> We plotted two different scatter plots predicted vs actual data.
       
TASK 5
       --> We conclude that most of the predicted values are much less as compared to true values. This may be due the 
           fact that the model we used had a very low r2_score as the label "PM2.5" didnt correlate with the features.

TASK 6 
       --> We created  a random data set and predicted the values on that dataset using the model.
        
                           *********************************************END******************************************
       
