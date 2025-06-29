from fastapi import FastAPI, Path, HTTPException, Query
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
    
    raise HTTPException(status_code=404, detail="Patient not found!")


@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description='Sort the patient data on the basis of Hight, Weight or BMI'), order: str = Query('asc', description='sort in asc or desc order')):
    
    valid_fields = ['height', 'weight', 'bmi']
    
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field section from {valid_fields}')
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail="Invalid order select between asc and desc")
    
    data = load_data()
    
    sort_order = True if order == 'desc' else False
    
    sort_data = sorted(data.values(), key=lambda x:x.get(sort_by, 0), reverse=sort_order)
    
    return sort_data
    
    