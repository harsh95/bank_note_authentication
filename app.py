from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

pickle_in = open('model.pkl', 'rb')
model = pickle.load(pickle_in)

@app.route('/')

def welcome():
    return "Welcome All"

@app.route('/predict', methods=["GET"])
def predict_note_authentication():
    """Bank Note Authentication with perameters
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
      200:
        description: Is bank note GENUINE or COUNTERFEIT
    """
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = model.predict([[variance, skewness, curtosis, entropy]])
    if prediction == [0]:
        return "The note is COUNTERFEIT"
    else:
        return "The note is GENUINE"
    
@app.route('/predict_file', methods = ["POST"])
def predict_note_file():
    """Bank Note Authentication with CSV file inout
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
    responses:
      200:
        description: O for COUNTERFEIT note & 1 for GENUINE note
    """
    df_test = pd.read_csv(request.files.get("file"))
    prediction = model.predict(df_test)
    return "The predicted values for the csv is " + str(list(prediction))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
