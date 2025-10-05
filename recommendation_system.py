import warnings
warnings.filterwarnings('ignore')

class RecommendationSystem:
    def __init__(self):
        self.medicine_database = self.create_medicine_database()
        self.diet_database = self.create_diet_database()
        self.nutritional_requirements = self.create_nutritional_requirements()
    
    def create_medicine_database(self):
        """Create a comprehensive medicine database"""
        return {
            'Common Cold': {
                'over_the_counter': [
                    {'name': 'Ibuprofen', 'dosage': '200-400mg every 6-8 hours', 'purpose': 'Pain relief and fever reduction'},
                    {'name': 'Acetaminophen', 'dosage': '500-1000mg every 6 hours', 'purpose': 'Fever and pain relief'},
                    {'name': 'Pseudoephedrine', 'dosage': '30-60mg every 4-6 hours', 'purpose': 'Nasal decongestant'},
                    {'name': 'Dextromethorphan', 'dosage': '15-30mg every 4-6 hours', 'purpose': 'Cough suppressant'}
                ],
                'prescription': [
                    {'name': 'Amoxicillin', 'dosage': '500mg every 8 hours', 'purpose': 'Antibiotic for bacterial infections'},
                    {'name': 'Azithromycin', 'dosage': '500mg once daily', 'purpose': 'Broad-spectrum antibiotic'}
                ],
                'natural_remedies': [
                    'Honey and lemon tea',
                    'Ginger tea',
                    'Echinacea supplements',
                    'Vitamin C supplements',
                    'Zinc lozenges'
                ]
            },
            'Flu': {
                'over_the_counter': [
                    {'name': 'Oseltamivir (Tamiflu)', 'dosage': '75mg twice daily', 'purpose': 'Antiviral medication'},
                    {'name': 'Ibuprofen', 'dosage': '400-600mg every 6-8 hours', 'purpose': 'Pain and fever relief'},
                    {'name': 'Acetaminophen', 'dosage': '650-1000mg every 6 hours', 'purpose': 'Fever reduction'}
                ],
                'prescription': [
                    {'name': 'Oseltamivir', 'dosage': '75mg twice daily for 5 days', 'purpose': 'Antiviral treatment'},
                    {'name': 'Zanamivir', 'dosage': '10mg twice daily for 5 days', 'purpose': 'Inhalation antiviral'}
                ],
                'natural_remedies': [
                    'Elderberry syrup',
                    'Echinacea tea',
                    'Garlic supplements',
                    'Probiotics',
                    'Vitamin D supplements'
                ]
            },
            'Fever': {
                'over_the_counter': [
                    {'name': 'Acetaminophen', 'dosage': '500-1000mg every 6 hours', 'purpose': 'Fever reduction'},
                    {'name': 'Ibuprofen', 'dosage': '200-400mg every 6-8 hours', 'purpose': 'Anti-inflammatory and fever reduction'},
                    {'name': 'Aspirin', 'dosage': '325-650mg every 4 hours', 'purpose': 'Fever and pain relief (adults only)'}
                ],
                'prescription': [
                    {'name': 'Acetaminophen with Codeine', 'dosage': 'As prescribed', 'purpose': 'Severe pain and fever'},
                    {'name': 'Naproxen', 'dosage': '220-440mg every 8-12 hours', 'purpose': 'Anti-inflammatory'}
                ],
                'natural_remedies': [
                    'Cool compresses',
                    'Lukewarm baths',
                    'Stay hydrated',
                    'Rest in cool environment',
                    'Herbal teas (peppermint, chamomile)'
                ]
            },
            'Headache': {
                'over_the_counter': [
                    {'name': 'Ibuprofen', 'dosage': '200-400mg every 6-8 hours', 'purpose': 'Pain relief'},
                    {'name': 'Acetaminophen', 'dosage': '500-1000mg every 6 hours', 'purpose': 'Headache relief'},
                    {'name': 'Aspirin', 'dosage': '325-650mg every 4 hours', 'purpose': 'Pain relief (adults only)'}
                ],
                'prescription': [
                    {'name': 'Sumatriptan', 'dosage': '25-100mg as needed', 'purpose': 'Migraine treatment'},
                    {'name': 'Naproxen', 'dosage': '220-440mg every 8-12 hours', 'purpose': 'Anti-inflammatory pain relief'}
                ],
                'natural_remedies': [
                    'Apply cold compress to forehead',
                    'Massage temples gently',
                    'Stay hydrated',
                    'Avoid bright lights',
                    'Relaxation techniques'
                ]
            },
            'Cough': {
                'over_the_counter': [
                    {'name': 'Dextromethorphan', 'dosage': '15-30mg every 4-6 hours', 'purpose': 'Cough suppressant'},
                    {'name': 'Guaifenesin', 'dosage': '200-400mg every 4 hours', 'purpose': 'Expectorant'},
                    {'name': 'Benzonatate', 'dosage': '100-200mg three times daily', 'purpose': 'Cough suppressant'}
                ],
                'prescription': [
                    {'name': 'Codeine', 'dosage': '10-20mg every 4-6 hours', 'purpose': 'Severe cough suppression'},
                    {'name': 'Hydrocodone', 'dosage': '5-10mg every 4-6 hours', 'purpose': 'Cough and pain relief'}
                ],
                'natural_remedies': [
                    'Honey (1-2 teaspoons)',
                    'Throat lozenges',
                    'Steam inhalation',
                    'Warm salt water gargle',
                    'Herbal teas (thyme, licorice)'
                ]
            }
        }
    
    def create_diet_database(self):
        """Create a comprehensive diet database"""
        return {
            'Common Cold': {
                'foods_to_eat': [
                    'Chicken soup (anti-inflammatory properties)',
                    'Citrus fruits (high in vitamin C)',
                    'Garlic (immune-boosting)',
                    'Ginger tea (soothing)',
                    'Honey (natural cough suppressant)',
                    'Green leafy vegetables',
                    'Berries (antioxidants)',
                    'Yogurt (probiotics)'
                ],
                'foods_to_avoid': [
                    'Dairy products (may increase mucus)',
                    'Sugary foods (suppress immune system)',
                    'Processed foods',
                    'Alcohol (dehydrating)',
                    'Caffeinated beverages (dehydrating)'
                ],
                'hydration': '8-10 glasses of water daily, herbal teas, warm broths'
            },
            'Flu': {
                'foods_to_eat': [
                    'Clear broths and soups',
                    'Bananas (easy to digest)',
                    'Rice (bland, easy on stomach)',
                    'Applesauce (vitamins and easy digestion)',
                    'Toast (bland carbohydrates)',
                    'Ginger (nausea relief)',
                    'Chamomile tea (calming)',
                    'Electrolyte drinks'
                ],
                'foods_to_avoid': [
                    'Spicy foods',
                    'Greasy or fried foods',
                    'Dairy products',
                    'Raw vegetables',
                    'Alcohol',
                    'Caffeinated beverages'
                ],
                'hydration': 'Frequent small sips of water, electrolyte solutions, herbal teas'
            },
            'Fever': {
                'foods_to_eat': [
                    'Cool, refreshing foods',
                    'Watermelon (high water content)',
                    'Cucumber (hydrating)',
                    'Coconut water (electrolytes)',
                    'Plain yogurt (probiotics)',
                    'Soft fruits (bananas, apples)',
                    'Clear soups',
                    'Ice chips or popsicles'
                ],
                'foods_to_avoid': [
                    'Hot, spicy foods',
                    'Heavy, rich meals',
                    'Alcohol',
                    'Caffeinated beverages',
                    'Sugary foods'
                ],
                'hydration': 'Plenty of cool fluids, electrolyte drinks, ice chips'
            },
            'Headache': {
                'foods_to_eat': [
                    'Magnesium-rich foods (spinach, almonds)',
                    'Water (dehydration can cause headaches)',
                    'Ginger (anti-inflammatory)',
                    'Peppermint tea (calming)',
                    'Dark chocolate (in moderation)',
                    'Nuts and seeds',
                    'Leafy greens',
                    'Whole grains'
                ],
                'foods_to_avoid': [
                    'Caffeine (can trigger headaches)',
                    'Alcohol',
                    'Processed meats (nitrates)',
                    'Aged cheeses (tyramine)',
                    'Artificial sweeteners',
                    'MSG (monosodium glutamate)'
                ],
                'hydration': 'Consistent water intake throughout the day'
            },
            'Cough': {
                'foods_to_eat': [
                    'Honey (natural cough suppressant)',
                    'Warm herbal teas',
                    'Throat-soothing foods',
                    'Soft, easy-to-swallow foods',
                    'Warm broths',
                    'Mashed potatoes',
                    'Oatmeal',
                    'Smoothies'
                ],
                'foods_to_avoid': [
                    'Spicy foods (can irritate throat)',
                    'Acidic foods (citrus, tomatoes)',
                    'Dry, crunchy foods',
                    'Alcohol',
                    'Very hot or very cold foods'
                ],
                'hydration': 'Warm fluids, throat lozenges, humidifier use'
            }
        }
    
    def create_nutritional_requirements(self):
        """Create nutritional requirements by age and condition"""
        return {
            'child': {
                'calories': '1200-2000',
                'protein': '1.2g per kg body weight',
                'vitamins': ['Vitamin C', 'Vitamin D', 'B-complex'],
                'minerals': ['Iron', 'Calcium', 'Zinc']
            },
            'adult': {
                'calories': '1800-2500',
                'protein': '0.8-1.0g per kg body weight',
                'vitamins': ['Vitamin C', 'Vitamin D', 'B-complex', 'Vitamin E'],
                'minerals': ['Iron', 'Calcium', 'Magnesium', 'Zinc']
            },
            'senior': {
                'calories': '1600-2200',
                'protein': '1.0-1.2g per kg body weight',
                'vitamins': ['Vitamin D', 'B12', 'Folate', 'Vitamin C'],
                'minerals': ['Calcium', 'Iron', 'Zinc', 'Magnesium']
            }
        }
    
    def get_medicine_recommendations(self, predicted_disease, user_data):
        """Get personalized medicine recommendations"""
        if predicted_disease not in self.medicine_database:
            return self.get_general_medicine_recommendations(user_data)
        
        disease_medicines = self.medicine_database[predicted_disease]
        recommendations = {
            'disease': predicted_disease,
            'over_the_counter': disease_medicines['over_the_counter'],
            'prescription': disease_medicines['prescription'],
            'natural_remedies': disease_medicines['natural_remedies'],
            'personalized_notes': self.get_personalized_medicine_notes(user_data, predicted_disease)
        }
        
        return recommendations
    
    def get_diet_recommendations(self, predicted_disease, user_data):
        """Get personalized diet recommendations"""
        if predicted_disease not in self.diet_database:
            return self.get_general_diet_recommendations(user_data)
        
        disease_diet = self.diet_database[predicted_disease]
        age_group = self.get_age_group(user_data.get('age', 30))
        nutritional_reqs = self.nutritional_requirements.get(age_group, self.nutritional_requirements['adult'])
        
        recommendations = {
            'disease': predicted_disease,
            'foods_to_eat': disease_diet['foods_to_eat'],
            'foods_to_avoid': disease_diet['foods_to_avoid'],
            'hydration': disease_diet['hydration'],
            'nutritional_requirements': nutritional_reqs,
            'meal_plan': self.create_meal_plan(predicted_disease, user_data),
            'personalized_notes': self.get_personalized_diet_notes(user_data, predicted_disease)
        }
        
        return recommendations
    
    def create_meal_plan(self, predicted_disease, user_data):
        """Create a personalized meal plan"""
        age = user_data.get('age', 30)
        
        # Base meal plan
        meal_plan = {
            'breakfast': [
                'Oatmeal with honey and berries',
                'Greek yogurt with granola',
                'Scrambled eggs with toast'
            ],
            'lunch': [
                'Chicken soup with vegetables',
                'Grilled chicken salad',
                'Quinoa bowl with vegetables'
            ],
            'dinner': [
                'Baked fish with steamed vegetables',
                'Lentil soup with whole grain bread',
                'Stir-fried vegetables with rice'
            ],
            'snacks': [
                'Fresh fruits',
                'Nuts and seeds',
                'Herbal tea with honey'
            ]
        }
        
        # Customize based on disease
        if 'cold' in predicted_disease.lower():
            meal_plan['breakfast'] = ['Warm oatmeal with honey', 'Chicken soup', 'Herbal tea']
            meal_plan['lunch'] = ['Chicken soup with vegetables', 'Warm vegetable soup', 'Broth-based soup']
        
        # Customize based on age
        if age < 18:
            meal_plan['snacks'].append('Milk or fortified plant milk')
        elif age > 65:
            meal_plan['snacks'].append('Soft fruits and yogurt')
        
        return meal_plan
    
    def get_personalized_medicine_notes(self, user_data, predicted_disease):
        """Get personalized notes for medicine recommendations"""
        notes = []
        
        age = user_data.get('age', 30)
        bmi = user_data.get('bmi', 22)
        temperature = user_data.get('temperature', 36.5)
        
        # Age-specific notes
        if age < 18:
            notes.append("Consult pediatrician before giving any medication to children")
            notes.append("Use age-appropriate dosages")
        elif age > 65:
            notes.append("Consider potential drug interactions with existing medications")
            notes.append("Start with lower dosages due to slower metabolism")
        
        # BMI-specific notes
        if bmi > 30:
            notes.append("Some medications may need dosage adjustment for body weight")
        elif bmi < 18.5:
            notes.append("Monitor for medication sensitivity due to lower body weight")
        
        # Temperature-specific notes
        if temperature > 38.5:
            notes.append("High fever - consider immediate medical attention")
            notes.append("Use fever-reducing medications as directed")
        
        # General notes
        notes.append("Always read medication labels and follow instructions")
        notes.append("Consult healthcare provider if symptoms worsen")
        notes.append("Discontinue use if allergic reactions occur")
        
        return notes
    
    def get_personalized_diet_notes(self, user_data, predicted_disease):
        """Get personalized notes for diet recommendations"""
        notes = []
        
        age = user_data.get('age', 30)
        bmi = user_data.get('bmi', 22)
        gender = user_data.get('gender', 'Unknown')
        
        # Age-specific notes
        if age < 18:
            notes.append("Ensure adequate nutrition for growth and development")
            notes.append("Include calcium-rich foods for bone health")
        elif age > 65:
            notes.append("Focus on nutrient-dense foods")
            notes.append("Consider vitamin D and B12 supplements")
        
        # BMI-specific notes
        if bmi > 30:
            notes.append("Focus on portion control and nutrient-dense foods")
            notes.append("Include more fiber and lean proteins")
        elif bmi < 18.5:
            notes.append("Increase caloric intake with healthy foods")
            notes.append("Include healthy fats and proteins")
        
        # Gender-specific notes
        if gender.lower() == 'female':
            notes.append("Ensure adequate iron intake")
            notes.append("Consider folic acid if of childbearing age")
        
        # General notes
        notes.append("Stay hydrated throughout the day")
        notes.append("Eat small, frequent meals if appetite is low")
        notes.append("Listen to your body's hunger and fullness cues")
        
        return notes
    
    def get_general_medicine_recommendations(self, user_data):
        """Get general medicine recommendations when disease is not in database"""
        return {
            'disease': 'General Illness',
            'over_the_counter': [
                {'name': 'Acetaminophen', 'dosage': '500-1000mg every 6 hours', 'purpose': 'Pain and fever relief'},
                {'name': 'Ibuprofen', 'dosage': '200-400mg every 6-8 hours', 'purpose': 'Anti-inflammatory and pain relief'}
            ],
            'prescription': [
                {'name': 'Consult healthcare provider', 'dosage': 'As prescribed', 'purpose': 'Proper diagnosis and treatment'}
            ],
            'natural_remedies': [
                'Rest and adequate sleep',
                'Stay hydrated',
                'Warm herbal teas',
                'Gentle exercise if feeling well'
            ],
            'personalized_notes': [
                'Consult healthcare provider for proper diagnosis',
                'Monitor symptoms closely',
                'Get adequate rest and nutrition'
            ]
        }
    
    def get_general_diet_recommendations(self, user_data):
        """Get general diet recommendations when disease is not in database"""
        return {
            'disease': 'General Illness',
            'foods_to_eat': [
                'Fresh fruits and vegetables',
                'Lean proteins (chicken, fish, beans)',
                'Whole grains',
                'Healthy fats (nuts, olive oil)',
                'Plenty of water'
            ],
            'foods_to_avoid': [
                'Processed foods',
                'Excessive sugar',
                'Alcohol',
                'Caffeinated beverages in excess'
            ],
            'hydration': '8-10 glasses of water daily',
            'nutritional_requirements': self.nutritional_requirements['adult'],
            'meal_plan': {
                'breakfast': ['Oatmeal with fruits', 'Greek yogurt with granola', 'Whole grain toast with avocado'],
                'lunch': ['Grilled chicken salad', 'Quinoa bowl', 'Vegetable soup'],
                'dinner': ['Baked fish with vegetables', 'Lentil curry with rice', 'Stir-fried vegetables'],
                'snacks': ['Fresh fruits', 'Nuts', 'Herbal tea']
            },
            'personalized_notes': [
                'Maintain balanced nutrition',
                'Stay hydrated',
                'Listen to your body\'s needs'
            ]
        }
    
    def get_age_group(self, age):
        """Determine age group for nutritional requirements"""
        if age < 18:
            return 'child'
        elif age > 65:
            return 'senior'
        else:
            return 'adult'
