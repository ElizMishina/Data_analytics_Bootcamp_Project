import pandas as pd
import numpy as np
from flask import Flask, request, render_template
import xgboost
import pickle

# Create Flask App
app = Flask(__name__)

# Load the scalar and regression model pickle files
scalar_pk = pickle.load(open("hp_scalar.pkl","rb"))
xgbmodel_pk = pickle.load(open("hp_xgbmodel.pkl","rb"))

# Loading housedata and average price data
df_housedata = pd.read_csv("formatted_housedata.csv")
average_price_df = pd.read_csv("average_price_df.csv")

# Create city list for dropdown
city_list = average_price_df["primary_city"].tolist()

# Homepage app route
@app.route("/")
def home():
    return render_template("index.html",city_list=city_list)

# Predict app route
@app.route("/predict", methods=['GET',"POST"])
def predict_api():
        # Get input from form
        sqft_living = request.form.get("sqft_living")
        grade = request.form.get("grade")
        sqft_above = request.form.get("sqft_above")
        bathrooms = request.form.get("bathrooms")
        city = request.form.get("city")
        view = request.form.get("view")
        sqft_basement = request.form.get("sqft_basement")
        bedrooms = request.form.get("bedrooms")

        # Get city rank
        city_rank = average_price_df.loc[average_price_df.primary_city == city, "city_rank"].values[0]

        # Filter data for current city
        predict_filter_df = df_housedata[df_housedata["city_rank"] == city_rank]

        # Create input dataframe for prediction
        pred_df = pd.DataFrame(columns=["sqft_living","grade","sqft_above","bathrooms","city_rank","view","sqft_basement","bedrooms"])
        pred_df["sqft_living"] = [sqft_living]
        pred_df["grade"] = grade
        pred_df["sqft_above"] = sqft_above
        pred_df["bathrooms"] = bathrooms
        pred_df["city_rank"] = city_rank
        pred_df["view"] = view
        pred_df["sqft_basement"] = sqft_basement
        pred_df["bedrooms"] = bedrooms

        # Fill in mean value for columns that have no data
        for column in pred_df:
            if pred_df.loc[0,column] == "":
                pred_df.loc[0,column] = predict_filter_df.groupby("city_rank")[column].mean().values[0]

        # Scale the prediction input dataset 
        pred_scaled = scalar_pk.transform(pred_df)
        
        # Predict house price using xgboost model
        prediction = xgbmodel_pk.predict(pred_scaled)
        prediction = np.exp(prediction)

        # Rename columns for display in HTML
        pred_details = pred_df.rename(columns={"sqft_living" : "SQFT Living",
                                           "sqft_basement" : "SQFT Basement",
                                           "sqft_above" : "SQFT Above",
                                           "bedrooms" :"Bedrooms",
                                           "bathrooms" : "Bathrooms",
                                           "grade" : "Grade",
                                           "view" : "View" })
        pred_details["City"] = city
        pred_details = pred_details[["City","SQFT Living","SQFT Above","SQFT Basement",
                                     "Bedrooms","Bathrooms","View","Grade"]]

        # Get Maximum Price Row and format for html display 
        max_details = predict_filter_df[predict_filter_df.price == predict_filter_df.price.max()]
        max_details['price'] = max_details['price'].astype('int64') 
        max_details = max_details.rename(columns={"sqft_living" : "SQFT Living",
                                           "sqft_basement" : "SQFT Basement",
                                           "sqft_above" : "SQFT Above",
                                           "bedrooms" :"Bedrooms",
                                           "bathrooms" : "Bathrooms",
                                           "grade" : "Grade",
                                           "view" : "View",
                                           "price" : "Price"})
        max_details["City"] = city
        max_details = max_details[["City","Price","SQFT Living","SQFT Above","SQFT Basement",
                                     "Bedrooms","Bathrooms","View","Grade"]]
        max_details = max_details.transpose()

        # Get Maximum Price Row and format for html display 
        min_details = predict_filter_df[predict_filter_df.price == predict_filter_df.price.min()]
        min_details['price'] = min_details['price'].astype('int64') 
        min_details = min_details.rename(columns={"sqft_living" : "SQFT Living",
                                           "sqft_basement" : "SQFT Basement",
                                           "sqft_above" : "SQFT Above",
                                           "bedrooms" :"Bedrooms",
                                           "bathrooms" : "Bathrooms",
                                           "grade" : "Grade",
                                           "view" : "View",
                                           "price" : "Price"})
        min_details["City"] = city
        min_details = min_details[["City","Price","SQFT Living","SQFT Above","SQFT Basement",
                                     "Bedrooms","Bathrooms","View","Grade"]]
        min_details = min_details.transpose()
       
        # Get Maximum Price Row and format for html display 
        predict_filter_df["Median_Price"] = predict_filter_df.price.median()
        predict_filter_df["Diff_From_Median"] = predict_filter_df['price'] - predict_filter_df["Median_Price"]
        predict_filter_df["Diff_From_Median"] = predict_filter_df["Diff_From_Median"].abs()
        median_details = predict_filter_df[predict_filter_df.Diff_From_Median == predict_filter_df.Diff_From_Median.min()]
        median_details['price'] = median_details['price'].astype('int64') 
        median_details = median_details.rename(columns={"sqft_living" : "SQFT Living",
                                           "sqft_basement" : "SQFT Basement",
                                           "sqft_above" : "SQFT Above",
                                           "bedrooms" :"Bedrooms",
                                           "bathrooms" : "Bathrooms",
                                           "grade" : "Grade",
                                           "view" : "View",
                                           "price" : "Price"})
        median_details["City"] = city
        median_details = median_details[["City","Price","SQFT Living","SQFT Above","SQFT Basement",
                                     "Bedrooms","Bathrooms","View","Grade"]]
        median_details = median_details.transpose()  

        # Create html table for diaplay
        pred_table = pred_details.to_html(classes='data', header="true", index=False, justify="left")
        max_table = max_details.to_html(classes='maxdata',header=False, justify="left")
        min_table = min_details.to_html(classes='maxdata', header=False,justify="left")
        median_table = median_details.to_html(classes='maxdata',header=False,justify="left")

        return render_template("predict.html", prediction=prediction[0],city_list=city_list,tables=[pred_table],
                                maxtable=[max_table],mintable=[min_table],mediantable=[median_table])

if __name__ == '__main__':
    app.run()
