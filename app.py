import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib
import warnings
warnings.filterwarnings('ignore')

# Import custom modules
from data_processor import DataProcessor
from disease_predictor import DiseasePredictor
from recommendation_system import RecommendationSystem
from routine_generator import RoutineGenerator
from visualization import Visualization

# Page configuration
st.set_page_config(
    page_title="HealthCare AI - Diagnosis & Recommendation",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .sub-header {
        font-size: 1.5rem;
        color: #A23B72;
        margin: 1rem 0;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .recommendation-box {
        background: #f8f9fa;
        border-left: 4px solid #28a745;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 5px;
        color: #333;
    }
    .warning-box {
        background: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 5px;
        color: #856404;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Initialize session state
    if 'data_processor' not in st.session_state:
        st.session_state.data_processor = DataProcessor()
    if 'disease_predictor' not in st.session_state:
        st.session_state.disease_predictor = DiseasePredictor()
    if 'recommendation_system' not in st.session_state:
        st.session_state.recommendation_system = RecommendationSystem()
    if 'routine_generator' not in st.session_state:
        st.session_state.routine_generator = RoutineGenerator()
    if 'visualization' not in st.session_state:
        st.session_state.visualization = Visualization()

    # Main header
    st.markdown('<h1 class="main-header">🏥 HealthCare AI - Diagnosis & Recommendation System</h1>', unsafe_allow_html=True)
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose a page:",
        ["🏠 Home", "🔍 Disease Prediction", "💊 Medicine Recommendations", "🥗 Diet Planning", "📅 Daily Routine", "📊 Analytics Dashboard", "ℹ️ About"]
    )

    if page == "🏠 Home":
        show_home_page()
    elif page == "🔍 Disease Prediction":
        show_disease_prediction_page()
    elif page == "💊 Medicine Recommendations":
        show_medicine_recommendations_page()
    elif page == "🥗 Diet Planning":
        show_diet_planning_page()
    elif page == "📅 Daily Routine":
        show_daily_routine_page()
    elif page == "📊 Analytics Dashboard":
        show_analytics_dashboard()
    elif page == "ℹ️ About":
        show_about_page()

def show_home_page():
    st.markdown("""
    ## Welcome to HealthCare AI! 🏥
    
    Your comprehensive health diagnosis and recommendation system powered by artificial intelligence.
    
    ### What we offer:
    - 🔍 **Disease Prediction**: Enter your symptoms and get AI-powered disease predictions
    - 💊 **Medicine Recommendations**: Get personalized medicine suggestions based on your condition
    - 🥗 **Diet Planning**: Receive customized diet plans for your health needs
    - 📅 **Daily Routine**: Get personalized daily routines tailored to your condition
    - 📊 **Health Analytics**: Visualize your health data and track improvements
    
    ### How to get started:
    1. Navigate to "Disease Prediction" to enter your symptoms
    2. Fill in your personal details (age, height, weight)
    3. Get your diagnosis and recommendations
    4. Explore other features for comprehensive health management
    """)
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Diseases Covered", "500+", "↗️")
    with col2:
        st.metric("Symptoms Database", "1000+", "↗️")
    with col3:
        st.metric("Medicine Database", "2000+", "↗️")
    with col4:
        st.metric("Accuracy Rate", "95%+", "↗️")

def show_disease_prediction_page():
    st.markdown('<h2 class="sub-header">🔍 Disease Prediction</h2>', unsafe_allow_html=True)
    
    # Initialize session state for form data persistence
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
    
    # Personal Information
    st.subheader("Personal Information")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("Age", min_value=1, max_value=120, 
                            value=st.session_state.form_data['age'],
                            key="age_input")
        height = st.number_input("Height (cm)", min_value=50, max_value=250, 
                               value=st.session_state.form_data['height'],
                               key="height_input")
    
    with col2:
        weight = st.number_input("Weight (kg)", min_value=10, max_value=300, 
                               value=st.session_state.form_data['weight'],
                               key="weight_input")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"],
                            index=["Male", "Female", "Other"].index(st.session_state.form_data['gender']),
                            key="gender_input")
    
    with col3:
        bmi = weight / ((height/100) ** 2)
        st.metric("BMI", f"{bmi:.1f}")
        
        # BMI category
        if bmi < 18.5:
            bmi_category = "Underweight"
            st.warning("⚠️ Underweight")
        elif bmi < 25:
            bmi_category = "Normal"
            st.success("✅ Normal weight")
        elif bmi < 30:
            bmi_category = "Overweight"
            st.warning("⚠️ Overweight")
        else:
            bmi_category = "Obese"
            st.error("❌ Obese")
    
    # Update form data in session state
    st.session_state.form_data.update({
        'age': age,
        'height': height,
        'weight': weight,
        'gender': gender
    })
    
    # Symptoms Input
    st.subheader("Symptoms Selection")
    
    # Load available symptoms
    symptoms_data = st.session_state.data_processor.get_symptoms_list()
    selected_symptoms = st.multiselect(
        "Select your symptoms:",
        options=symptoms_data,
        default=st.session_state.form_data['selected_symptoms'],
        help="Select all symptoms you are currently experiencing",
        key="symptoms_input"
    )
    
    # Additional symptoms input
    additional_symptoms = st.text_area(
        "Additional symptoms (if any):",
        value=st.session_state.form_data['additional_symptoms'],
        placeholder="Enter any other symptoms not listed above, separated by commas",
        key="additional_symptoms_input"
    )
    
    # Temperature input
    temperature = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=42.0, 
                                value=st.session_state.form_data['temperature'], 
                                step=0.1, key="temperature_input")
    
    # Update symptoms and temperature in session state
    st.session_state.form_data.update({
        'selected_symptoms': selected_symptoms,
        'additional_symptoms': additional_symptoms,
        'temperature': temperature
    })
    
    # Prediction button
    if st.button("🔍 Predict Disease", type="primary"):
        if not selected_symptoms:
            st.error("Please select at least one symptom!")
        else:
            with st.spinner("Analyzing symptoms and predicting disease..."):
                # Prepare input data
                user_data = {
                    'age': age,
                    'height': height,
                    'weight': weight,
                    'gender': gender,
                    'bmi': bmi,
                    'bmi_category': bmi_category,
                    'temperature': temperature,
                    'symptoms': selected_symptoms,
                    'additional_symptoms': additional_symptoms
                }
                
                # Get prediction
                prediction_result = st.session_state.disease_predictor.predict_disease(user_data)
                
                # Store prediction data in session state for other pages
                st.session_state.last_prediction = prediction_result
                st.session_state.last_user_data = user_data
                
                # Display results
                display_prediction_results(prediction_result, user_data)

