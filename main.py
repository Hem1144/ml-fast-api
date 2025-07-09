from fastapi import FastAPI, Path
import json

app = FastAPI()

def load_data():
    # Example: Load data from a JSON file or return a sample dictionary
    # Replace this with your actual data loading logic
    try:
        with open('patients.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # Return sample data if file not found
        return {
            "P001": {"name": "John Doe", "age": 30},
            "P002": {"name": "Jane Smith", "age": 25}
        }

@app.get("/")
def contact_info():
    return {"Contact Info": "Please feel free to contact us when needed."}


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