import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import warnings
warnings.filterwarnings('ignore')

class DataProcessor:
    def __init__(self):
        self.symptoms_data = None
        self.diseases_data = None
        self.medical_data = None
        self.symptom_severity = None
        self.label_encoders = {}
        self.scaler = StandardScaler()
        self.load_data()
    
    def load_data(self):
        """Load and preprocess all datasets"""
        try:
            # Load symptoms and diseases dataset
            self.symptoms_data = pd.read_csv('Final_Augmented_dataset_Diseases_and_Symptoms.csv')
            
            # Load health dataset
            self.medical_data = pd.read_csv('health_dataset.csv')
            
            # Load symptom severity data
            self.symptom_severity = pd.read_csv('Symptom-severity.csv')
            
            # Load additional medical data
            try:
                self.diseases_data = pd.read_csv('medical data.csv')
            except:
                self.diseases_data = None
            
            # Preprocess data
            self.preprocess_data()
            
        except Exception as e:
            print(f"Error loading data: {e}")
            self.create_sample_data()
    
    def create_sample_data(self):
        """Create sample data if files are not found"""
        # Sample symptoms data
        self.symptoms_data = pd.DataFrame({
            'diseases': ['Common Cold', 'Flu', 'Headache', 'Fever', 'Cough'],
            'fever': [1, 1, 0, 1, 0],
            'cough': [1, 1, 0, 0, 1],
            'headache': [0, 1, 1, 0, 0],
            'fatigue': [1, 1, 1, 1, 0],
            'sore_throat': [1, 1, 0, 0, 0]
        })
        
        # Sample symptom severity
        self.symptom_severity = pd.DataFrame({
            'Symptom': ['fever', 'cough', 'headache', 'fatigue', 'sore_throat'],
            'weight': [5, 3, 4, 3, 4]
        })
        
        # Sample medical data
        self.medical_data = pd.DataFrame({
            'Disease': ['Common Cold', 'Flu', 'Headache', 'Fever', 'Cough'],
            'Symptom_1': ['fever', 'fever', 'headache', 'fever', 'cough'],
            'Symptom_2': ['cough', 'fatigue', 'fatigue', 'headache', 'fatigue'],
            'Symptom_3': ['sore_throat', 'headache', 'nausea', 'chills', 'sore_throat']
        })
    
    def preprocess_data(self):
        """Preprocess the loaded data"""
        if self.symptoms_data is not None:
            # Clean column names
            self.symptoms_data.columns = self.symptoms_data.columns.str.strip()
            
            # Handle missing values
            self.symptoms_data = self.symptoms_data.fillna(0)
            
            # Convert binary columns to int
            symptom_columns = [col for col in self.symptoms_data.columns if col != 'diseases']
            for col in symptom_columns:
                self.symptoms_data[col] = self.symptoms_data[col].astype(int)
        
        if self.symptom_severity is not None:
            # Clean symptom severity data
            self.symptom_severity.columns = self.symptom_severity.columns.str.strip()
            self.symptom_severity = self.symptom_severity.dropna()
    
    def get_symptoms_list(self):
        """Get list of available symptoms"""
        if self.symptoms_data is not None:
            symptom_columns = [col for col in self.symptoms_data.columns if col != 'diseases']
            return sorted(symptom_columns)
        return []
    
    def get_diseases_list(self):
        """Get list of available diseases"""
        if self.symptoms_data is not None:
            return sorted(self.symptoms_data['diseases'].unique().tolist())
        return []
    
    def get_symptom_severity(self, symptom):
        """Get severity weight for a symptom"""
        if self.symptom_severity is not None:
            severity_row = self.symptom_severity[
                self.symptom_severity['Symptom'].str.lower() == symptom.lower()
            ]
            if not severity_row.empty:
                return severity_row['weight'].iloc[0]
        return 1  # Default weight
    
    def prepare_training_data(self):
        """Prepare data for machine learning training"""
        if self.symptoms_data is None:
            return None, None
        
        # Separate features and target
        X = self.symptoms_data.drop('diseases', axis=1)
        y = self.symptoms_data['diseases']
        
        # Encode target variable
        if 'diseases' not in self.label_encoders:
            self.label_encoders['diseases'] = LabelEncoder()
            y_encoded = self.label_encoders['diseases'].fit_transform(y)
        else:
            y_encoded = self.label_encoders['diseases'].transform(y)
        
        return X, y_encoded
    
    def get_disease_symptoms(self, disease):
        """Get symptoms associated with a specific disease"""
        if self.symptoms_data is None:
            return []
        
        disease_row = self.symptoms_data[self.symptoms_data['diseases'] == disease]
        if disease_row.empty:
            return []
        
        symptoms = []
        for col in self.symptoms_data.columns:
            if col != 'diseases' and disease_row[col].iloc[0] == 1:
                symptoms.append(col)
        
        return symptoms
    
    def get_disease_info(self, disease):
        """Get comprehensive information about a disease"""
        info = {
            'name': disease,
            'symptoms': self.get_disease_symptoms(disease),
            'severity': 'Medium',  # Default severity
            'description': f"Information about {disease}",
            'precautions': [],
            'treatment_approach': 'Consult a healthcare professional'
        }
        
        # Add specific information based on disease
        if 'cold' in disease.lower():
            info.update({
                'severity': 'Low',
                'description': 'Common cold is a viral infection of the upper respiratory tract.',
                'precautions': ['Rest', 'Stay hydrated', 'Avoid close contact with others'],
                'treatment_approach': 'Symptomatic treatment and rest'
            })
        elif 'flu' in disease.lower():
            info.update({
                'severity': 'Medium',
                'description': 'Influenza is a viral infection that affects the respiratory system.',
                'precautions': ['Rest', 'Stay hydrated', 'Antiviral medication if prescribed'],
                'treatment_approach': 'Antiviral treatment and supportive care'
            })
        elif 'fever' in disease.lower():
            info.update({
                'severity': 'Medium',
                'description': 'Fever is an elevated body temperature, often a sign of infection.',
                'precautions': ['Monitor temperature', 'Stay hydrated', 'Rest'],
                'treatment_approach': 'Antipyretics and identify underlying cause'
            })
        
        return info
    
    def calculate_symptom_score(self, symptoms, additional_symptoms=""):
        """Calculate a weighted score based on symptoms and their severity"""
        total_score = 0
        symptom_count = 0
        
        for symptom in symptoms:
            severity = self.get_symptom_severity(symptom)
            total_score += severity
            symptom_count += 1
        
        # Add additional symptoms if provided
        if additional_symptoms:
            additional_list = [s.strip() for s in additional_symptoms.split(',') if s.strip()]
            for symptom in additional_list:
                severity = self.get_symptom_severity(symptom)
                total_score += severity
                symptom_count += 1
        
        return total_score, symptom_count
    
    def get_health_metrics(self, age, height, weight, temperature):
        """Calculate various health metrics"""
        bmi = weight / ((height/100) ** 2)
        
        # BMI category
        if bmi < 18.5:
            bmi_category = "Underweight"
        elif bmi < 25:
            bmi_category = "Normal"
        elif bmi < 30:
            bmi_category = "Overweight"
        else:
            bmi_category = "Obese"
        
        # Temperature category
        if temperature < 36.0:
            temp_category = "Low"
        elif temperature <= 37.5:
            temp_category = "Normal"
        elif temperature <= 38.5:
            temp_category = "Mild Fever"
        else:
            temp_category = "High Fever"
        
        return {
            'bmi': bmi,
            'bmi_category': bmi_category,
            'temperature_category': temp_category,
            'age_group': self.get_age_group(age)
        }
    
    def get_age_group(self, age):
        """Categorize age into groups"""
        if age < 18:
            return "Child/Teen"
        elif age < 30:
            return "Young Adult"
        elif age < 50:
            return "Adult"
        elif age < 65:
            return "Middle-aged"
        else:
            return "Senior"
    
    def get_risk_factors(self, user_data):
        """Identify potential risk factors based on user data"""
        risk_factors = []
        
        # BMI risk factors
        bmi = user_data.get('bmi', 0)
        if bmi < 18.5:
            risk_factors.append("Underweight - may indicate nutritional deficiencies")
        elif bmi > 30:
            risk_factors.append("Obesity - increased risk of cardiovascular diseases")
        
        # Age risk factors
        age = user_data.get('age', 0)
        if age > 65:
            risk_factors.append("Advanced age - increased risk of chronic diseases")
        
        # Temperature risk factors
        temperature = user_data.get('temperature', 36.5)
        if temperature > 38.5:
            risk_factors.append("High fever - may indicate serious infection")
        
        # Symptom count risk factors
        symptoms = user_data.get('symptoms', [])
        if len(symptoms) > 5:
            risk_factors.append("Multiple symptoms - may indicate complex condition")
        
        return risk_factors
