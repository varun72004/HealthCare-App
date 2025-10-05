import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

class Visualization:
    def __init__(self):
        self.color_palette = {
            'primary': '#2E86AB',
            'secondary': '#A23B72',
            'success': '#28a745',
            'warning': '#ffc107',
            'danger': '#dc3545',
            'info': '#17a2b8',
            'light': '#f8f9fa',
            'dark': '#343a40'
        }
    
    def create_health_dashboard(self, user_data, prediction_result):
        """Create a clean, focused health dashboard"""
        from plotly.subplots import make_subplots
        
        # Create simplified layout with more space
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('BMI Status', 'Temperature Status', 'Symptom Analysis', 'Recommendation Categories'),
            specs=[[{"type": "indicator"}, {"type": "indicator"}],
                   [{"type": "bar"}, {"type": "bar"}]],
            vertical_spacing=0.25,
            horizontal_spacing=0.15
        )
        
        # BMI Indicator - simplified
        bmi = user_data.get('bmi', 22)
        bmi_status = self.get_bmi_status(bmi)
        fig.add_trace(go.Indicator(
            mode="gauge+number",
            value=bmi,
            title={'text': f"BMI: {bmi_status}", 'font': {'size': 14}},
            gauge={
                'axis': {'range': [None, 40]},
                'bar': {'color': self.get_bmi_color(bmi)},
                'steps': [
                    {'range': [0, 18.5], 'color': "lightblue"},
                    {'range': [18.5, 25], 'color': "lightgreen"},
                    {'range': [25, 30], 'color': "yellow"},
                    {'range': [30, 40], 'color': "red"}
                ]
            }
        ), row=1, col=1)
        
        # Temperature Indicator - simplified
        temperature = user_data.get('temperature', 36.5)
        temp_status = self.get_temperature_status(temperature)
        fig.add_trace(go.Indicator(
            mode="gauge+number",
            value=temperature,
            title={'text': f"Temperature: {temp_status}", 'font': {'size': 14}},
            gauge={
                'axis': {'range': [35, 42]},
                'bar': {'color': self.get_temperature_color(temperature)},
                'steps': [
                    {'range': [35, 36.5], 'color': "lightblue"},
                    {'range': [36.5, 37.5], 'color': "lightgreen"},
                    {'range': [37.5, 38.5], 'color': "yellow"},
                    {'range': [38.5, 42], 'color': "red"}
                ]
            }
        ), row=1, col=2)
        
        # Symptom Analysis - simplified
        symptoms = user_data.get('symptoms', [])
        if symptoms:
            # Show only first 5 symptoms to avoid overcrowding
            display_symptoms = symptoms[:5]
            symptom_data = {}
            for symptom in display_symptoms:
                clean_symptom = symptom.replace('_', ' ').title()
                symptom_data[clean_symptom] = 1
            
            fig.add_trace(go.Bar(
                x=list(symptom_data.keys()),
                y=list(symptom_data.values()),
                marker_color=self.color_palette['primary'],
                name='Symptoms'
            ), row=2, col=1)
        else:
            fig.add_trace(go.Bar(
                x=['No Symptoms'],
                y=[0],
                marker_color=self.color_palette['light']
            ), row=2, col=1)
        
        # Recommendation Categories - simplified
        recommendations = prediction_result.get('recommendations', [])
        if recommendations:
            categories = {
                'Rest': 0,
                'Hydration': 0,
                'Medication': 0,
                'Diet': 0,
                'Other': 0
            }
            
            for rec in recommendations:
                rec_lower = rec.lower()
                if any(word in rec_lower for word in ['rest', 'sleep', 'bed', 'relax']):
                    categories['Rest'] += 1
                elif any(word in rec_lower for word in ['water', 'hydrat', 'fluid', 'drink']):
                    categories['Hydration'] += 1
                elif any(word in rec_lower for word in ['medication', 'medicine', 'pill', 'take']):
                    categories['Medication'] += 1
                elif any(word in rec_lower for word in ['food', 'eat', 'diet', 'meal', 'nutrition']):
                    categories['Diet'] += 1
                else:
                    categories['Other'] += 1
            
            # Only show categories with recommendations
            filtered_categories = {k: v for k, v in categories.items() if v > 0}
            
            if filtered_categories:
                fig.add_trace(go.Bar(
                    x=list(filtered_categories.keys()),
                    y=list(filtered_categories.values()),
                    marker_color=self.color_palette['primary'],
                    name='Recommendations'
                ), row=2, col=2)
            else:
                fig.add_trace(go.Bar(
                    x=['General Care'],
                    y=[1],
                    marker_color=self.color_palette['info']
                ), row=2, col=2)
        else:
            fig.add_trace(go.Bar(
                x=['No Recommendations'],
                y=[0],
                marker_color=self.color_palette['light']
            ), row=2, col=2)
        
        # Update layout - clean and simple
        fig.update_layout(
            title={
                'text': "Health Dashboard",
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 18, 'color': '#2E86AB'}
            },
            showlegend=False,
            height=600,
            template="plotly_white",
            font=dict(size=11),
            margin=dict(l=40, r=40, t=60, b=40)
        )
        
        # Update axes - simplified
        fig.update_xaxes(tickangle=0, row=2, col=1)
        fig.update_xaxes(tickangle=0, row=2, col=2)
        fig.update_yaxes(showticklabels=False, row=2, col=1)
        fig.update_yaxes(showticklabels=False, row=2, col=2)
        
        return fig
    
    def add_health_metrics(self, fig, user_data, row, col):
        """Add health metrics indicators"""
        bmi = user_data.get('bmi', 22)
        temperature = user_data.get('temperature', 36.5)
        
        # BMI Gauge
        fig.add_trace(go.Indicator(
            mode="gauge+number",
            value=bmi,
            title={'text': "BMI"},
            gauge={
                'axis': {'range': [None, 40]},
                'bar': {'color': self.get_bmi_color(bmi)},
                'steps': [
                    {'range': [0, 18.5], 'color': "lightgray"},
                    {'range': [18.5, 25], 'color': "lightgreen"},
                    {'range': [25, 30], 'color': "yellow"},
                    {'range': [30, 40], 'color': "red"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 30
                }
            }
        ), row=row, col=col)
        
        # Temperature Gauge
        fig.add_trace(go.Indicator(
            mode="gauge+number",
            value=temperature,
            title={'text': "Temperature (°C)"},
            gauge={
                'axis': {'range': [35, 42]},
                'bar': {'color': self.get_temperature_color(temperature)},
                'steps': [
                    {'range': [35, 36.5], 'color': "lightblue"},
                    {'range': [36.5, 37.5], 'color': "lightgreen"},
                    {'range': [37.5, 38.5], 'color': "yellow"},
                    {'range': [38.5, 42], 'color': "red"}
                ]
            }
        ), row=row, col=col)
    
    def add_symptom_analysis(self, fig, user_data, row, col):
        """Add symptom analysis bar chart"""
        symptoms = user_data.get('symptoms', [])
        
        if symptoms:
            # Count symptoms
            symptom_counts = pd.Series(symptoms).value_counts()
            
            fig.add_trace(go.Bar(
                x=symptom_counts.values,
                y=symptom_counts.index,
                orientation='h',
                marker_color=self.color_palette['primary']
            ), row=row, col=col)
        else:
            fig.add_trace(go.Bar(
                x=[0],
                y=['No symptoms'],
                orientation='h',
                marker_color=self.color_palette['light']
            ), row=row, col=col)
    
    def add_risk_assessment(self, fig, prediction_result, row, col):
        """Add risk assessment pie chart"""
        risk_level = prediction_result.get('risk_level', 'Medium')
        confidence = prediction_result.get('confidence', 70)
        
        # Risk levels
        risk_data = {
            'Low': 0,
            'Medium': 0,
            'High': 0
        }
        
        risk_data[risk_level] = confidence
        
        fig.add_trace(go.Pie(
            labels=list(risk_data.keys()),
            values=list(risk_data.values()),
            marker_colors=[self.color_palette['success'], self.color_palette['warning'], self.color_palette['danger']]
        ), row=row, col=col)
    
    def add_recommendations_chart(self, fig, prediction_result, row, col):
        """Add recommendations bar chart"""
        recommendations = prediction_result.get('recommendations', [])
        
        if recommendations:
            # Categorize recommendations more accurately
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
            
            # Only show categories with recommendations
            filtered_categories = {k: v for k, v in categories.items() if v > 0}
            
            if filtered_categories:
                fig.add_trace(go.Bar(
                    x=list(filtered_categories.keys()),
                    y=list(filtered_categories.values()),
                    marker_color=[self.color_palette['primary'], self.color_palette['info'], 
                                self.color_palette['warning'], self.color_palette['success'], 
                                self.color_palette['secondary']][:len(filtered_categories)],
                    text=list(filtered_categories.values()),
                    textposition='auto'
                ), row=row, col=col)
            else:
                fig.add_trace(go.Bar(
                    x=['General Care'],
                    y=[1],
                    marker_color=self.color_palette['info'],
                    text=['1'],
                    textposition='auto'
                ), row=row, col=col)
        else:
            fig.add_trace(go.Bar(
                x=['General Care'],
                y=[1],
                marker_color=self.color_palette['light'],
                text=['1'],
                textposition='auto'
            ), row=row, col=col)
    
    def create_symptom_timeline(self, user_data, prediction_result):
        """Create a symptom timeline visualization"""
        symptoms = user_data.get('symptoms', [])
        
        if not symptoms:
            return None
        
        # Create timeline data
        timeline_data = []
        for i, symptom in enumerate(symptoms):
            timeline_data.append({
                'Day': i + 1,
                'Symptom': symptom,
                'Severity': np.random.randint(1, 6),  # Random severity for demo
                'Status': 'Active'
            })
        
        df = pd.DataFrame(timeline_data)
        
        fig = px.scatter(
            df, 
            x='Day', 
            y='Severity', 
            color='Symptom',
            size='Severity',
            title='Symptom Timeline',
            labels={'Severity': 'Symptom Severity (1-5)', 'Day': 'Days Since Onset'}
        )
        
        fig.update_layout(
            template="plotly_white",
            height=400
        )
        
        return fig
    
    def create_medicine_recommendations_chart(self, medicine_recommendations):
        """Create medicine recommendations visualization"""
        if not medicine_recommendations:
            return None
        
        # Prepare data
        otc_meds = medicine_recommendations.get('over_the_counter', [])
        prescription_meds = medicine_recommendations.get('prescription', [])
        natural_remedies = medicine_recommendations.get('natural_remedies', [])
        
        # Create categories
        categories = ['Over-the-Counter', 'Prescription', 'Natural Remedies']
        counts = [len(otc_meds), len(prescription_meds), len(natural_remedies)]
        
        fig = go.Figure(data=[
            go.Bar(
                x=categories,
                y=counts,
                marker_color=[self.color_palette['info'], self.color_palette['warning'], self.color_palette['success']]
            )
        ])
        
        fig.update_layout(
            title="Medicine Recommendations by Category",
            xaxis_title="Medicine Type",
            yaxis_title="Number of Recommendations",
            template="plotly_white",
            height=400
        )
        
        return fig
    
    def create_diet_recommendations_chart(self, diet_recommendations):
        """Create diet recommendations visualization"""
        if not diet_recommendations:
            return None
        
        foods_to_eat = diet_recommendations.get('foods_to_eat', [])
        foods_to_avoid = diet_recommendations.get('foods_to_avoid', [])
        
        # Create word cloud data
        eat_data = pd.DataFrame({
            'Food': foods_to_eat,
            'Category': 'Recommended',
            'Count': [1] * len(foods_to_eat)
        })
        
        avoid_data = pd.DataFrame({
            'Food': foods_to_avoid,
            'Category': 'Avoid',
            'Count': [1] * len(foods_to_avoid)
        })
        
        combined_data = pd.concat([eat_data, avoid_data])
        
        fig = px.bar(
            combined_data,
            x='Food',
            y='Count',
            color='Category',
            title='Diet Recommendations',
            color_discrete_map={'Recommended': self.color_palette['success'], 'Avoid': self.color_palette['danger']}
        )
        
        fig.update_layout(
            template="plotly_white",
            height=400,
            xaxis_tickangle=-45
        )
        
        return fig
    
    def create_routine_schedule_chart(self, routine_data):
        """Create daily routine schedule visualization"""
        if not routine_data:
            return None
        
        # Prepare schedule data
        schedule_data = []
        time_periods = ['morning', 'afternoon', 'evening', 'night']
        
        for period in time_periods:
            activities = routine_data.get(period, [])
            for activity in activities:
                schedule_data.append({
                    'Time_Period': period.title(),
                    'Activity': activity,
                    'Duration': 60  # Default duration in minutes
                })
        
        df = pd.DataFrame(schedule_data)
        
        fig = px.bar(
            df,
            x='Time_Period',
            y='Duration',
            color='Activity',
            title='Daily Routine Schedule',
            labels={'Duration': 'Duration (minutes)', 'Time_Period': 'Time Period'}
        )
        
        fig.update_layout(
            template="plotly_white",
            height=400
        )
        
        return fig
    
    def create_health_trends_chart(self, user_data, prediction_result):
        """Create health trends over time"""
        # Simulate health trends (in real app, this would come from historical data)
        days = list(range(1, 8))
        
        # Simulate BMI trend
        bmi_trend = [user_data.get('bmi', 22) + np.random.normal(0, 0.5) for _ in days]
        
        # Simulate temperature trend
        temp_trend = [user_data.get('temperature', 36.5) + np.random.normal(0, 0.3) for _ in days]
        
        # Simulate symptom count trend
        symptom_count = len(user_data.get('symptoms', []))
        symptom_trend = [max(0, symptom_count + np.random.normal(0, 1)) for _ in days]
        
        fig = make_subplots(
            rows=3, cols=1,
            subplot_titles=('BMI Trend', 'Temperature Trend', 'Symptom Count Trend'),
            vertical_spacing=0.1
        )
        
        # BMI trend
        fig.add_trace(go.Scatter(
            x=days,
            y=bmi_trend,
            mode='lines+markers',
            name='BMI',
            line=dict(color=self.color_palette['primary'])
        ), row=1, col=1)
        
        # Temperature trend
        fig.add_trace(go.Scatter(
            x=days,
            y=temp_trend,
            mode='lines+markers',
            name='Temperature',
            line=dict(color=self.color_palette['secondary'])
        ), row=2, col=1)
        
        # Symptom count trend
        fig.add_trace(go.Scatter(
            x=days,
            y=symptom_trend,
            mode='lines+markers',
            name='Symptom Count',
            line=dict(color=self.color_palette['warning'])
        ), row=3, col=1)
        
        fig.update_layout(
            title="Health Trends (7 Days)",
            height=600,
            template="plotly_white"
        )
        
        return fig
    
    def create_risk_factors_chart(self, risk_factors):
        """Create risk factors visualization"""
        if not risk_factors:
            return None
        
        # Categorize risk factors
        categories = {
            'High': 0,
            'Medium': 0,
            'Low': 0
        }
        
        for factor in risk_factors:
            if any(word in factor.lower() for word in ['high', 'severe', 'serious']):
                categories['High'] += 1
            elif any(word in factor.lower() for word in ['medium', 'moderate']):
                categories['Medium'] += 1
            else:
                categories['Low'] += 1
        
        fig = go.Figure(data=[
            go.Pie(
                labels=list(categories.keys()),
                values=list(categories.values()),
                marker_colors=[self.color_palette['danger'], self.color_palette['warning'], self.color_palette['success']]
            )
        ])
        
        fig.update_layout(
            title="Risk Factors Distribution",
            template="plotly_white",
            height=400
        )
        
        return fig
    
    def get_bmi_color(self, bmi):
        """Get color for BMI value"""
        if bmi < 18.5:
            return self.color_palette['info']
        elif bmi < 25:
            return self.color_palette['success']
        elif bmi < 30:
            return self.color_palette['warning']
        else:
            return self.color_palette['danger']
    
    def get_temperature_color(self, temperature):
        """Get color for temperature value"""
        if temperature < 36.5:
            return self.color_palette['info']
        elif temperature < 37.5:
            return self.color_palette['success']
        elif temperature < 38.5:
            return self.color_palette['warning']
        else:
            return self.color_palette['danger']
    
    def get_bmi_status(self, bmi):
        """Get BMI status text"""
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    
    def get_temperature_status(self, temperature):
        """Get temperature status text"""
        if temperature < 36.5:
            return "Low"
        elif temperature < 37.5:
            return "Normal"
        elif temperature < 38.5:
            return "Mild Fever"
        else:
            return "High Fever"
    
    def create_summary_report(self, user_data, prediction_result, medicine_recommendations, diet_recommendations, routine_data):
        """Create a comprehensive summary report"""
        # Create summary data
        summary_data = {
            'Patient_Info': {
                'Age': user_data.get('age', 'N/A'),
                'BMI': f"{user_data.get('bmi', 0):.1f}",
                'Temperature': f"{user_data.get('temperature', 0):.1f}°C",
                'Symptoms': len(user_data.get('symptoms', []))
            },
            'Diagnosis': {
                'Predicted_Disease': prediction_result.get('predicted_disease', 'N/A'),
                'Confidence': f"{prediction_result.get('confidence', 0):.1f}%",
                'Risk_Level': prediction_result.get('risk_level', 'N/A')
            },
            'Recommendations': {
                'Medicines': len(medicine_recommendations.get('over_the_counter', [])) if medicine_recommendations else 0,
                'Diet_Items': len(diet_recommendations.get('foods_to_eat', [])) if diet_recommendations else 0,
                'Routine_Activities': len(routine_data.get('morning', [])) if routine_data else 0
            }
        }
        
        return summary_data
