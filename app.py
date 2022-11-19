from flask import Flask,render_template
import requests
import pickle
import pandas as pd
import numpy as np
import sklearn
import lightgbm
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from lightgbm import LGBMClassifier
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
import joblib
from zipfile import ZipFile





print('The scikit-learn version is {}.'.format(sklearn.__version__))
print(lightgbm.__version__)

app = Flask(__name__)


url = 'https://github.com/Arushi-Gupta07/Heroku-demo/blob/main/model.pkl?raw=true'
with open("model.pkl",'wb') as output_file: output_file.write(requests.get(url).content)

with open("model.pkl", 'rb') as file:  LGBM = pickle.load(file)




     

@app.route("/")
def Index():
     return render_template('Index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    
    
    file = request.files['file']
    fileName = file.filename
    
    file.save(secure_filename(file.filename))
    
  	 
    df=pd.read_csv(fileName)
      
    x_test=df
    
    
    
    
    
    
    y_test_pred_lgbm = LGBM.predict_proba(x_test)[:,1]
    
    #make prediction
    prediction=""
    for i in y_test_pred_lgbm:
      if i > 0.5:
         prediction="Transaction is fraud"
      else:
         prediction="Transaction is non-fraud"
        
    print(prediction)        
       
    return render_template('Index.html', prediction_text='This {} transaction.'.format(prediction)) 

    

if __name__=='__main__':
    app.run(debug=True)