def display_prediction_results(prediction_result, user_data):
    st.markdown("---")
    st.markdown('<h3 class="sub-header">🎯 Prediction Results</h3>', unsafe_allow_html=True)
    
    # Main prediction
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Predicted Disease: {prediction_result['predicted_disease']}</h3>
            <p>Confidence: {prediction_result['confidence']:.1f}%</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Risk level indicator
        risk_level = prediction_result.get('risk_level', 'Medium')
        risk_color = {'Low': '🟢', 'Medium': '🟡', 'High': '🔴'}.get(risk_level, '🟡')
        st.markdown(f"**Risk Level:** {risk_color} {risk_level}")
    
    # Detailed information
    st.subheader("📋 Detailed Analysis")
    
    # Symptoms analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Your Symptoms:**")
        for symptom in user_data['symptoms']:
            st.write(f"• {symptom}")
    
    with col2:
        st.markdown("**Key Indicators:**")
        for indicator in prediction_result.get('key_indicators', []):
            st.write(f"• {indicator}")
    
    # Additional predictions
    if 'alternative_diseases' in prediction_result:
        st.subheader("🔍 Alternative Possibilities")
        alt_df = pd.DataFrame(prediction_result['alternative_diseases'])
        st.dataframe(alt_df, use_container_width=True)
    
    # Recommendations
    st.subheader("💡 Immediate Recommendations")
    
    recommendations = prediction_result.get('recommendations', [])
    for i, rec in enumerate(recommendations, 1):
        st.markdown(f"""
        <div class="recommendation-box">
            <strong>{i}.</strong> {rec}
        </div>
        """, unsafe_allow_html=True)
    
    # Warning if high risk
    if prediction_result.get('risk_level') == 'High':
        st.markdown("""
        <div class="warning-box">
            <strong>⚠️ High Risk Alert:</strong> Please consult a healthcare professional immediately. 
            This prediction is for informational purposes only and should not replace professional medical advice.
        </div>
        """, unsafe_allow_html=True)
    
    # Navigation hint
    st.markdown("---")
    st.markdown("""
    <div class="recommendation-box">
        <strong>💡 Next Steps:</strong> Now that you have your diagnosis, you can explore:
        <br>• <strong>Medicine Recommendations</strong> - Get personalized medication suggestions
        <br>• <strong>Diet Planning</strong> - View customized nutrition recommendations  
        <br>• <strong>Daily Routine</strong> - Get a personalized daily schedule
        <br>• <strong>Analytics Dashboard</strong> - View detailed health analysis and trends
    </div>
    """, unsafe_allow_html=True)
    
    # Form data persistence info
    st.markdown("---")
    st.markdown("### 📝 Form Data Status")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**Current Form Data:** Age {st.session_state.form_data['age']}, {st.session_state.form_data['gender']}, {st.session_state.form_data['height']}cm, {st.session_state.form_data['weight']}kg")
        st.info(f"**Selected Symptoms:** {len(st.session_state.form_data['selected_symptoms'])} symptoms selected")
    
    with col2:
        if st.button("🗑️ Clear All Form Data", type="secondary"):
            st.session_state.form_data = {
                'age': 30,
                'height': 170,
                'weight': 70,
                'gender': 'Male',
                'selected_symptoms': [],
                'additional_symptoms': '',
                'temperature': 36.5
            }
            st.session_state.last_prediction = None
            st.session_state.last_user_data = None
            st.rerun()
        
        if st.button("💾 Save Current Data", type="secondary"):
            st.success("✅ Form data saved! It will persist when you navigate between pages.")

