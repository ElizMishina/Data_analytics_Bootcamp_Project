<<<<<<< HEAD
## Segement 2
### Presentation
* Everyone
* [Elizabeth](https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/blob/EMishina/README.md) putting together the presentation
* [Presentation](https://docs.google.com/presentation/d/1tu8kpEW_eMj6sY7mHG4yKu1wUKrHQQwbZeIkFiv13WE/edit?usp=sharing)

### GitHub
* [Elizabeth's ReadMe](https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/blob/EMishina/README.md)

### Machine Learning Model
* [Brandon's ReadMe](https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/blob/Brandon/Brandon/README.md)
* [Savitha's ReadMe](https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/blob/ssathya/README.md)
=======
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
>>>>>>> ssathya

**Model Predictions**  

<<<<<<< HEAD
### Database
* [Caleb's ReadMe](https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/blob/Caleb/README.md)
=======
* The values required for house price prediction are captured from the user (Hardcoded for now. Have to integrate with the webpage)
* The city_rank is calculated based on the primary city
* A dataframe is created with the available values for features entered and null values for features that were not entered
* The housedata is filtered for the city that the user entered
* A for loop was created to loop through columns that do not have values and the mean value based on the filtered dataset is populated for these columns
* The predicted dataframe is scaled using previous scalar model
* The house price is then predicted using the previously trained model
>>>>>>> ssathya

## Deliverable 1

**Worked on:**  
Presentation: Everyone  
Github: Master branch origanization - Elizabeth, Branches - Everyone  
Machine Learning model: Savitha and Brandon  
Database: Elizabeth and Caleb  

<<<<<<< HEAD
### Dashboard
* [Elizabeth's ReadMe](https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/blob/EMishina/README.md)
* [Storyboard](https://docs.google.com/presentation/d/1zPjLQjZFv1hgx527TvCYcwXP_tY3SkvMWfn8anygJrc/edit?usp=sharing)
=======
**Topic:** Predict House prices in King County based on previous house sales data  
>>>>>>> ssathya

**Reason for selection:** This project gives an oppurtunity for us to implement both supervised learning (predict house prices) and unsupervised learning (group houses for vizualization)  

<<<<<<< HEAD
## Segement 3
### Presentation
[Presentation Slides](https://docs.google.com/presentation/d/1tu8kpEW_eMj6sY7mHG4yKu1wUKrHQQwbZeIkFiv13WE/edit?usp=sharing)
* Orginised by [Elizabeth](https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/blob/EMishina/README.md)
* Information added by everyone

### GitHub
* Orginized by [Elizabeth](https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/blob/EMishina/README.md)

### Machine Learning Model
* [Brandon's ReadMe](https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/blob/Brandon/Brandon/README.md)
* [Savitha's ReadMe](https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/blob/ssathya/README.md)

### Database
N/A

### Dashboard
[Story Board](https://docs.google.com/presentation/d/1zPjLQjZFv1hgx527TvCYcwXP_tY3SkvMWfn8anygJrc/edit?usp=sharing)
[Savitha](https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/blob/ssathya/README.md) started the base code
[Elizabeth](https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/blob/EMishina/README.md) and [Caleb](https://github.com/ElizMishina/Data_analytics_Bootcamp_Project/blob/Caleb/README.md) put it together

## Segement 4
=======
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
>>>>>>> ssathya
