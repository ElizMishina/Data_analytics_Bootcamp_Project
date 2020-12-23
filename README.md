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

## Machine Learning Model (Draft) 

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