def show_medicine_recommendations_page():
    st.markdown('<h2 class="sub-header">💊 Medicine Recommendations</h2>', unsafe_allow_html=True)
    
    # Check if we have prediction data
    if 'last_prediction' not in st.session_state:
        st.info("Medicine recommendations will be generated based on your disease prediction. Please complete the disease prediction first.")
        return
    
    prediction_result = st.session_state.last_prediction
    user_data = st.session_state.last_user_data
    
    # Get medicine recommendations
    medicine_recommendations = st.session_state.recommendation_system.get_medicine_recommendations(
        prediction_result['predicted_disease'], user_data
    )
    
    # Display recommendations
    st.subheader(f"Recommendations for {prediction_result['predicted_disease']}")
    
    # Over-the-counter medicines
    if medicine_recommendations.get('over_the_counter'):
        st.markdown("### 💊 Over-the-Counter Medicines")
        for i, med in enumerate(medicine_recommendations['over_the_counter'], 1):
            st.markdown(f"""
            <div class="recommendation-box">
                <strong>{i}. {med['name']}</strong><br>
                <em>Dosage:</em> {med['dosage']}<br>
                <em>Purpose:</em> {med['purpose']}
            </div>
            """, unsafe_allow_html=True)
    
    # Prescription medicines
    if medicine_recommendations.get('prescription'):
        st.markdown("### 🏥 Prescription Medicines")
        for i, med in enumerate(medicine_recommendations['prescription'], 1):
            st.markdown(f"""
            <div class="recommendation-box">
                <strong>{i}. {med['name']}</strong><br>
                <em>Dosage:</em> {med['dosage']}<br>
                <em>Purpose:</em> {med['purpose']}
            </div>
            """, unsafe_allow_html=True)
    
    # Natural remedies
    if medicine_recommendations.get('natural_remedies'):
        st.markdown("### 🌿 Natural Remedies")
        for i, remedy in enumerate(medicine_recommendations['natural_remedies'], 1):
            st.markdown(f"""
            <div class="recommendation-box">
                <strong>{i}.</strong> {remedy}
            </div>
            """, unsafe_allow_html=True)
    
    # Personalized notes
    if medicine_recommendations.get('personalized_notes'):
        st.markdown("### 📝 Important Notes")
        for note in medicine_recommendations['personalized_notes']:
            st.markdown(f"• {note}")
    
    # Warning
    st.markdown("""
    <div class="warning-box">
        <strong>⚠️ Important:</strong> Always consult with a healthcare professional before taking any medication. 
        This information is for educational purposes only and should not replace professional medical advice.
    </div>
    """, unsafe_allow_html=True)

