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
Two datasets were used as a part of this project. Both the files were reviewed to determine the number of rows, the columns available and the data type for the column.

**Data Analysis:**  
The dataset was analysed in detail during the data preprocessing step. Initial analysis includes determining the data types, null values in the dataset, duplicate entries, looking at unique values to create bins.

### Machine Learning Model:  

[Link to Machine Learning Model](https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/blob/ssathya/Machine%20Learning%20Model/House_Price_Prediction_ML.ipynb)

**Data Preprocessing:**  
The steps for data preprocessing are listed below

* Drop any null rows
* Drop any rows that do not have price
* Format the date column to extract the sold year
* Calculate the sold age and renovated age column for prediction (since encoding the year column might not yield required results, the age is calculated for prediction)
* Merged dataset to get primary city for each zipcode (Will be performed using SQL Alchemy after database integration)
* Drop columns that are not needed (id,lat,long,sqft_living15,sqft_lot15,date,yr_built,yr_renovated,zipcode)
* The primary city column was encoded using custom encoding (rank based on average price)

**Feature Selection:**  
Feature selection was performed using two different methods

* Pearsons Correlation Coefficient was used to determine the correlation between the price and other columns
* Select Kbest score was used to determine the significance of each column to the price
* The results were plotted as a bar graph and the results were similar
* Features with correlation greater that 0.3 were selected for prediction

**Model Selection:**  

* X dataset was created using the features selected in the feature selection process
* Y dataset was created using the price column
* The dataset was split into test and train datasets using train_test_split from sklearn
* The test and trained datasets were then scaled using StandardScaler from sklearn
* Three models listed below were trained and tested and the root mean square value was calculated
    - Randon Forest Regression
    - XG Boost Regression
    - Linear Regression
* The predicted values were plotted against actuals
* Based on the results, the linear regression model had the best results

**Model Predictions**  

* The values required for house price prediction are captured from the user (Hardcoded for now. Have to integrate with the webpage)
* The city_rank is calculated based on the primary city
* A dataframe is created with the available values for features entered and null values for features that were not entered
* The housedata is filtered for the city that the user entered
* A for loop was created to loop through columns that do not have values and the mean value based on the filtered dataset is populated for these columns
* The predicted dataframe is scaled using previous scalar model
* The house price is then predicted using the previously trained model

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