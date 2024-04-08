from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_contract_types')
def get_contract_types():
    response = jsonify({
        'contract': util.get_contract_types()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')  
    return response

@app.route('/get_internetservice_types')
def get_internetservice_types():
    response = jsonify({
        'internetservices': util.get_internetservice_types()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')  
    return response

@app.route('/get_paymentmethod_types')
def get_paymentmethod_types():
    response = jsonify({
        'paymentmethod': util.get_paymentmethod_types()
    })
    response.headers.add('Access-Control-Allow-Origin', '*' ) 
    return response

@app.route('/predict_customer_churn', methods=['POST'])
def predict_customer_churn():
    data = request.get_json()

    gender = data["gender"]
    seniorcitizen = data["seniorcitizen"]
    partner = data["partner"]
    dependents = data["dependents"]
    tenure = data["tenure"]
    phoneservice = data["phoneservice"]
    multiplelines = data["multiplelines"]
    onlinesecurity = data["onlinesecurity"]
    onlinebackup = data["onlinebackup"]
    deviceprotection = data["deviceprotection"]
    techsupport = data["techsupport"]
    streamingtv = data["streamingtv"]
    streamingmovies = data["streamingmovies"]
    paperlessbilling = data["paperlessbilling"]
    monthlycharges = data["monthlycharges"]
    totalcharges = data["totalcharges"]
    internetservice = data["internetservice"]
    contract = data["contract"]
    paymentmethod = data["paymentmethod"]

    estimated_churn_probability = util.get_estimated_churn_probability(gender, seniorcitizen, partner, dependents, tenure, phoneservice, multiplelines, onlinesecurity, onlinebackup, deviceprotection, techsupport, streamingtv, streamingmovies, paperlessbilling, monthlycharges, totalcharges, internetservice, contract, paymentmethod)

    response = jsonify({
        'estimated_churn_probability': estimated_churn_probability
    })
    response.headers.add('Access-Control-Allow-Origin', '*')  # replace with your trusted domain
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Customer Churn Prediction...")
    util.load_saved_artifacts()
    app.run()