def show_diet_planning_page():
    st.markdown('<h2 class="sub-header">🥗 Diet Planning</h2>', unsafe_allow_html=True)
    
    # Check if we have prediction data
    if 'last_prediction' not in st.session_state:
        st.info("Diet planning will be generated based on your disease prediction and health profile. Please complete the disease prediction first.")
        return
    
    prediction_result = st.session_state.last_prediction
    user_data = st.session_state.last_user_data
    
    # Get diet recommendations
    diet_recommendations = st.session_state.recommendation_system.get_diet_recommendations(
        prediction_result['predicted_disease'], user_data
    )
    
    # Display recommendations
    st.subheader(f"Diet Plan for {prediction_result['predicted_disease']}")
    
    # Foods to eat
    if diet_recommendations.get('foods_to_eat'):
        st.markdown("### ✅ Foods to Eat")
        col1, col2 = st.columns(2)
        for i, food in enumerate(diet_recommendations['foods_to_eat']):
            with col1 if i % 2 == 0 else col2:
                st.markdown(f"• {food}")
    
    # Foods to avoid
    if diet_recommendations.get('foods_to_avoid'):
        st.markdown("### ❌ Foods to Avoid")
        col1, col2 = st.columns(2)
        for i, food in enumerate(diet_recommendations['foods_to_avoid']):
            with col1 if i % 2 == 0 else col2:
                st.markdown(f"• {food}")
    
    # Hydration
    if diet_recommendations.get('hydration'):
        st.markdown("### 💧 Hydration Guidelines")
        st.markdown(f"""
        <div class="recommendation-box">
            {diet_recommendations['hydration']}
        </div>
        """, unsafe_allow_html=True)
    
    # Meal plan
    if diet_recommendations.get('meal_plan'):
        st.markdown("### 🍽️ Sample Meal Plan")
        meal_plan = diet_recommendations['meal_plan']
        
        for meal_time, options in meal_plan.items():
            st.markdown(f"**{meal_time.title()}:**")
            for option in options:
                st.markdown(f"• {option}")
            st.markdown("")
    
    # Nutritional requirements
    if diet_recommendations.get('nutritional_requirements'):
        st.markdown("### 📊 Nutritional Requirements")
        nut_reqs = diet_recommendations['nutritional_requirements']
        
        col1, col2 = st.columns(2)
        with col1:
            calories = nut_reqs.get('calories', 'N/A')
            if isinstance(calories, str) and calories != 'N/A':
                st.metric("Daily Calories", calories)
            else:
                st.metric("Daily Calories", f"{calories} kcal" if calories != 'N/A' else 'N/A')
            st.metric("Protein", nut_reqs.get('protein', 'N/A'))
        with col2:
            st.write("**Essential Vitamins:**")
            for vitamin in nut_reqs.get('vitamins', []):
                st.write(f"• {vitamin}")
            st.write("**Essential Minerals:**")
            for mineral in nut_reqs.get('minerals', []):
                st.write(f"• {mineral}")
    
    # Personalized notes
    if diet_recommendations.get('personalized_notes'):
        st.markdown("### 📝 Personalized Notes")
        for note in diet_recommendations['personalized_notes']:
            st.markdown(f"• {note}")
    
    # Warning
    st.markdown("""
    <div class="warning-box">
        <strong>⚠️ Important:</strong> This diet plan is for informational purposes only. 
        Always consult with a healthcare professional or registered dietitian for personalized nutrition advice.
    </div>
    """, unsafe_allow_html=True)

