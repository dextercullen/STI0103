#!/usr/bin/env python
# coding: utf-8


from flask import Flask
from flask import request, render_template
import joblib


app = Flask(__name__)


@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        Nikkei = request.form.get("Nikkei")
        print(Nikkei)
        model1 = joblib.load("STI_REG")
        pred1 = model1.predict([[Nikkei]])
        str1 = "The prediction for STI usng Regression is :"+ str(pred1)
        
        return (render_template("index.html",result = str1))
    else:
        return(render_template("index.html", result = "2"))


if __name__=="__main__":
    app.run()


