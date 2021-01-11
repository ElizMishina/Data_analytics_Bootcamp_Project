# Segment 1

**Problem Statement (Topic):** Predicting King County, USA housing prices using specific features

**Reason Why We Selected Topic:** Interesting way to apply machine learning models (supervised/unsupervised) to real world data in order to predict house prices

**Questions Answered:**

    * Can we predict the price of a home in King County, USA based on features such as square footage, # of rooms, zipcode, etc.
    * How accurately can we predict the price of a home 
    * To what extent does each feature impact the price of a home

**Dataset Source:** 

[Link to Dataset 1](https://www.kaggle.com/achyutanandaparida/dataset%20from%20%20house%20sales%20in%20king%20county,%20usa)  
[Link to Dataset 2](https://www.unitedstateszipcodes.org/wa/)  

**Preprocessing Data (Database):**
Elizabeth Mishina & Caleb TenHuisen

    * Download dataset as csv
    * Create tables in database with CSV (SQL)
    * Read tables into Pandas using SQLAlchemy/SQLlite
    * Clean up data if needed

**Machine Learning Model (Outline):**
Brandon DeLuna & Savitha Sathyanathan
    
    Target: House Price

    Features:

        * # of bedrooms
        * # of bathrooms
        * # of square foot living
        * # of square foot lot
        * # of floors
        * water front
        * view

    Model (Linear Regression/Random Forest Regressor/Clustering):

        * Predict price of home based on features such as # of bedrooms, # of bathrooms, square footage, etc.
        * Use p-value from multiple linear regressions to look at each independent variable to determine if there is a significant relationship with the dependent variable 
        * Select features for model based on the level of significance of the relationship to the dependent variable
        * Create clusters for the price of homes with the selected features
        * Use 3D plot to visualize the breakdown of features of each cluster and display what house price group they fall under (prediction)
        * After evaluating each independent variable, use r-squared of the model to determine if the model was successful at predicting dependent variable.
        * Optimize the machine learning model in order to improve accuracy


# Segment 2

## Machine Learning Model (Draft): Brandon DeLuna & Savitha Sathyanathan 

This is the draft model of our machine learning model. All data used is preliminary.

Description of preliminary data prepocessing:

    * Read in datasets 1 & 2 into jupyter notebook
    * Checked for columns, missing data, and unique values in each dataset
    * Merged the 2 datasets using the common "zipcode" column
    * Checked for columns, missing data, and unique values in joined dataset
    * Dropped columns in joined dataset that were deemed unnecessary for machine learning model

Machine Learning Model (Draft):

Overview: We used Linear Regression & Random Forest Regressor as our models in order to measure how effectively we could predict the price of a house based on selected features. The model is preliminary and has not been refined to create an accurate test yet. This segment was used as a test run to see if our model could take in our inputs and create an output. 

We used Linear Regression in order to measure the significance of the relationships between the independent variables and dependent variable
We used Random Forest Regressor because of the fact that the model uses averaging in order to improve predictive accuracy and control over-fitting

See process below:

    * Calculated the correlation coefficient of independent variables using Pearsons Correlation Coefficient
    * Selected features for model with a coefficient greater than 0.5. Correlations above 0.5 are considered to have a high level of correlation
    * Created dataframe with only selected features
    * Created variables for independant features and dependent feature
    * Split the training/testing sets. I decided to have the training set test a random selection of 80% of the original data and the test set would have the remaining 20%
    * Transformed y_train set into log in order to normalize distribution of data
    * Scaled and transformed X_train & X_test
    * Created Linear regression instance, trained and fit the testing sets, printed coefficients, mean squared error, and r-squared value
    * Created Random Forest Regressor model, trained and fit the testing sets, printed mean squared error, and r-squared value

Limitiations to the models inlcude the following:

    * Limited data on some of the selected features 
    * Correlation coefficients not accurately representing the true correlation of independent variables to dependent variable


# Segment 3

## Machine Learning Model (Final): Brandon DeLuna & Savitha Sathyanathan 

This is the final version and working model of our machine learning algorithm we will be using in our project.

Data Preprocessing:

    * Create a connection with the database file through sqlite3
    * Read in the SQL query and create a dataframe
    * Check for columns & datatypes
    * Dropped unneccessary columns
    * Check the number of unique values in each columns to see if we needed to use binning, none was needed
    * Check for missing data in each column
    * Converted "date" string to show only the year
    * Converted dataype of all columns with dates to integers
    * Created a ranking system for "primary city" based on the average house price for each city and merged it into existing datframe
    * Filtered out data points with price > 4,000,000.00 to remove outliers

Feature Engineering & Feature Selection:

    * Once our database was created with our working data we used the Pearsons Correlation Coefficient in order to find the best features to use for our machine learning model
    * We chose features with a Pearson Coefficient of 0.5 and above because having a coefficient of 0.5 or more shows a strong correlation to the dependent variable

Machine Learning:

    * Began by setting the selected pearson features as our independent variables
    * Set dependent variable as price
    * Split the data into training/testing sets
    * Transformed y_train dataset to log in order to normalize the data
    * Scaled our X_train and X_test datasets in order to arrange our data into a standard normal distribution

    * We tested our data with the 3 models below:
        * Created a Linear Regression model with sklearn
            - Linear approach to modelling the relationship between the independent and dependent variables
        * Created a Random Forest Regressor model with sklearn
            - Meta estimator that fits a number of classifying decision trees on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting
        * Created a XGBoost regressor model
            - Decision tree based ensemble machine learning algorithm that uses gradient boosting framework
    
    * The below are the metrics we used to measure the accuracy of our models:
        * Root Mean Squared Error (RMSE)
            - Measures the amount of predictions errors there are, value closer to 0 are better
        * Mean Squared Error (MSE)
            - Measures the quality of the estimator, values closer to 0 are better
        * Coefficient of Determination (R^2)
            - Measures how accurate the prediction is, an R^2 value of 1 would represent a perfect prediction
    
    * The below is the conlusion of our testing: 
        * The XGBoost regressor model yielded the highest accuracy scores. 
            - RMSE: 88,225.33
            - MSE: 21,978,220,607.50
            - R^2: 0.82
        * Of all 3 metrics we used to measure accuracy XGBoost had the lowest RMSE, MSE. and R^2 scores.
        * The XGBoost model was the model we decided to use for our machine learning project
    
    * After testing we used unsupervised learning to visualize our data with clusters
        - Goal was to segment features into clusters based upon price in order to show correlation of features with associated price range
        - Initialized the K-Means model in order to group data into 5 clusters 
        - Created a datafame with predicted clusters, labeled the clusters, and filtered out outliers
        - Created a 3D scatter plot using plotly express


Observations:

    * The machine learning model we used for testing in segment 2 changed in segment 3. Initially we only used Linear Regression and Random Forest Regressor. However, after further research of models we could use we came across the XGBoost model which ended up yielding higher accuracy scores and proved to be the better performing model.

# Segment 4

Presentation - data preprocessing, machine learning model, xgboost model
    