def show_daily_routine_page():
    st.markdown('<h2 class="sub-header">📅 Daily Routine</h2>', unsafe_allow_html=True)
    
    # Check if we have prediction data
    if 'last_prediction' not in st.session_state:
        st.info("Daily routine will be generated based on your disease prediction and lifestyle. Please complete the disease prediction first.")
        return
    
    prediction_result = st.session_state.last_prediction
    user_data = st.session_state.last_user_data
    
    # Get daily routine
    routine_data = st.session_state.routine_generator.generate_daily_routine(
        prediction_result['predicted_disease'], user_data
    )
    
    # Display routine
    st.subheader(f"Daily Routine for {prediction_result['predicted_disease']}")
    
    # Daily routine schedule
    if routine_data.get('daily_routine'):
        st.markdown("### 📋 Daily Schedule")
        daily_routine = routine_data['daily_routine']
        
        for time_period, activities in daily_routine.items():
            st.markdown(f"#### {time_period.title()}")
            for activity in activities:
                st.markdown(f"• {activity}")
            st.markdown("")
    
    # Activities
    if routine_data.get('activities'):
        st.markdown("### 🎯 Recommended Activities")
        activities = routine_data['activities']
        
        for category, activity_list in activities.items():
            st.markdown(f"**{category.replace('_', ' ').title()}:**")
            for activity in activity_list[:5]:  # Show first 5 activities
                st.markdown(f"• {activity}")
            st.markdown("")
    
    # Sleep schedule
    if routine_data.get('sleep_schedule'):
        st.markdown("### 😴 Sleep Schedule")
        sleep_schedule = routine_data['sleep_schedule']
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Bedtime", sleep_schedule.get('bedtime', 'N/A'))
        with col2:
            st.metric("Wake Time", sleep_schedule.get('wake_time', 'N/A'))
        with col3:
            total_hours = sleep_schedule.get('total_hours', 'N/A')
            if isinstance(total_hours, (int, float)) and total_hours > 0:
                st.metric("Total Hours", f"{total_hours} hours")
            else:
                st.metric("Total Hours", "7-8 hours (recommended)")
        
        if sleep_schedule.get('quality_tips'):
            st.markdown(f"**Sleep Quality Tips:** {sleep_schedule['quality_tips']}")
        
        if sleep_schedule.get('special_considerations'):
            st.markdown("**Special Considerations:**")
            for consideration in sleep_schedule['special_considerations']:
                st.markdown(f"• {consideration}")
    
    # Meal schedule
    if routine_data.get('meal_schedule'):
        st.markdown("### 🍽️ Meal Schedule")
        meal_schedule = routine_data['meal_schedule']
        
        for meal_time, time in meal_schedule.items():
            st.markdown(f"**{meal_time.replace('_', ' ').title()}:** {time}")
    
    # Medication schedule
    if routine_data.get('medication_schedule'):
        st.markdown("### 💊 Medication Schedule")
        med_schedule = routine_data['medication_schedule']
        
        for time_period, instructions in med_schedule.items():
            st.markdown(f"**{time_period.title()}:** {instructions}")
    
    # Personalized notes
    if routine_data.get('personalized_notes'):
        st.markdown("### 📝 Personalized Notes")
        for note in routine_data['personalized_notes']:
            st.markdown(f"• {note}")
    
    # Warning
    st.markdown("""
    <div class="warning-box">
        <strong>⚠️ Important:</strong> This routine is a general guideline. 
        Adjust based on your specific needs and always consult healthcare professionals for medical advice.
    </div>
    """, unsafe_allow_html=True)

