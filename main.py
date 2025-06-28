from fastapi import FastAPI, Path
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


@app.get('/patient/{patient_id}')
def view_single_patient(patient_id: str = Path(..., description='ID of the patient', Example='P001')):
    data = load_data()
        
    if patient_id in data:
        return data[patient_id]
    
    return {"error": "Patient id not found"}