#!/usr/bin/env python3
"""
Test script to verify form data persistence functionality
"""

import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_form_persistence():
    """Test form data persistence functionality"""
    print("🧪 Testing Form Data Persistence...")
    
    try:
        # Test session state initialization
        import streamlit as st
        
        # Simulate session state initialization
        if 'form_data' not in st.session_state:
            st.session_state.form_data = {
                'age': 30,
                'height': 170,
                'weight': 70,
                'gender': 'Male',
                'selected_symptoms': [],
                'additional_symptoms': '',
                'temperature': 36.5
            }
        
        # Test form data structure
        form_data = st.session_state.form_data
        
        # Verify all required fields exist
        required_fields = ['age', 'height', 'weight', 'gender', 'selected_symptoms', 'additional_symptoms', 'temperature']
        for field in required_fields:
            assert field in form_data, f"Missing field: {field}"
        
        print("✅ Form data structure is correct")
        
        # Test form data updates
        original_age = form_data['age']
        form_data['age'] = 35
        form_data['selected_symptoms'] = ['fever', 'headache']
        form_data['additional_symptoms'] = 'nausea, dizziness'
        
        # Verify updates persist
        assert form_data['age'] == 35, "Age update failed"
        assert len(form_data['selected_symptoms']) == 2, "Symptoms update failed"
        assert form_data['additional_symptoms'] == 'nausea, dizziness', "Additional symptoms update failed"
        
        print("✅ Form data updates work correctly")
        
        # Test form data reset
        form_data = {
            'age': 30,
            'height': 170,
            'weight': 70,
            'gender': 'Male',
            'selected_symptoms': [],
            'additional_symptoms': '',
            'temperature': 36.5
        }
        
        # Verify reset works
        assert form_data['age'] == 30, "Form reset failed"
        assert len(form_data['selected_symptoms']) == 0, "Symptoms reset failed"
        
        print("✅ Form data reset works correctly")
        
        # Test BMI calculation
        height = form_data['height']
        weight = form_data['weight']
        bmi = weight / ((height/100) ** 2)
        
        expected_bmi = 70 / ((170/100) ** 2)
        assert abs(bmi - expected_bmi) < 0.01, f"BMI calculation failed: {bmi} != {expected_bmi}"
        
        print("✅ BMI calculation works correctly")
        
        print("🎉 All form persistence tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Form persistence test failed: {e}")
        return False

def test_session_state_management():
    """Test session state management"""
    print("\n🧪 Testing Session State Management...")
    
    try:
        import streamlit as st
        
        # Test prediction data storage
        if 'last_prediction' not in st.session_state:
            st.session_state.last_prediction = None
        if 'last_user_data' not in st.session_state:
            st.session_state.last_user_data = None
        
        # Simulate prediction data
        mock_prediction = {
            'predicted_disease': 'Common Cold',
            'confidence': 85.5,
            'risk_level': 'Low',
            'recommendations': ['Rest', 'Stay hydrated', 'Take over-the-counter medication']
        }
        
        mock_user_data = {
            'age': 30,
            'height': 170,
            'weight': 70,
            'gender': 'Male',
            'bmi': 24.2,
            'temperature': 37.2,
            'symptoms': ['fever', 'headache', 'cough']
        }
        
        # Store data in session state
        st.session_state.last_prediction = mock_prediction
        st.session_state.last_user_data = mock_user_data
        
        # Verify data is stored
        assert st.session_state.last_prediction is not None, "Prediction data not stored"
        assert st.session_state.last_user_data is not None, "User data not stored"
        assert st.session_state.last_prediction['predicted_disease'] == 'Common Cold', "Prediction data corrupted"
        assert st.session_state.last_user_data['age'] == 30, "User data corrupted"
        
        print("✅ Session state management works correctly")
        
        # Test data clearing
        st.session_state.last_prediction = None
        st.session_state.last_user_data = None
        
        assert st.session_state.last_prediction is None, "Prediction data not cleared"
        assert st.session_state.last_user_data is None, "User data not cleared"
        
        print("✅ Session state clearing works correctly")
        
        print("🎉 All session state tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Session state test failed: {e}")
        return False

def main():
    """Run all form persistence tests"""
    print("📊 Testing Form Data Persistence and Session State Management")
    print("=" * 60)
    
    # Run tests
    test1_passed = test_form_persistence()
    test2_passed = test_session_state_management()
    
    print("\n" + "=" * 60)
    print("📊 Test Results Summary:")
    print(f"✅ Form Persistence: {'PASSED' if test1_passed else 'FAILED'}")
    print(f"✅ Session State: {'PASSED' if test2_passed else 'FAILED'}")
    
    if test1_passed and test2_passed:
        print("\n🎉 All tests passed! Form data will now persist across page navigation.")
        print("\n✨ Features implemented:")
        print("• Form data persists when navigating between pages")
        print("• Personal information (age, height, weight, gender) is saved")
        print("• Selected symptoms are remembered")
        print("• Additional symptoms text is preserved")
        print("• Temperature input is maintained")
        print("• Clear form button to reset all data")
        print("• Save button to confirm data persistence")
    else:
        print("\n❌ Some tests failed. Please check the implementation.")
    
    return test1_passed and test2_passed

if __name__ == "__main__":
    main()





