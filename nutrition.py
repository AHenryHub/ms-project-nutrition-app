#bring in nutitional info for that ingredient
#import nutrition_list

ingredient = input("Enter an ingredient name: ")
nutrition_list = {}

if(nutrition_list[ingredient]!= {}):
    #ask user for macros if the ingredient is new to the dB
    calories = input("Enter the number of calories per serving: ")
    protein = input("Enter the amount of grams of protein per serving: ")
    fats = input("Enter the amount of grams of fats per serving: ")
    carbohydrates = input("Enter the amount of carbohydrates per serving: ")
    added_sugar = input("Enter the amount of added sugar per serving: ")

#lists macro nutrient quantities per serving for an ingredient (macros in grams/serving)
nutrition_list = {ingredient:{'Calories':100,'Protein':10,'Fats':5,'Carbohydrates':20,'Added Sugar':3}}

