# Nutrition Calculator
# A simple python application used to calculate nutrition information
# Used to benchmark the 'pytest' testing framework
# Author: Ryan Rasti

class Calculator:
    """The Nutrition Calculator"""

    def __init__(self):
        self.total_calories = 0
        self.macronutrients = {
            'protein': 0,
            'carbohydrate': 0,
            'fat': 0
        }
        self.meals_eaten_today = []

    def calculate_total_calories(self):
        protein_calories = 0
        carbohydrate_calories = 0
        fat_calories = 0

        if self.macronutrients['protein'] != 0:
            protein_calories = self.macronutrients['protein'] * 4
        if self.macronutrients['carbohydrate'] != 0:
            carbohydrate_calories = self.macronutrients['carbohydrate'] * 4
        if self.macronutrients['fat'] != 0:
            fat_calories = self.macronutrients['fat'] * 9

        self.total_calories = protein_calories + carbohydrate_calories + fat_calories
        print(f'Total calories based on current macros: {self.total_calories}')
        return self.total_calories

    def log_meal(self, meal_name, protein, carbohydrate, fat):
        v = [meal_name, protein, carbohydrate, fat]
        for i in v:
            if i is None:
                raise Exception(f"None value encountered for {i}")
            
        self.meals_eaten_today.append(meal_name)
        self.macronutrients['protein'] += protein
        self.macronutrients['carbohydrate'] += carbohydrate
        self.macronutrients['fat'] += fat

        print(f'Meal: {meal_name} added.')
        self.calculate_total_calories()