from flask import Flask 
render_template, request
import random
from sklearn.ensemble import 
RandomForestClassifier 
from sklearn.model_selection import 
train_test_split 
from sklearn.metrics import 
accuracy_score 

app = Flask(__GasGuard__)

# Simulated gas sensor data
gas_data = {
    'methane': random.uniform(0, 100) ,
    'carbon monoxide' : random.uniform(0, 100) ,
    'hydrogen_sulfide' : random.uniform(0, 100) ,
}

#Training data
X_train = [
    [10, 20, 30],  # normal conditions 
    [10, 20, 30],  # warning conditions 
    [10, 20, 30],  #
    [10, 20, 30],  #
    [10, 20, 30],  #
    [10, 20, 30],  #
]