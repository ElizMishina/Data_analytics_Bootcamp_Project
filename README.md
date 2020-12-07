# Data_Analytics_Bootcamp_Project
**Deliverable 1**

**Problem Statement (Topic):** Predict the value of a King County, USA home based on key attributes such as # of bedrooms, bathrooms, house size, lot size, etc.

**Reason Why We Selected Topic:** Creating a tool that can accurately predict a properties value based on real data could be useful outside of class whenever we decide to buy our own home.

**Questions Answered:**

    * Can we predict the price of a home in King County, USA based on features such as square footage, # of rooms, zipcode, etc.?
    * How accurately can we predict the price of a home?
    * To what extent does each feature impact the price of a home?

**Dataset Source:** 
[Link to Data](https://www.kaggle.com/achyutanandaparida/dataset%20from%20%20house%20sales%20in%20king%20county,%20usa)  
[Link to Data](https://www.unitedstateszipcodes.org/wa/)  

**Preprocessing Data (Database):**
**Portion of Deliverable 1 I am responsible for**

    
    * Download dataset as csv
    
<a target="_blank" rel="noopener noreferrer" href="https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/blob/Caleb/Photos/Screen%20Shot%202020-12-06%20at%206.11.42%20PM.png"><img src="https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/blob/Caleb/Photos/Screen%20Shot%202020-12-06%20at%206.11.42%20PM.png" alt="" style="max-width:100%;"></a>

<a target="_blank" rel="noopener noreferrer" href="https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/blob/Caleb/Photos/Screen%20Shot%202020-12-06%20at%206.12.20%20PM.png"><img src="https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/blob/Caleb/Photos/Screen%20Shot%202020-12-06%20at%206.12.20%20PM.png" alt="" style="max-width:100%;"></a>

    * Create Entity Relationship Diagram to show how the dataset sources are related
<a target="_blank" rel="noopener noreferrer" href="https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/blob/Caleb/Photos/Screen%20Shot%202020-12-06%20at%206.10.07%20PM.png"><img src="https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/blob/Caleb/Photos/Screen%20Shot%202020-12-06%20at%206.10.07%20PM.png" alt="" style="max-width:100%;"></a>

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

    Model:

        * Predict price of home based on features such as # of bedrooms, # of bathrooms, square footage, etc.
        * Create groups based on price of house and cluster features that are related to datapoints within each price range
        * Use 3D plot to visualize the breakdown of features of each cluster and display what house price group they fall under (prediction)
        * Use p-value from multiple linear regressions to look at each independent variable to determine if there is a significant relationship with the dependent variable 
        * After evaluating each independent variable, use r-squared of the model to determine if the model was successful at predicting dependent variable.