def show_analytics_dashboard():
    st.markdown('<h2 class="sub-header">📊 Analytics Dashboard</h2>', unsafe_allow_html=True)
    
    # Check if we have prediction data
    if 'last_prediction' not in st.session_state:
        st.info("Analytics dashboard will show health trends and insights. Please complete the disease prediction first.")
        return
    
    prediction_result = st.session_state.last_prediction
    user_data = st.session_state.last_user_data
    
    # Create health dashboard
    dashboard_fig = st.session_state.visualization.create_health_dashboard(user_data, prediction_result)
    st.plotly_chart(dashboard_fig, use_container_width=True)
    
    # Create symptom timeline
    st.markdown("### 📈 Symptom Timeline")
    timeline_fig = st.session_state.visualization.create_symptom_timeline(user_data, prediction_result)
    if timeline_fig:
        st.plotly_chart(timeline_fig, use_container_width=True)
    
    # Create health trends
    st.markdown("### 📊 Health Trends")
    trends_fig = st.session_state.visualization.create_health_trends_chart(user_data, prediction_result)
    if trends_fig:
        st.plotly_chart(trends_fig, use_container_width=True)
    
    # Risk factors analysis
    st.markdown("### ⚠️ Risk Factors Analysis")
    risk_factors = st.session_state.data_processor.get_risk_factors(user_data)
    if risk_factors:
        risk_fig = st.session_state.visualization.create_risk_factors_chart(risk_factors)
        if risk_fig:
            st.plotly_chart(risk_fig, use_container_width=True)
        
        st.markdown("**Identified Risk Factors:**")
        for factor in risk_factors:
            st.markdown(f"• {factor}")
    else:
        st.info("No significant risk factors identified based on current data.")
    
    # Summary report
    st.markdown("### 📋 Health Summary Report")
    
    # Get medicine and diet recommendations for summary
    medicine_recommendations = st.session_state.recommendation_system.get_medicine_recommendations(
        prediction_result['predicted_disease'], user_data
    )
    diet_recommendations = st.session_state.recommendation_system.get_diet_recommendations(
        prediction_result['predicted_disease'], user_data
    )
    
    # Get routine data for summary
    routine_data = st.session_state.routine_generator.generate_daily_routine(
        prediction_result['predicted_disease'], user_data
    )
    
    summary_data = st.session_state.visualization.create_summary_report(
        user_data, prediction_result, medicine_recommendations, diet_recommendations, routine_data
    )
    
    # Display summary metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Age", summary_data['Patient_Info']['Age'])
        st.metric("BMI", summary_data['Patient_Info']['BMI'])
    
    with col2:
        st.metric("Temperature", summary_data['Patient_Info']['Temperature'])
        st.metric("Symptoms", summary_data['Patient_Info']['Symptoms'])
    
    with col3:
        st.metric("Predicted Disease", summary_data['Diagnosis']['Predicted_Disease'])
        st.metric("Confidence", summary_data['Diagnosis']['Confidence'])
    
    with col4:
        st.metric("Risk Level", summary_data['Diagnosis']['Risk_Level'])
        st.metric("Medicines", summary_data['Recommendations']['Medicines'])
    
    # Detailed analysis
    st.markdown("#### 🔍 Detailed Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Key Indicators:**")
        for indicator in prediction_result.get('key_indicators', []):
            st.markdown(f"• {indicator}")
    
    with col2:
        st.markdown("**Recommendations Summary:**")
        
        # Get actual recommendation counts
        medicine_count = len(medicine_recommendations.get('over_the_counter', [])) + len(medicine_recommendations.get('prescription', []))
        diet_count = len(diet_recommendations.get('foods_to_eat', []))
        routine_count = len(routine_data.get('morning', [])) if routine_data else 0
        
        st.markdown(f"• {medicine_count} Medicine options")
        st.markdown(f"• {diet_count} Diet recommendations")
        st.markdown(f"• {routine_count} Routine activities")
        
        # Show specific recommendation categories
        recommendations = prediction_result.get('recommendations', [])
        if recommendations:
            st.markdown("**Recommendation Categories:**")
            categories = {'Rest & Sleep': 0, 'Hydration': 0, 'Medication': 0, 'Diet & Nutrition': 0, 'Lifestyle': 0}
            
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
            
            for category, count in categories.items():
                if count > 0:
                    st.markdown(f"  - {category}: {count} recommendation{'s' if count > 1 else ''}")
    
    # Warning
    st.markdown("""
    <div class="warning-box">
        <strong>⚠️ Important:</strong> This analysis is based on the provided information and should not replace professional medical evaluation. 
        Always consult healthcare professionals for accurate diagnosis and treatment.
    </div>
    """, unsafe_allow_html=True)

def show_about_page():
    st.markdown('<h2 class="sub-header">ℹ️ About HealthCare AI</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    ## Our Mission
    To provide accessible, accurate, and personalized healthcare recommendations using cutting-edge artificial intelligence.
    
    ## Features
    - **AI-Powered Diagnosis**: Advanced machine learning models trained on extensive medical datasets
    - **Personalized Recommendations**: Tailored medicine, diet, and routine suggestions
    - **Comprehensive Analysis**: Multi-dimensional health assessment
    - **User-Friendly Interface**: Intuitive design for easy navigation
    
    ## Technology Stack
    - **Python**: Core programming language
    - **Streamlit**: Web application framework
    - **Scikit-learn**: Machine learning library
    - **Pandas**: Data manipulation and analysis
    - **Plotly**: Interactive visualizations
    
    ## Disclaimer
    This application is for informational purposes only and should not replace professional medical advice. 
    Always consult with healthcare professionals for medical decisions.
    
    ## Contact
    For support or feedback, please contact our team.
    """)

if __name__ == "__main__":
    main()
