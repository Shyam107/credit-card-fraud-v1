import pickle
import pandas as pd

from flask import Flask, request, render_template, redirect, url_for

pipe2 = pickle.load(open("random.pkl", "rb"))

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        category = request.form["category"]
        amount = float(request.form["amount"])
        state = request.form["state"]
        zip = float(request.form["amount"])
        latitude = float(request.form["latitude"])
        longitude = float(request.form["longitude"])
        population = float(request.form["population"])
        mlatitude = float(request.form["mlatitude"])
        mlongitude = float(request.form["mlongitude"])
        age = float(request.form["age"])
        hour = float(request.form["hour"])
        day = float(request.form["day"])
        month = float(request.form["month"])

        input_df = pd.DataFrame(
            {
                "category": [category],
                "state": [state],
                "amt": [amount],
                "zip": [zip],
                "lat": [latitude],
                "long": [longitude],
                "city_pop": [population],
                "merch_lat": [mlatitude],
                "merch_long": [mlongitude],
                "age": [age],
                "hour": [hour],
                "day": [day],
                "month": [month],
            }
        )
        result = pipe2.predict(input_df)
        r = ""
        if result == 0 or result <= 0.5:
            r = "Transaction is not a fraud Transaction !"
        else:
            r = "Transaction is a fraud Transaction !"
        return render_template("result.html", labels=r)
        # number2_value = request.form.get("number2")

        # input_df = pd.DataFrame(
        #     {
        #         "category": [Cat],
        #         "state": [state],
        #         "amt": [amt],
        #         "zip": [zip],
        #         "lat": [lat],
        #         "long": [long],
        #         "city_pop": [city_pop],
        #         "merch_lat": [merch_lat],
        #         "merch_long": [merch_long],
        #         "age": [age],
        #         "hour": [hour],
        #         "day": [day],
        #         "month": [month],
        #     }
        # )
        # result = pipe2.predict(input_df)
        # if result == 0 or result <= 0.5:
        #     st.text("Transaction is not a fraud Transaction !")
        # else:
        #     st.text("Transaction is a fraud Transaction !")
