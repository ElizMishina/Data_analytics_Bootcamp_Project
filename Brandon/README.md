**Deliverable 1**

**Problem Statement: Predicting California housing prices using specific features**

**Dataset Source:** 
[Link to Data](https://www.kaggle.com/achyutanandaparida/dataset%20from%20%20house%20sales%20in%20king%20county,%20usa)  
[Link to Data](https://www.unitedstateszipcodes.org/wa/)  

**Preprocessing Data (Database):**

    * Download dataset as csv
    * Create tables in database with CSV (SQL)
    * Read tables into Pandas using SQLAlchemy/SQLlite
    * Clean up data if needed

**Machine Learning Model (Outline):**

    Target: House Price

    Features:

        * # of bedrooms
        * # of bathrooms
        * # of square foot living
        * # of square foot lot
        * # of floors
        * water front
        * view

    Model:

        * Predict price of home based on features such as # of bedrooms, # of bathrooms, square footage, etc.
        * Create groups based on price of house and cluster features that are related to datapoints within each price range
        * Use 3D plot to visualize the breakdown of features of each cluster and display what house price group they fall under (prediction)
        * Use p-value from multiple linear regressions to look at each independent variable to determine if there is a significant relationship with the dependent variable 
        * After evaluating each independent variable, use r-squared of the model to determine if the model was successful at predicting dependent variable.


