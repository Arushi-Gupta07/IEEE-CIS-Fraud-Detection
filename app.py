print("Hello")
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






print('The scikit-learn version is {}.'.format(sklearn.__version__))
print(lightgbm.__version__)

app = Flask(__name__)


@app.route("/")
def Index():
     return render_template('Index.html')


    
  

if __name__=='__main__':
    app.run(debug=True)
