import warnings
warnings.filterwarnings('ignore')

class RoutineGenerator:
    def __init__(self):
        self.routine_templates = self.create_routine_templates()
        self.activity_database = self.create_activity_database()
        self.sleep_requirements = self.create_sleep_requirements()
    
    def create_routine_templates(self):
        """Create routine templates for different conditions"""
        return {
            'Common Cold': {
                'morning': [
                    'Wake up at consistent time',
                    'Drink warm water with lemon',
                    'Gentle stretching or light yoga',
                    'Healthy breakfast',
                    'Take prescribed medications'
                ],
                'afternoon': [
                    'Light work or rest',
                    'Warm herbal tea',
                    'Light lunch',
                    'Short walk if feeling well',
                    'Rest or nap'
                ],
                'evening': [
                    'Light dinner',
                    'Relaxing activities (reading, music)',
                    'Warm shower or bath',
                    'Prepare for early bedtime',
                    'Take evening medications'
                ],
                'night': [
                    'Early bedtime (8-9 PM)',
                    'Use humidifier if needed',
                    'Elevate head while sleeping',
                    'Ensure 8-9 hours of sleep'
                ]
            },
            'Flu': {
                'morning': [
                    'Wake up when body feels ready',
                    'Drink electrolyte solution',
                    'Light breakfast if appetite allows',
                    'Take antiviral medication',
                    'Check temperature'
                ],
                'afternoon': [
                    'Rest in bed',
                    'Drink plenty of fluids',
                    'Light lunch or soup',
                    'Monitor symptoms',
                    'Take prescribed medications'
                ],
                'evening': [
                    'Light dinner or broth',
                    'Relaxing activities',
                    'Prepare for early sleep',
                    'Take evening medications',
                    'Ensure comfortable sleeping environment'
                ],
                'night': [
                    'Early bedtime (7-8 PM)',
                    'Use humidifier',
                    'Keep tissues and water nearby',
                    'Ensure 9-10 hours of sleep'
                ]
            },
            'Fever': {
                'morning': [
                    'Wake up naturally',
                    'Check temperature',
                    'Drink cool water',
                    'Light breakfast',
                    'Take fever-reducing medication'
                ],
                'afternoon': [
                    'Rest in cool environment',
                    'Apply cool compresses',
                    'Drink plenty of fluids',
                    'Light lunch',
                    'Monitor temperature regularly'
                ],
                'evening': [
                    'Cool shower or bath',
                    'Light dinner',
                    'Relaxing activities',
                    'Take evening medication',
                    'Prepare cool sleeping environment'
                ],
                'night': [
                    'Sleep in cool room',
                    'Use light bedding',
                    'Keep water nearby',
                    'Ensure 8-9 hours of sleep'
                ]
            },
            'Headache': {
                'morning': [
                    'Wake up gradually',
                    'Drink water immediately',
                    'Gentle neck and shoulder stretches',
                    'Light breakfast',
                    'Take pain medication if needed'
                ],
                'afternoon': [
                    'Avoid bright lights',
                    'Take breaks from screens',
                    'Light lunch',
                    'Gentle walk if possible',
                    'Apply cold compress if helpful'
                ],
                'evening': [
                    'Relaxing activities',
                    'Light dinner',
                    'Avoid triggers (caffeine, alcohol)',
                    'Prepare for early bedtime',
                    'Take evening medication if prescribed'
                ],
                'night': [
                    'Sleep in dark, quiet room',
                    'Use comfortable pillow',
                    'Ensure 7-8 hours of sleep',
                    'Keep water nearby'
                ]
            },
            'Cough': {
                'morning': [
                    'Wake up at consistent time',
                    'Drink warm water with honey',
                    'Gentle breathing exercises',
                    'Light breakfast',
                    'Take cough medication'
                ],
                'afternoon': [
                    'Use throat lozenges',
                    'Drink warm herbal tea',
                    'Light lunch',
                    'Avoid irritants (smoke, dust)',
                    'Take prescribed medications'
                ],
                'evening': [
                    'Warm shower (steam helps)',
                    'Light dinner',
                    'Relaxing activities',
                    'Use humidifier',
                    'Take evening medication'
                ],
                'night': [
                    'Sleep with head elevated',
                    'Use humidifier',
                    'Keep cough drops nearby',
                    'Ensure 8-9 hours of sleep'
                ]
            }
        }
    
    def create_activity_database(self):
        """Create database of activities suitable for different conditions"""
        return {
            'low_energy': [
                'Gentle stretching',
                'Deep breathing exercises',
                'Light reading',
                'Listening to music',
                'Meditation',
                'Warm bath',
                'Light housework'
            ],
            'moderate_energy': [
                'Short walk',
                'Light yoga',
                'Cooking simple meals',
                'Gardening (light)',
                'Art or crafts',
                'Phone calls with friends',
                'Light cleaning'
            ],
            'high_energy': [
                'Regular exercise',
                'Sports activities',
                'Hiking',
                'Dancing',
                'Swimming',
                'Cycling',
                'Intensive housework'
            ],
            'mental_activities': [
                'Reading',
                'Puzzles',
                'Learning new skills',
                'Writing',
                'Playing games',
                'Watching educational content',
                'Creative projects'
            ],
            'social_activities': [
                'Phone calls',
                'Video chats',
                'Visiting friends (if not contagious)',
                'Group activities',
                'Community events',
                'Support groups',
                'Family time'
            ]
        }
    
    def create_sleep_requirements(self):
        """Create sleep requirements by age and condition"""
        return {
            'age_groups': {
                'child': {'hours': 10, 'bedtime': '8-9 PM', 'wake_time': '6-7 AM'},
                'teen': {'hours': 9, 'bedtime': '9-10 PM', 'wake_time': '7-8 AM'},
                'adult': {'hours': 8, 'bedtime': '10-11 PM', 'wake_time': '6-7 AM'},
                'senior': {'hours': 7, 'bedtime': '9-10 PM', 'wake_time': '6-7 AM'}
            },
            'conditions': {
                'Common Cold': {'extra_hours': 1, 'quality': 'Good rest important'},
                'Flu': {'extra_hours': 2, 'quality': 'Deep sleep essential'},
                'Fever': {'extra_hours': 1, 'quality': 'Cool environment needed'},
                'Headache': {'extra_hours': 0, 'quality': 'Consistent sleep schedule'},
                'Cough': {'extra_hours': 1, 'quality': 'Elevated head position'}
            }
        }
    
    def generate_daily_routine(self, predicted_disease, user_data):
        """Generate a personalized daily routine"""
        age = user_data.get('age', 30)
        
        # Get base routine for disease
        base_routine = self.routine_templates.get(predicted_disease, self.get_general_routine())
        
        # Customize based on user data
        personalized_routine = self.customize_routine(base_routine, user_data)
        
        # Add specific activities
        activities = self.get_recommended_activities(predicted_disease, user_data)
        
        # Create sleep schedule
        sleep_schedule = self.create_sleep_schedule(age, predicted_disease)
        
        # Create meal schedule
        meal_schedule = self.create_meal_schedule(predicted_disease, user_data)
        
        # Create medication schedule
        medication_schedule = self.create_medication_schedule(predicted_disease, user_data)
        
        return {
            'disease': predicted_disease,
            'daily_routine': personalized_routine,
            'activities': activities,
            'sleep_schedule': sleep_schedule,
            'meal_schedule': meal_schedule,
            'medication_schedule': medication_schedule,
            'personalized_notes': self.get_routine_notes(user_data, predicted_disease)
        }
    
    def customize_routine(self, base_routine, user_data):
        """Customize routine based on user data"""
        age = user_data.get('age', 30)
        bmi = user_data.get('bmi', 22)
        temperature = user_data.get('temperature', 36.5)
        
        customized = {}
        
        for time_period, activities in base_routine.items():
            customized[time_period] = activities.copy()
            
            # Age-specific customizations
            if age < 18:
                customized[time_period].append('Ensure adequate nutrition for growth')
            elif age > 65:
                customized[time_period].append('Take breaks and rest as needed')
            
            # BMI-specific customizations
            if bmi > 30:
                customized[time_period].append('Include light physical activity')
            elif bmi < 18.5:
                customized[time_period].append('Focus on nutritious meals')
            
            # Temperature-specific customizations
            if temperature > 38.5:
                customized[time_period].append('Monitor temperature regularly')
                customized[time_period].append('Stay in cool environment')
        
        return customized
    
    def get_recommended_activities(self, predicted_disease, user_data):
        """Get recommended activities based on condition and user data"""
        age = user_data.get('age', 30)
        self.assess_energy_level(predicted_disease, user_data)
        
        activities = {
            'low_energy': self.activity_database['low_energy'],
            'moderate_energy': self.activity_database['moderate_energy'],
            'mental_activities': self.activity_database['mental_activities'],
            'social_activities': self.activity_database['social_activities']
        }
        
        # Customize based on age
        if age < 18:
            activities['low_energy'].extend(['Coloring', 'Simple games', 'Story time'])
            activities['moderate_energy'].extend(['Playground activities', 'Art projects'])
        elif age > 65:
            activities['low_energy'].extend(['Gentle chair exercises', 'Crossword puzzles'])
            activities['moderate_energy'].extend(['Walking', 'Gardening'])
        
        return activities
    
    def assess_energy_level(self, predicted_disease, user_data):
        """Assess energy level based on condition and symptoms"""
        temperature = user_data.get('temperature', 36.5)
        symptoms = user_data.get('symptoms', [])
        
        energy_score = 5  # Base energy level (1-10)
        
        # Temperature impact
        if temperature > 38.5:
            energy_score -= 3
        elif temperature > 37.5:
            energy_score -= 2
        
        # Symptom impact
        fatigue_symptoms = ['fatigue', 'weakness', 'lethargy', 'tiredness']
        for symptom in symptoms:
            if any(fatigue in symptom.lower() for fatigue in fatigue_symptoms):
                energy_score -= 2
        
        # Disease-specific impact
        if 'flu' in predicted_disease.lower():
            energy_score -= 2
        elif 'cold' in predicted_disease.lower():
            energy_score -= 1
        
        return max(1, min(10, energy_score))
    
    def create_sleep_schedule(self, age, predicted_disease):
        """Create personalized sleep schedule"""
        age_group = self.get_age_group(age)
        sleep_reqs = self.sleep_requirements['age_groups'][age_group]
        condition_reqs = self.sleep_requirements['conditions'].get(predicted_disease, {})
        
        # Calculate total sleep hours
        base_hours = sleep_reqs['hours']
        extra_hours = condition_reqs.get('extra_hours', 0)
        total_hours = base_hours + extra_hours
        
        # Ensure total hours is reasonable
        if total_hours < 6:
            total_hours = 7
        elif total_hours > 12:
            total_hours = 9
        
        return {
            'bedtime': sleep_reqs['bedtime'],
            'wake_time': sleep_reqs['wake_time'],
            'total_hours': total_hours,
            'quality_tips': condition_reqs.get('quality', 'Maintain consistent sleep schedule'),
            'special_considerations': self.get_sleep_considerations(predicted_disease)
        }
    
    def create_meal_schedule(self, predicted_disease, user_data):
        """Create personalized meal schedule"""
        age = user_data.get('age', 30)
        
        base_schedule = {
            'breakfast': '7:00-8:00 AM',
            'morning_snack': '10:00-10:30 AM',
            'lunch': '12:00-1:00 PM',
            'afternoon_snack': '3:00-3:30 PM',
            'dinner': '6:00-7:00 PM',
            'evening_snack': '8:00-8:30 PM (if needed)'
        }
        
        # Customize based on condition
        if 'flu' in predicted_disease.lower():
            base_schedule['breakfast'] = 'When appetite allows'
            base_schedule['lunch'] = 'Light soup or broth'
            base_schedule['dinner'] = 'Early dinner (5:00-6:00 PM)'
        
        # Customize based on age
        if age < 18:
            base_schedule['morning_snack'] = '9:30-10:00 AM'
            base_schedule['afternoon_snack'] = '2:30-3:00 PM'
        elif age > 65:
            base_schedule['breakfast'] = '8:00-9:00 AM'
            base_schedule['dinner'] = '5:00-6:00 PM'
        
        return base_schedule
    
    def create_medication_schedule(self, predicted_disease, user_data):
        """Create medication schedule"""
        age = user_data.get('age', 30)
        
        schedule = {
            'morning': 'With breakfast (8:00 AM)',
            'afternoon': 'With lunch (12:00 PM)',
            'evening': 'With dinner (6:00 PM)',
            'bedtime': 'Before sleep (9:00 PM)'
        }
        
        # Customize based on age
        if age < 18:
            schedule['morning'] = 'With breakfast (7:30 AM)'
            schedule['bedtime'] = 'Before sleep (8:30 PM)'
        elif age > 65:
            schedule['morning'] = 'With breakfast (8:30 AM)'
            schedule['bedtime'] = 'Before sleep (9:30 PM)'
        
        return schedule
    
    def get_sleep_considerations(self, predicted_disease):
        """Get sleep considerations for specific conditions"""
        considerations = {
            'Common Cold': [
                'Use humidifier to ease congestion',
                'Elevate head with extra pillow',
                'Keep tissues and water nearby'
            ],
            'Flu': [
                'Ensure comfortable temperature',
                'Use humidifier',
                'Keep medications nearby',
                'Have emergency contact ready'
            ],
            'Fever': [
                'Sleep in cool room',
                'Use light bedding',
                'Keep thermometer nearby',
                'Monitor temperature during night'
            ],
            'Headache': [
                'Sleep in dark, quiet room',
                'Use comfortable pillow',
                'Avoid triggers before bed',
                'Keep pain medication nearby'
            ],
            'Cough': [
                'Sleep with head elevated',
                'Use humidifier',
                'Keep cough drops nearby',
                'Avoid dry air'
            ]
        }
        
        return considerations.get(predicted_disease, [
            'Maintain consistent sleep schedule',
            'Create comfortable sleeping environment',
            'Avoid screens before bedtime'
        ])
    
    def get_routine_notes(self, user_data, predicted_disease):
        """Get personalized notes for the routine"""
        notes = []
        
        age = user_data.get('age', 30)
        bmi = user_data.get('bmi', 22)
        temperature = user_data.get('temperature', 36.5)
        
        # Age-specific notes
        if age < 18:
            notes.append("Ensure adequate nutrition for growth and development")
            notes.append("Include age-appropriate activities")
        elif age > 65:
            notes.append("Take breaks and rest as needed")
            notes.append("Focus on gentle activities")
        
        # BMI-specific notes
        if bmi > 30:
            notes.append("Include light physical activity when feeling well")
            notes.append("Focus on portion control at meals")
        elif bmi < 18.5:
            notes.append("Ensure adequate caloric intake")
            notes.append("Include nutrient-dense foods")
        
        # Temperature-specific notes
        if temperature > 38.5:
            notes.append("Monitor temperature regularly")
            notes.append("Stay in cool environment")
            notes.append("Seek medical attention if fever persists")
        
        # General notes
        notes.append("Listen to your body and adjust activities as needed")
        notes.append("Stay hydrated throughout the day")
        notes.append("Get adequate rest and sleep")
        notes.append("Consult healthcare provider if symptoms worsen")
        
        return notes
    
    def get_age_group(self, age):
        """Determine age group for sleep requirements"""
        if age < 13:
            return 'child'
        elif age < 20:
            return 'teen'
        elif age < 65:
            return 'adult'
        else:
            return 'senior'
    
    def get_general_routine(self):
        """Get general routine when disease is not in database"""
        return {
            'morning': [
                'Wake up at consistent time',
                'Drink water',
                'Light stretching',
                'Healthy breakfast',
                'Take prescribed medications'
            ],
            'afternoon': [
                'Light work or activities',
                'Healthy lunch',
                'Short walk if feeling well',
                'Rest or relaxation'
            ],
            'evening': [
                'Light dinner',
                'Relaxing activities',
                'Prepare for bedtime',
                'Take evening medications'
            ],
            'night': [
                'Consistent bedtime',
                'Ensure 7-8 hours of sleep',
                'Create comfortable sleeping environment'
            ]
        }
