from flask import Flask,request,jsonify
from flask_cors import CORS
import joblib
import os

# flask is use to create our backend application/server
# request lets Flask to access data send by the frountend
# the backend need to send the predicted to react

# CORS is important
# react-> localhost:3000, Flask->localhost:5000
# browser normally resticts communication between different origins,it allows react frountend to communicate with our Flask backend
# CORS- Cross-Origin Resource Sharing

# joblib allows python to load (sms_spam_model.pkl,tfidf_vectorizer.pkl) save objects back into the memory, so we don't  have to train the model every time the backend start

# this helps python works with file and folders(we need this because our model file is nt inside our backend folder )

app = Flask(__name__) #this creats our Flask backend application
CORS(app)#Allows other origins,such as our React Frountend to communicate with this backend 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ML_DIR=os.path.join(BASE_DIR,"ML")

# BREAKDOWN OF THE COMPLEX LINE

# __file__
# means:The location of the current Python file.
# Our current file is:Backend/app.py


# os.path.abspath(__file__)
# gets the full/absolute path of app.py. Something conceptually like: (C:\Users\YourName\Machine Learning\Project 1 - SMS_Spam_Detection\Backend\app.py)

# os.path.dirname(...)
# gets the folder containing something.
# So the first dirname takes us from:
# Backend/app.py
# to:
# Backend
# The second dirname takes us from:
# Backend
# to:
# Project 1 - SMS_Spam_Detection
# Therefore:
# BASE_DIR
# becomes our main project folder.

model = joblib.load(os.path.join(ML_DIR,"sms_spam_model.pkl")) #contains our trained spam detection model

# os.path.join = creates the correct file path: ML/sms_spam_model.pkl
# joblib.load = lodes the save model


tfidf= joblib.load(os.path.join(ML_DIR,"tfidf_vectorizer.pkl"))

# loads over priviously trained TF-IDF vectorizer

@app.route("/") #tells us that if someone visit this perticular url,run this function. So Flask know which function to execute

def home():
    return jsonify({
        "message":"SMS Spam Detection Backend is running"
    })

# backend sends a json respond
 
@app.route("/predict",methods=["POST"])

# creating "/predict" ,so the  frountend will eventually send a request to this ,eg= http/...../predict
# use POST because we are sending data to backend

def predict():
    data= request.get_json()
    # request give us access to what frountend sent and rest extracts json data
    message= data.get("message","")
    # taking value associated with message
    if not message.strip():
    # its checks weather the use actually entered a msg or not, and strip remove the spaces from beginning and end
     return jsonify({
        "error":"Please enter a msg"
    }),400
    message_tfidf= tfidf.transform([message]) #converts into numerical representation expected by the trained model
    prediction= model.predict(message_tfidf)[0]
    if prediction ==1:
      result ="SPAM"

    else:
     result="HUMAN"
    return jsonify({
    "message":message,
    "prediction":result
    })

if __name__=="__main__":
    app.run(debug=True)
