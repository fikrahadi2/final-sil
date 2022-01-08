from flask import Flask,request
from flask_cors import CORS
import pandas as pd
import joblib

loaded_model = joblib.load('final_model.sav')

app = Flask(__name__)
CORS(app)

def predict(val):
    loaded_model = joblib.load('final_model.sav')
    dp=[]
    dp.append(int(val.get('age')))
    dp.append(int(val.get('sex')))
    dp.append(float(val.get('bmi')))
    dp.append(int(val.get('children')))
    dp.append(int(val.get('smoker')))
    dp.append(int(val.get('region')))
    df_p = pd.DataFrame([dp])
    return loaded_model.predict(df_p[:1])

@app.route('/postAPI',methods = ['POST'])
def postAPI():
    reqData = request.get_json()
    val = reqData['val']
    return str(predict(val)[0])