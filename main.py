from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    
    return data

@app.get("/")
def patient():
    return {'message':'Patients management system'}


@app.get("/about")
def about():
    return {'message': 'API for manage patients records'}

@app.get("/contact")
def contact():
    return {"Contact Info": "Please fell fee to contact us when needed."}


@app.get('/view')
def view():
    data = load_data()
    
    return data


