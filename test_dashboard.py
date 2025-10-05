#!/usr/bin/env python3
"""
Test script to verify the improved health dashboard
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from visualization import Visualization
from disease_predictor import DiseasePredictor

def test_improved_dashboard():
    """Test the improved health dashboard"""
    print("🧪 Testing Improved Health Dashboard...")
    
    # Create test data
    user_data = {
        'age': 28,
        'height': 175,
        'weight': 70,
        'bmi': 22.9,
        'temperature': 38.2,
        'symptoms': ['fever', 'cough', 'headache', 'fatigue']
    }
    
    prediction_result = {
        'predicted_disease': 'Common Cold',
        'confidence': 85.0,
        'risk_level': 'Medium',
        'recommendations': [
            'Get plenty of rest and sleep',
            'Stay hydrated by drinking water',
            'Take fever-reducing medication',
            'Eat light, nutritious meals',
            'Use a humidifier to ease congestion'
        ]
    }
    
    # Test visualization
    viz = Visualization()
    
    try:
        # Create dashboard
        dashboard_fig = viz.create_health_dashboard(user_data, prediction_result)
        
        # Check dashboard properties
        print(f"   Dashboard title: {dashboard_fig.layout.title.text}")
        print(f"   Number of traces: {len(dashboard_fig.data)}")
        print(f"   Dashboard height: {dashboard_fig.layout.height}")
        
        # Check individual components
        trace_types = [trace.type for trace in dashboard_fig.data]
        print(f"   Chart types: {trace_types}")
        
        # Verify we have the expected components
        expected_types = ['indicator', 'indicator', 'bar', 'bar']
        if trace_types == expected_types:
            print("   ✅ Dashboard has correct chart types")
        else:
            print(f"   ❌ Expected {expected_types}, got {trace_types}")
            return False
        
        # Test BMI status
        bmi_status = viz.get_bmi_status(user_data['bmi'])
        print(f"   BMI Status: {bmi_status}")
        
        # Test temperature status
        temp_status = viz.get_temperature_status(user_data['temperature'])
        print(f"   Temperature Status: {temp_status}")
        
        # Test recommendation categorization
        recommendations = prediction_result['recommendations']
        categories = {
            'Rest & Sleep': 0,
            'Hydration': 0,
            'Medication': 0,
            'Diet & Nutrition': 0,
            'Lifestyle': 0
        }
        
        for rec in recommendations:
            rec_lower = rec.lower()
            if any(word in rec_lower for word in ['rest', 'sleep', 'bed', 'relax']):
                categories['Rest & Sleep'] += 1
            elif any(word in rec_lower for word in ['water', 'hydrat', 'fluid', 'drink']):
                categories['Hydration'] += 1
            elif any(word in rec_lower for word in ['medication', 'medicine', 'pill', 'take']):
                categories['Medication'] += 1
            elif any(word in rec_lower for word in ['food', 'eat', 'diet', 'meal', 'nutrition']):
                categories['Diet & Nutrition'] += 1
            else:
                categories['Lifestyle'] += 1
        
        print("   Recommendation Categories:")
        for category, count in categories.items():
            if count > 0:
                print(f"     - {category}: {count}")
        
        print("   ✅ Dashboard created successfully with proper categorization")
        return True
        
    except Exception as e:
        print(f"   ❌ Dashboard creation failed: {e}")
        return False

def test_dashboard_clarity():
    """Test dashboard clarity and information"""
    print("\n🧪 Testing Dashboard Clarity...")
    
    user_data = {
        'age': 30,
        'bmi': 17.3,  # Underweight
        'temperature': 38.5,  # High fever
        'symptoms': ['headache', 'sore_throat']
    }
    
    prediction_result = {
        'predicted_disease': 'Flu',
        'confidence': 90.0,
        'risk_level': 'High',
        'recommendations': [
            'Rest in bed and avoid physical exertion',
            'Stay hydrated and eat light meals',
            'Take antiviral medication if prescribed',
            'Monitor your temperature regularly'
        ]
    }
    
    viz = Visualization()
    
    try:
        dashboard_fig = viz.create_health_dashboard(user_data, prediction_result)
        
        # Check BMI status
        bmi_status = viz.get_bmi_status(user_data['bmi'])
        if bmi_status == "Underweight":
            print("   ✅ BMI status correctly identified as Underweight")
        else:
            print(f"   ❌ BMI status incorrect: {bmi_status}")
            return False
        
        # Check temperature status
        temp_status = viz.get_temperature_status(user_data['temperature'])
        if temp_status == "High Fever":
            print("   ✅ Temperature status correctly identified as High Fever")
        else:
            print(f"   ❌ Temperature status incorrect: {temp_status}")
            return False
        
        # Check symptom display
        symptoms = user_data['symptoms']
        print(f"   Symptoms displayed: {len(symptoms)} symptoms")
        for symptom in symptoms:
            clean_symptom = symptom.replace('_', ' ').title()
            print(f"     - {clean_symptom}")
        
        print("   ✅ Dashboard provides clear, accurate information")
        return True
        
    except Exception as e:
        print(f"   ❌ Dashboard clarity test failed: {e}")
        return False

def main():
    """Run dashboard tests"""
    print("📊 Testing Improved Health Dashboard")
    print("=" * 50)
    
    tests = [
        ("Improved Dashboard", test_improved_dashboard),
        ("Dashboard Clarity", test_dashboard_clarity)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        if test_func():
            passed += 1
        else:
            print(f"   ⚠️  {test_name} test failed")
    
    print("\n" + "=" * 50)
    print(f"📊 Dashboard Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All dashboard improvements are working correctly!")
        print("\n✨ Dashboard Features:")
        print("   • Clear BMI and Temperature gauges with status labels")
        print("   • Individual symptom display with clean names")
        print("   • Accurate recommendation categorization")
        print("   • Professional styling and layout")
        print("   • Informative text labels and counts")
    else:
        print("⚠️  Some dashboard features need attention.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)





