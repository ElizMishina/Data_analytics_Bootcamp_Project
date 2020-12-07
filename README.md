# Deliverable 1

## Problem Statement (Topic):## Predicting King County, USA housing prices using specific features

**Reason Why We Selected Topic:** Interesting way to apply machine learning models (supervised/unsupervised) to real world data in order to predict house prices

**Questions Answered:**

    * Can we predict the price of a home in King County, USA based on features such as square footage, # of rooms, zipcode, etc.
    * How accurately can we predict the price of a home 
    * To what extent does each feature impact the price of a home

**Dataset Source:** 

[Link to Dataset 1](https://www.kaggle.com/achyutanandaparida/dataset%20from%20%20house%20sales%20in%20king%20county,%20usa)  
[Link to Dataset 2](https://www.unitedstateszipcodes.org/wa/)  

**Preprocessing Data (Database):**
**Elizabeth Mishina & Caleb TenHuisen**

    * Download dataset as csv
    * Create tables in database with CSV (SQL)
    * Read tables into Pandas using SQLAlchemy/SQLlite
    * Clean up data if needed

**Machine Learning Model (Outline):**
**Brandon DeLuna & Savitha Sathyanathan**
    
    Target: House Price

    Features:

        * # of bedrooms
        * # of bathrooms
        * # of square foot living
        * # of square foot lot
        * # of floors
        * water front
        * view

    Model (Random Forest Classifier/Clustering):

        * Predict price of home based on features such as # of bedrooms, # of bathrooms, square footage, etc.
        * Use p-value from multiple linear regressions to look at each independent variable to determine if there is a significant relationship with the dependent variable 
        * Select features for model based on the level of significance of the relationship to the dependent variable
        * Create clusters for the price of homes with the selected features
        * Use 3D plot to visualize the breakdown of features of each cluster and display what house price group they fall under (prediction)
        * After evaluating each independent variable, use r-squared of the model to determine if the model was successful at predicting dependent variable.
        * Optimize the machine learning model in order to improve accuracy


