# House Price Prediction

## Deliverable 1

**Worked on:**  
Presentation: Everyone  
Github: Master branch origanization - Elizabeth, Branches - Everyone  
Machine Learning model: Savitha and Brandon  
Database: Elizabeth and Caleb  

**Topic:** Predict House prices in King County based on previous house sales data  

**Reason for selection:** This project gives an oppurtunity for us to implement both supervised learning (predict house prices) and unsupervised learning (group houses for vizualization)  

**Data Source:** House Sales Data for King County from Kaggle [Link to Data](https://www.kaggle.com/achyutanandaparida/dataset%20from%20%20house%20sales%20in%20king%20county,%20usa)  

**Questions Answered:**  

- Predict house prices  
- Group houses into diffrent cluster  
- Analyse what features impact the house price  

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

**Data Preprocessing:**

- Download dataset as csv from Kaggel
- Create tables in database(SQLlite) and upload data
- Read tables into Pandas using SQLAlchemy
- Perform data cleansing as needed

**Outline of machine learning model:**

- Use p-Value from multiple linear regressions to look at each independent variable to determine if there is a significant relationship with the dependent variable
- Predict price of home based on features listed above
- Create groups based on the features using clustering
- Use 3D plot to visualize the breakdown of features of each cluster and display what house price group they fall under (prediction)
- After evaluating each independent variable, use r-squared of the model to determine if the model was successful at predicting dependent variables
- Optimize the machine learning model to improve accuracy