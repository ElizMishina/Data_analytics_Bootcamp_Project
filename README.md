# House Price Prediction

[Master Readme Link](https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/tree/main)

## Deliverable 4

Presentation: Everyone  
Github: Master branch origanization - Elizabeth, Branches - Everyone  
Machine Learning model: Savitha and Brandon  
Database: Caleb  
Dashboard: Savitha and Elizabeth 

**Result of Analysis:**
The App is able to predict the house price based on the values entered by the user with 83% accuracy  
The features that impact the house price are given below (ranked from 1)  

- Sqft Living
- Grade (of the house 1(low) to 13(high))
- Sqft Above
- Bathrooms
- City Rank (based on the average price of city)
- View (from property 1 (low) to 4(high))
- Sqft Basement
- Bedrooms
- Waterfront (Is the property waterfront or not)
- floors
- Renovated Age (Sold year - Revonated year)
- Sqft Lot
- Sold Age (Sold Year - Built Year)
- Condition (of the house 1 - 4)

**Recommendations and Areas of Improvement:**

- Prediction Accuracy of the machine learning model can be improved by exploring different models
- Handling of the form entries when no data is provided by the user can be improved
- Refactor code using functions for performance
- Improve HTML view by adding addition charts and information

**Slides**  
[Google Slides](https://docs.google.com/presentation/d/1tu8kpEW_eMj6sY7mHG4yKu1wUKrHQQwbZeIkFiv13WE/edit?usp=sharing)

**Dashboard**  
[Heroku App](https://house-price-prediction-2020.herokuapp.com/)

**Database**  
[Caleb's Readme](https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/tree/Caleb)

## Deliverable 3

**Worked on:**  
Presentation: Everyone  
Github: Master branch origanization - Elizabeth, Branches - Everyone  
Machine Learning model: Savitha and Brandon  
Database: Caleb  
Dashboard: Savitha and Elizabeth  

**Technologies, languages, tools:**  

- Python: Pandas, Numpy, SKlearn, XGBoost, Pickle, Matplotlib, SQLlite3, SQLalchemy, Flask  
- SQLLite Database  
- HTML, CSS  
- Machine Learning Algorithm: Random Forest, XGBoost, Random Forest, Kmean Clustering  

**Model Choice**  
There was no change to model selection between segment 2 and segment 3. The details are in the Deliverable 2 section of readme (below)

**Model Training**  

- The processed data was split into test and train dataset using the "train_test_split" module from sklearn  
- The X test and train datasets were then standardised using "Standard Scalar"  
- The standardised dataset was then used to train the model and then the test data was used to test the accracy of the model

**Accuracy Score**  

- Since the Machine learning model used is a regression model, the Root Mean Squared and R Squared values were used to test the accuracy of the model
- The R Squared value for the model are listed below
    - XGBoost: 0.77
    - Random Forest Regressor: 0.75
    - Linear Regressor: 0.69

**Dashboard**

- HTML Webpage was used to create the house price prediction [Link to HTML Templates](https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/tree/ssathya/Machine%20Learning%20Model/templates)
- The trained model was downloaded as a pickle file for future use
- A flask app was created to render html template and get input from the user [Link to Flask App](https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/blob/ssathya/Machine%20Learning%20Model/app.py)
- The webpage contains
    - A chart that plots correlation between the features and house price 
    - A interactive chart that shows the house clusters based on the features (Output of Kmeans)
    - A form to get input from user for the house features.
    - The house price will then be predicted based on the trained model and the the results will be displayed to the user.

## Deliverable 2  

**Worked on:**  
Presentation: Everyone  
Github: Master branch origanization - Elizabeth, Branches - Everyone  
Machine Learning model: Savitha and Brandon  
Database: Caleb  
Dashboard: Savitha and Elizabeth 

* Pearsons Correlation Coefficient was used to determine the correlation between the price and other columns
* Select Kbest score was used to determine the significance of each column to the price
* The results were plotted as a bar graph and the results were similar
* Features with correlation greater that 0.3 were selected for prediction

**Model Selection:**  

* X dataset was created using the features selected in the feature selection process
* Y dataset was created using the price column
* The dataset was split into test and train datasets using train_test_split from sklearn
* The test and trained datasets were then scaled using StandardScaler from sklearn
* Three models listed below were trained and tested and the root mean square and R Squared value was calculated
    - Randon Forest Regression
    - XG Boost Regression
    - Linear Regression
* The predicted values were plotted against actuals
* Based on the results, the XGBoost model had the best results for Root mean squared and R Squared values and was choosen 
* XGBoost predicts the model the results more accurately compared to other models
* XGBoost  is more likely to overfit compared to Randomforest or Linear Regression

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
