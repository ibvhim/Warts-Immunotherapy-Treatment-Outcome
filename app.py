import pickle 
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load Model
model = pickle.load(open('BC_immunotherapy.pkl','rb'))
scaler = pickle.load(open('scaling.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/predict_api',methods=['POST'])
# def predict_api():
#     data=request.get_json('data')
#     print(data)
#     reshaped_data=np.array(list(data.values())).reshape(1, -1)
#     print ("DATA RETRIEVED AND RESHAPED ->",reshaped_data)
#     new_data=scaler.transform(np.array(list(data.values())).reshape(1, -1))
#     output=model.predict(new_data)
#     print (output[0])
#     return jsonify(output[0])

    

@app.route('/predict_',methods=['POST'])
def predict():
    # takes input
    data = [request.form.values()] 

    # # normalizes data
    # final_input= scaler.transform(np.array(data).reshape(1,-1))
    # print (final_input)

    # # predicts the outcome
    # output = model.predict(final_input)[0]
    # outcome = ''
    # # outcome text
    # if output == 1:
    #     outcome = "Congratulations! According to the model, your warts can be removed using Immunotherapy!"
    # else:
    #     outcome = "According to our model Immunotherapy will not treat your warts. Unfortuantely, you might have to look for alternative treatment methods."
    
    # displays outcome 
    outcome = [x for x in data]
    return render_template("home.html",prediction_text=outcome) 

if __name__=="__main__":
    app.run(debug=True)