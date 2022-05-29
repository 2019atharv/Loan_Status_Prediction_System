
import numpy as np
from flask import Flask, jsonify, render_template,request
import pickle


app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def main():
    return render_template('index.html')

# @app.route('/predict',methods=['POST'])
# def predict():
    int_features

@app.route('/predict',methods=['POST','GET'])
def predict():
    print(request.form)
    int_features = [int(x) for x in request.form.values()]
    age = int_features[0]
    age=int(age)
    int_features.pop(0)
    final = [np.array(int_features)]
    print(int_features)
    print(final)
    prediction = model.predict(final)
    output= prediction

    # gender = request.form.values['Gender']
    # marital = request.form.values['Marital']
    # dependents = request.form.values['Dependents']
    # education = request.form.values['Education']
    # employed = request.form.values['Employed']
    # income = request.form.values['Income']
    # coappincome = request.form.values['CoappIncome']
    # loanamount = request.form.values['loanAmt']
    # term = request.form.values['Term']
    # history = request.form.values['History']
    # propertyType = request.form.values['Property']
    # arr = np.array([[gender,marital,dependents,education,employed,income,coappincome,loanamount,term,history,propertyType]])
    # prediction = model.predict(arr)
    # pred = model.predict(arr)
    # output = prediction[0]
    print(output[0])
    if age<18:
        return render_template('index.html',age_text='Age is less than 18')
    if age>60:
        return render_template('index.html',age_text='Age is greater than 60')
    
    if output[0] == 0:
        print('Loan not approved')
        return render_template('index.html',prediction_text='Loan is not approved')
    else:
        print("loan approved")
        return render_template('index.html',prediction_text='Loan is approved')

    # print(arr)



if __name__ == "__main__":
    app.run(debug=True)