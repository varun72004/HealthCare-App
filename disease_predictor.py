import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import warnings
warnings.filterwarnings('ignore')

class DiseasePredictor:
    def __init__(self):
        self.models = {}
        self.label_encoders = {}
        self.symptom_columns = []
        self.disease_info = {}
        self.load_or_train_models()
    
    def load_or_train_models(self):
        """Load pre-trained models or train new ones"""
        try:
            # Try to load pre-trained models
            self.models = joblib.load('disease_models.pkl')
            self.label_encoders = joblib.load('label_encoders.pkl')
            self.symptom_columns = joblib.load('symptom_columns.pkl')
            print("Loaded pre-trained models")
        except:
            # Train new models
            self.train_models()
    
    def train_models(self):
        """Train machine learning models for disease prediction"""
        from data_processor import DataProcessor
        
        # Initialize data processor
        data_processor = DataProcessor()
        
        # Get training data
        X, y = data_processor.prepare_training_data()
        
        if X is None or len(X) == 0:
            print("No training data available")
            return
        
        # Store symptom columns
        self.symptom_columns = X.columns.tolist()
        
        # Split data (handle case where some classes have only 1 sample)
        try:
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42, stratify=y
            )
        except ValueError:
            # If stratification fails, use random split
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
        
        # Train multiple models
        models_to_train = {
            'RandomForest': RandomForestClassifier(n_estimators=100, random_state=42),
            'GradientBoosting': GradientBoostingClassifier(n_estimators=100, random_state=42),
            'LogisticRegression': LogisticRegression(random_state=42, max_iter=1000),
            'SVM': SVC(probability=True, random_state=42)
        }
        
        best_model = None
        best_score = 0
        
        for name, model in models_to_train.items():
            # Train model
            model.fit(X_train, y_train)
            
            # Evaluate model
            y_pred = model.predict(X_test)
            score = accuracy_score(y_test, y_pred)
            
            print(f"{name} Accuracy: {score:.3f}")
            
            # Store model
            self.models[name] = model
            
            # Track best model
            if score > best_score:
                best_score = score
                best_model = name
        
        print(f"Best model: {best_model} with accuracy: {best_score:.3f}")
        
        # Save models
        joblib.dump(self.models, 'disease_models.pkl')
        joblib.dump(self.label_encoders, 'label_encoders.pkl')
        joblib.dump(self.symptom_columns, 'symptom_columns.pkl')
        
        # Create disease information database
        self.create_disease_database(data_processor)
    
    def create_disease_database(self, data_processor):
        """Create a comprehensive disease information database"""
        diseases = data_processor.get_diseases_list()
        
        for disease in diseases:
            self.disease_info[disease] = data_processor.get_disease_info(disease)
    
    def predict_disease(self, user_data):
        """Predict disease based on user input"""
        if not self.models:
            return self.get_fallback_prediction(user_data)
        
        # Prepare input features
        input_features = self.prepare_input_features(user_data)
        
        if input_features is None:
            return self.get_fallback_prediction(user_data)
        
        # Get predictions from all models
        predictions = {}
        probabilities = {}
        
        for model_name, model in self.models.items():
            try:
                pred = model.predict([input_features])[0]
                proba = model.predict_proba([input_features])[0]
                
                # Convert prediction back to disease name
                if 'diseases' in self.label_encoders:
                    disease_name = self.label_encoders['diseases'].inverse_transform([pred])[0]
                else:
                    disease_name = str(pred)
                
                predictions[model_name] = disease_name
                probabilities[model_name] = max(proba)
                
            except Exception as e:
                print(f"Error with {model_name}: {e}")
                continue
        
        # Ensemble prediction (majority vote)
        if predictions:
            # Count votes
            vote_count = {}
            for model_name, prediction in predictions.items():
                if prediction in vote_count:
                    vote_count[prediction] += 1
                else:
                    vote_count[prediction] = 1
            
            # Get most voted prediction
            predicted_disease = max(vote_count, key=vote_count.get)
            
            # Calculate average confidence
            confidence = np.mean([prob for prob in probabilities.values()]) * 100
            
            # Get disease information
            disease_info = self.disease_info.get(predicted_disease, {})
            
            # Calculate risk level
            risk_level = self.calculate_risk_level(user_data, predicted_disease)
            
            # Generate recommendations
            recommendations = self.generate_recommendations(user_data, predicted_disease, disease_info)
            
            # Get alternative diseases
            alternative_diseases = self.get_alternative_diseases(predictions, probabilities)
            
            return {
                'predicted_disease': predicted_disease,
                'confidence': confidence,
                'risk_level': risk_level,
                'disease_info': disease_info,
                'recommendations': recommendations,
                'alternative_diseases': alternative_diseases,
                'key_indicators': self.get_key_indicators(user_data, predicted_disease),
                'model_predictions': predictions
            }
        else:
            return self.get_fallback_prediction(user_data)
    
    def prepare_input_features(self, user_data):
        """Prepare input features for prediction"""
        if not self.symptom_columns:
            return None
        
        # Initialize feature vector
        features = np.zeros(len(self.symptom_columns))
        
        # Map symptoms to features
        symptoms = user_data.get('symptoms', [])
        for i, symptom in enumerate(self.symptom_columns):
            if symptom in symptoms:
                features[i] = 1
        
        # Add additional symptoms if provided
        additional_symptoms = user_data.get('additional_symptoms', '')
        if additional_symptoms:
            additional_list = [s.strip().lower() for s in additional_symptoms.split(',') if s.strip()]
            for i, symptom in enumerate(self.symptom_columns):
                if symptom.lower() in additional_list:
                    features[i] = 1
        
        return features
    
    def calculate_risk_level(self, user_data, predicted_disease):
        """Calculate risk level based on user data and predicted disease"""
        risk_score = 0
        
        # Age factor
        age = user_data.get('age', 30)
        if age > 65:
            risk_score += 2
        elif age < 18:
            risk_score += 1
        
        # BMI factor
        bmi = user_data.get('bmi', 22)
        if bmi > 30 or bmi < 18.5:
            risk_score += 1
        
        # Temperature factor
        temperature = user_data.get('temperature', 36.5)
        if temperature > 38.5:
            risk_score += 2
        elif temperature > 37.5:
            risk_score += 1
        
        # Symptom count factor
        symptoms = user_data.get('symptoms', [])
        if len(symptoms) > 5:
            risk_score += 1
        
        # Disease-specific risk
        disease_risk = self.get_disease_risk_level(predicted_disease)
        risk_score += disease_risk
        
        # Determine risk level
        if risk_score >= 5:
            return "High"
        elif risk_score >= 3:
            return "Medium"
        else:
            return "Low"
    
    def get_disease_risk_level(self, disease):
        """Get risk level for specific disease"""
        high_risk_diseases = ['heart disease', 'diabetes', 'cancer', 'stroke', 'pneumonia']
        medium_risk_diseases = ['flu', 'bronchitis', 'asthma', 'hypertension']
        
        disease_lower = disease.lower()
        
        for high_risk in high_risk_diseases:
            if high_risk in disease_lower:
                return 2
        
        for medium_risk in medium_risk_diseases:
            if medium_risk in disease_lower:
                return 1
        
        return 0
    
    def generate_recommendations(self, user_data, predicted_disease, disease_info):
        """Generate personalized recommendations"""
        recommendations = []
        
        # General recommendations based on disease
        if 'cold' in predicted_disease.lower():
            recommendations.extend([
                "Get plenty of rest and sleep",
                "Stay hydrated by drinking water and warm fluids",
                "Use a humidifier to ease congestion",
                "Gargle with warm salt water for sore throat"
            ])
        elif 'flu' in predicted_disease.lower():
            recommendations.extend([
                "Rest in bed and avoid physical exertion",
                "Stay hydrated and eat light, nutritious meals",
                "Take antiviral medication if prescribed by doctor",
                "Monitor your temperature regularly"
            ])
        elif 'fever' in predicted_disease.lower():
            recommendations.extend([
                "Take fever-reducing medication as directed",
                "Stay hydrated with water and electrolyte drinks",
                "Rest and avoid strenuous activities",
                "Use cool compresses to reduce body temperature"
            ])
        else:
            recommendations.extend([
                "Consult with a healthcare professional",
                "Monitor your symptoms closely",
                "Get adequate rest and maintain good hygiene",
                "Follow any prescribed treatment plan"
            ])
        
        # Age-specific recommendations
        age = user_data.get('age', 30)
        if age > 65:
            recommendations.append("Consider consulting a geriatric specialist")
        elif age < 18:
            recommendations.append("Ensure proper nutrition for growth and recovery")
        
        # BMI-specific recommendations
        bmi = user_data.get('bmi', 22)
        if bmi > 30:
            recommendations.append("Consider weight management as part of treatment")
        elif bmi < 18.5:
            recommendations.append("Focus on proper nutrition and weight gain")
        
        return recommendations
    
    def get_alternative_diseases(self, predictions, probabilities):
        """Get alternative disease predictions"""
        # Sort by probability
        sorted_diseases = sorted(probabilities.items(), key=lambda x: x[1], reverse=True)
        
        alternatives = []
        for model_name, prob in sorted_diseases[:3]:
            disease = predictions[model_name]
            alternatives.append({
                'disease': disease,
                'confidence': f"{prob*100:.1f}%",
                'model': model_name
            })
        
        return alternatives
    
    def get_key_indicators(self, user_data, predicted_disease):
        """Get key indicators that led to the prediction"""
        indicators = []
        
        # Temperature indicators
        temperature = user_data.get('temperature', 36.5)
        if temperature > 37.5:
            indicators.append(f"Elevated temperature ({temperature}°C)")
        
        # BMI indicators
        bmi = user_data.get('bmi', 22)
        if bmi > 30:
            indicators.append(f"High BMI ({bmi:.1f})")
        elif bmi < 18.5:
            indicators.append(f"Low BMI ({bmi:.1f})")
        
        # Symptom indicators
        symptoms = user_data.get('symptoms', [])
        if symptoms:
            indicators.append(f"Presenting symptoms: {', '.join(symptoms[:3])}")
        
        # Age indicators
        age = user_data.get('age', 30)
        if age > 65:
            indicators.append(f"Advanced age ({age} years)")
        
        return indicators
    
    def get_fallback_prediction(self, user_data):
        """Fallback prediction when models are not available"""
        symptoms = user_data.get('symptoms', [])
        temperature = user_data.get('temperature', 36.5)
        
        # Simple rule-based prediction
        if temperature > 38.5:
            if 'cough' in symptoms and 'fatigue' in symptoms:
                predicted_disease = "Flu"
            else:
                predicted_disease = "Fever"
        elif 'headache' in symptoms and 'fatigue' in symptoms:
            predicted_disease = "Headache/Migraine"
        elif 'cough' in symptoms and 'sore_throat' in symptoms:
            predicted_disease = "Common Cold"
        else:
            predicted_disease = "General Illness"
        
        return {
            'predicted_disease': predicted_disease,
            'confidence': 60.0,
            'risk_level': 'Medium',
            'disease_info': {},
            'recommendations': [
                "Consult with a healthcare professional for accurate diagnosis",
                "Monitor your symptoms closely",
                "Get adequate rest and maintain good hygiene"
            ],
            'alternative_diseases': [],
            'key_indicators': [f"Presenting symptoms: {', '.join(symptoms)}"],
            'model_predictions': {'Fallback': predicted_disease}
        }
