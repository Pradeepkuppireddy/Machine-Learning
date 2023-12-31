from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('Linear_regression_model_new.pkl', 'rb'))


@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


#standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        area = int(request.form['area'])
        bedrooms = int(request.form['bedrooms'])
        age=int(request.form['age'])
        
        prediction=model.predict([[area,bedrooms,age]])
        output=prediction[0]
        if output<0:
            return render_template('index.html',prediction_texts="Sorry No result")
        else:
            return render_template('index.html',prediction_text="Please find the resut {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
