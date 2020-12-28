# House Price Prediction

[Master Readme Link](https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/tree/main)

## Deliverable 2

**Worked on:**  
Presentation: Everyone  
Github: Master branch origanization - Elizabeth, Branches - Everyone  
Machine Learning model: Savitha and Brandon  
Database: Caleb  
Dashboard: Elizabeth  

**Data Exploration:**  
Two datasets were used as a part of this project. Both the files were 

**Data Analysis:**  


### Machine Learning Model: 

**Data Preprocessing:**  

**Feature Selection:**  

**Model Selection:**



## Deliverable 1

**Worked on:**  
Presentation: Everyone  
Github: Master branch origanization - Elizabeth, Branches - Everyone  
Machine Learning model: Savitha and Brandon  
Database: Elizabeth and Caleb  

**Topic:** Predict House prices in King County based on previous house sales data  

**Reason for selection:** This project gives an oppurtunity for us to implement both supervised learning (predict house prices) and unsupervised learning (group houses for vizualization)  

**Data Source:**  

- House Sales Data for King County from Kaggle [Link to Data](https://www.kaggle.com/achyutanandaparida/dataset%20from%20%20house%20sales%20in%20king%20county,%20usa)  
- Population and City info by Zipcode from unitedstateszipcodes.org [Link to Data](https://www.unitedstateszipcodes.org/wa/#zips-list)

**Questions Answered:**  

- Predict house prices  
- Group houses into diffrent cluster  
- Analyze what features impact the house price  
- Analyze house prices by city/zipcode

**Machine Learning model:**  

- Predict House prices using Random Forest Classifier  
- Group houses into clusters using clustering  

**Features:**

- bedrooms
- bathrooms
- sqft_living
- sqft_lot
- floors
- waterfront
- view
- condition
- grade
- yr_built
- yr_renovated
- population

**Data Preprocessing:**

- Download house sales dataset as csv from Kaggel
- Download population and city details dataset as csv from unitedstateszipcodes.org
- Create tables in database(SQLlite) and upload data
- Read tables into Pandas using SQLAlchemy
- Perform data cleansing as needed

**Outline of machine learning model:**

- Use p-Value from multiple linear regressions to look at each independent variable to determine if there is a significant relationship with the dependent variable
- Select features that have significant relationship to the dependent variable
- Predict price of home based on selected features
- Create clusters based on the selected features using clustering
- Use plots to visualize the breakdown of features of each cluster and display what house price group they fall under (prediction)
- After evaluating each independent variable, use r-squared of the model to determine if the model was successful at predicting dependent variables
- Optimize the machine learning model to improve accuracy

**Database:**
[Caleb's Readme](https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/tree/Caleb)