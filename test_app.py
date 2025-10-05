#!/usr/bin/env python3
"""
Test script for HealthCare AI Application
This script tests the core functionality without running the full Streamlit app
"""

import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test if all modules can be imported"""
    try:
        from data_processor import DataProcessor
        from disease_predictor import DiseasePredictor
        from recommendation_system import RecommendationSystem
        from routine_generator import RoutineGenerator
        from visualization import Visualization
        print("✅ All modules imported successfully")
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def test_data_processor():
    """Test DataProcessor functionality"""
    try:
        from data_processor import DataProcessor
        processor = DataProcessor()
        
        # Test basic functionality
        symptoms = processor.get_symptoms_list()
        diseases = processor.get_diseases_list()
        
        print(f"✅ DataProcessor: Found {len(symptoms)} symptoms, {len(diseases)} diseases")
        return True
    except Exception as e:
        print(f"❌ DataProcessor error: {e}")
        return False

def test_disease_predictor():
    """Test DiseasePredictor functionality"""
    try:
        from disease_predictor import DiseasePredictor
        predictor = DiseasePredictor()
        
        # Test with sample data
        user_data = {
            'age': 30,
            'height': 170,
            'weight': 70,
            'gender': 'Male',
            'bmi': 24.2,
            'bmi_category': 'Normal',
            'temperature': 37.2,
            'symptoms': ['fever', 'cough', 'headache'],
            'additional_symptoms': ''
        }
        
        result = predictor.predict_disease(user_data)
        print(f"✅ DiseasePredictor: Predicted {result['predicted_disease']} with {result['confidence']:.1f}% confidence")
        return True
    except Exception as e:
        print(f"❌ DiseasePredictor error: {e}")
        return False

def test_recommendation_system():
    """Test RecommendationSystem functionality"""
    try:
        from recommendation_system import RecommendationSystem
        recommender = RecommendationSystem()
        
        # Test medicine recommendations
        user_data = {
            'age': 30,
            'bmi': 24.2,
            'gender': 'Male'
        }
        
        medicine_recs = recommender.get_medicine_recommendations('Common Cold', user_data)
        diet_recs = recommender.get_diet_recommendations('Common Cold', user_data)
        
        print(f"✅ RecommendationSystem: {len(medicine_recs['over_the_counter'])} OTC medicines, {len(diet_recs['foods_to_eat'])} diet recommendations")
        return True
    except Exception as e:
        print(f"❌ RecommendationSystem error: {e}")
        return False

def test_routine_generator():
    """Test RoutineGenerator functionality"""
    try:
        from routine_generator import RoutineGenerator
        generator = RoutineGenerator()
        
        user_data = {
            'age': 30,
            'bmi': 24.2,
            'temperature': 37.2,
            'symptoms': ['fever', 'cough']
        }
        
        routine = generator.generate_daily_routine('Common Cold', user_data)
        
        print(f"✅ RoutineGenerator: Generated routine with {len(routine['daily_routine'])} time periods")
        return True
    except Exception as e:
        print(f"❌ RoutineGenerator error: {e}")
        return False

def test_visualization():
    """Test Visualization functionality"""
    try:
        from visualization import Visualization
        viz = Visualization()
        
        user_data = {
            'age': 30,
            'bmi': 24.2,
            'temperature': 37.2,
            'symptoms': ['fever', 'cough', 'headache']
        }
        
        prediction_result = {
            'predicted_disease': 'Common Cold',
            'confidence': 85.0,
            'risk_level': 'Medium',
            'recommendations': ['Rest', 'Stay hydrated', 'Take medication']
        }
        
        # Test dashboard creation
        dashboard = viz.create_health_dashboard(user_data, prediction_result)
        print("✅ Visualization: Dashboard created successfully")
        return True
    except Exception as e:
        print(f"❌ Visualization error: {e}")
        return False

def main():
    """Run all tests"""
    print("🏥 HealthCare AI - Testing Application Components")
    print("=" * 50)
    
    tests = [
        ("Module Imports", test_imports),
        ("Data Processor", test_data_processor),
        ("Disease Predictor", test_disease_predictor),
        ("Recommendation System", test_recommendation_system),
        ("Routine Generator", test_routine_generator),
        ("Visualization", test_visualization)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🧪 Testing {test_name}...")
        if test_func():
            passed += 1
        else:
            print(f"   ⚠️  {test_name} test failed")
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Application is ready to run.")
        print("\n🚀 To start the application, run:")
        print("   streamlit run app.py")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)


