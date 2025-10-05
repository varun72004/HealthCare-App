#!/usr/bin/env python3
"""
Demo script showing how to use the HealthCare AI Application
This demonstrates the complete workflow without the Streamlit interface
"""

import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_processor import DataProcessor
from disease_predictor import DiseasePredictor
from recommendation_system import RecommendationSystem
from routine_generator import RoutineGenerator
from visualization import Visualization

def demo_complete_workflow():
    """Demonstrate the complete healthcare AI workflow"""
    
    print("🏥 HealthCare AI - Complete Workflow Demo")
    print("=" * 50)
    
    # Initialize all components
    print("\n1. Initializing components...")
    data_processor = DataProcessor()
    disease_predictor = DiseasePredictor()
    recommendation_system = RecommendationSystem()
    routine_generator = RoutineGenerator()
    visualization = Visualization()
    print("✅ All components initialized")
    
    # Sample user data
    print("\n2. Sample user data:")
    user_data = {
        'age': 28,
        'height': 175,
        'weight': 70,
        'gender': 'Male',
        'bmi': 22.9,
        'bmi_category': 'Normal',
        'temperature': 38.2,
        'symptoms': ['fever', 'cough', 'headache', 'fatigue'],
        'additional_symptoms': 'sore throat, body aches'
    }
    
    print(f"   Age: {user_data['age']} years")
    print(f"   Height: {user_data['height']} cm")
    print(f"   Weight: {user_data['weight']} kg")
    print(f"   BMI: {user_data['bmi']}")
    print(f"   Temperature: {user_data['temperature']}°C")
    print(f"   Symptoms: {', '.join(user_data['symptoms'])}")
    print(f"   Additional: {user_data['additional_symptoms']}")
    
    # Step 1: Disease Prediction
    print("\n3. Disease Prediction:")
    prediction_result = disease_predictor.predict_disease(user_data)
    print(f"   Predicted Disease: {prediction_result['predicted_disease']}")
    print(f"   Confidence: {prediction_result['confidence']:.1f}%")
    print(f"   Risk Level: {prediction_result['risk_level']}")
    print(f"   Key Indicators: {', '.join(prediction_result.get('key_indicators', []))}")
    
    # Step 2: Medicine Recommendations
    print("\n4. Medicine Recommendations:")
    medicine_recs = recommendation_system.get_medicine_recommendations(
        prediction_result['predicted_disease'], user_data
    )
    
    print("   Over-the-Counter Medicines:")
    for i, med in enumerate(medicine_recs['over_the_counter'][:3], 1):
        print(f"   {i}. {med['name']} - {med['purpose']}")
    
    print("   Natural Remedies:")
    for i, remedy in enumerate(medicine_recs['natural_remedies'][:3], 1):
        print(f"   {i}. {remedy}")
    
    # Step 3: Diet Planning
    print("\n5. Diet Planning:")
    diet_recs = recommendation_system.get_diet_recommendations(
        prediction_result['predicted_disease'], user_data
    )
    
    print("   Foods to Eat:")
    for i, food in enumerate(diet_recs['foods_to_eat'][:5], 1):
        print(f"   {i}. {food}")
    
    print("   Foods to Avoid:")
    for i, food in enumerate(diet_recs['foods_to_avoid'][:3], 1):
        print(f"   {i}. {food}")
    
    print(f"   Hydration: {diet_recs['hydration']}")
    
    # Step 4: Daily Routine
    print("\n6. Daily Routine:")
    routine_data = routine_generator.generate_daily_routine(
        prediction_result['predicted_disease'], user_data
    )
    
    print("   Daily Schedule:")
    for time_period, activities in routine_data['daily_routine'].items():
        print(f"   {time_period.title()}:")
        for activity in activities[:3]:  # Show first 3 activities
            print(f"     • {activity}")
    
    print(f"   Sleep Schedule: {routine_data['sleep_schedule']['bedtime']} - {routine_data['sleep_schedule']['wake_time']}")
    print(f"   Total Sleep: {routine_data['sleep_schedule']['total_hours']} hours")
    
    # Step 5: Health Analytics
    print("\n7. Health Analytics:")
    
    # Create health dashboard
    dashboard_fig = visualization.create_health_dashboard(user_data, prediction_result)
    print("   ✅ Health dashboard created")
    
    # Create symptom timeline
    timeline_fig = visualization.create_symptom_timeline(user_data, prediction_result)
    print("   ✅ Symptom timeline created")
    
    # Risk factors
    risk_factors = data_processor.get_risk_factors(user_data)
    print(f"   Risk Factors: {len(risk_factors)} identified")
    for factor in risk_factors:
        print(f"     • {factor}")
    
    # Summary report
    summary_data = visualization.create_summary_report(
        user_data, prediction_result, medicine_recs, diet_recs, routine_data
    )
    
    print("\n8. Summary Report:")
    print(f"   Patient Age: {summary_data['Patient_Info']['Age']}")
    print(f"   BMI: {summary_data['Patient_Info']['BMI']}")
    print(f"   Temperature: {summary_data['Patient_Info']['Temperature']}")
    print(f"   Symptoms Count: {summary_data['Patient_Info']['Symptoms']}")
    print(f"   Predicted Disease: {summary_data['Diagnosis']['Predicted_Disease']}")
    print(f"   Confidence: {summary_data['Diagnosis']['Confidence']}")
    print(f"   Risk Level: {summary_data['Diagnosis']['Risk_Level']}")
    print(f"   Medicine Options: {summary_data['Recommendations']['Medicines']}")
    print(f"   Diet Recommendations: {summary_data['Recommendations']['Diet_Items']}")
    print(f"   Routine Activities: {summary_data['Recommendations']['Routine_Activities']}")
    
    print("\n" + "=" * 50)
    print("🎉 Complete workflow demonstration finished!")
    print("\n💡 To use the full interactive application:")
    print("   streamlit run app.py")
    print("   Then open http://localhost:8501 in your browser")

if __name__ == "__main__":
    demo_complete_workflow()


