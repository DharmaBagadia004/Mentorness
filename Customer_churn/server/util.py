import pickle
import json

__internetservice = None
__contract = None
__paymentmethod = None
__data_columns = None
__model = None

def get_estimated_churn_probability(gender, seniorcitizen, partner, dependents, tenure, phoneservice, multiplelines, onlinesecurity, onlinebackup, deviceprotection, techsupport, streamingtv, streamingmovies, paperlessbilling, monthlycharges, totalcharges, internetservice, contract, paymentmethod):
    try:
        locser_index = __data_columns.index("internetservice_dsl")
    except:
        locser_index = -1

    try:
        loccon_index = __data_columns.index("contract_month-to-month")
    except:
        loccon_index = -1

    try:
        locpay_index = __data_columns.index("paymentmethod_bank transfer (automatic)")
    except:
        locpay_index = -1

    x = []
    x.append(int(gender))
    x.append(int(seniorcitizen))
    x.append(int(partner))
    x.append(int(dependents))
    x.append(int(tenure))
    x.append(int(phoneservice))
    x.append(int(multiplelines))
    x.append(int(onlinesecurity))
    x.append(int(onlinebackup))
    x.append(int(deviceprotection))
    x.append(int(techsupport))
    x.append(int(streamingtv))
    x.append(int(streamingmovies))
    x.append(int(paperlessbilling))
    x.append(float(monthlycharges))
    x.append(float(totalcharges))

    for i in range(16, 19):
        if i == locser_index:
            x.append(True)
        else:
            x.append(False)

    for i in range(19, 22):
        if i == loccon_index:
            x.append(True)
        else:
            x.append(False)

    for i in range(22, 26):
        if i == locpay_index:
            x.append(True)
        else:
            x.append(False)

    return __model.predict_proba([x])[0][1]

def load_saved_artifacts():
    global __data_columns
    global __internetservice
    global __contract
    global __paymentmethod

    with open("D:/Mentorness Internship/Customer_churn/server/artifacts/columns2.json", "r") as f:
        __data_columns = json.load(f)['data_columns']

    __internetservice = [__data_columns.index("internetservice_dsl"), 
                         __data_columns.index("internetservice_fiber optic"), 
                         __data_columns.index("internetservice_no")]

    __contract = [__data_columns.index("contract_month-to-month"), 
                  __data_columns.index("contract_one year"), 
                  __data_columns.index("contract_two year")]

    __paymentmethod = [__data_columns.index("paymentmethod_bank transfer (automatic)"), 
                       __data_columns.index("paymentmethod_credit card (automatic)"), 
                       __data_columns.index("paymentmethod_electronic check"), 
                       __data_columns.index("paymentmethod_mailed check")]

    global __model
    if __model is None:
        with open('D:/Mentorness Internship/Customer_churn/server/artifacts/churn_model.pickle', 'rb') as f:
            __model = pickle.load(f)

def get_internetservice_types():
    return __internetservice

def get_contract_types():
    return __contract

def get_paymentmethod_types():
    return __paymentmethod

def get_data_columns():
    return __data_columns
