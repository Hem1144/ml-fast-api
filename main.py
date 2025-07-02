from fastapi import FastAPI, Path, HTTPException, Query
import json
from enum import Enum

app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data

patients_db = load_data()

class SortField(str, Enum):
    height = "height"
    weight = "weight"
    bmi = "bmi"

class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"

@app.get("/")
def patient():
    return {'message':'Patients management system'}


@app.get("/about-us")
def about():
    return {'message': 'API for manage patients records'}

@app.get("/contact-us")
def contact():
    return {"Contact Info": "Please fell fee to contact us when needed."}


@app.get('/view')
def view():
    return patients_db



@app.get('/patient/{patient_id}')
def view_single_patient(patient_id: str = Path(..., description='ID of the patient', Example='P001')):
    if patient_id in patients_db:
        return patients_db[patient_id]
    
    raise HTTPException(status_code=404, detail="Patient not found!")


@app.get("/sort")
def sort_patients(sort_by: SortField = Query(..., description='Sort the patient data on the basis of Height, Weight or BMI'), order: SortOrder = Query(SortOrder.asc, description='Sort in asc or desc order')):
    
    sort_order = order == SortOrder.desc
    sorted_data = sorted(patients_db.values(), key=lambda x: x.get(sort_by.value, 0), reverse=sort_order)
    return sorted_data
    
    