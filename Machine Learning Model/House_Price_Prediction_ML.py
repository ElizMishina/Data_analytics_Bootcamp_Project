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

        # Create html table for diaplay
        pred_table = pred_df.to_html(classes='data', header="true", index=False, justify="left", col_space=100)
        return render_template("predict.html", prediction=prediction[0],city_list=city_list,tables=[pred_table])

if __name__ == '__main__':
    app.run()
