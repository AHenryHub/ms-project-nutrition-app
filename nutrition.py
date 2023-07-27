from flask import Flask
import query_db
import submit_db_entry

def macros(recipeid):
    nutrition_list = {}

    recipe = query_db.query_db(recipeid)

    #ask user for macros if the ingredient is new to the dB
    calories = input("Enter the number of calories per serving: ")
    protein = input("Enter the amount of grams of protein per serving: ")
    fats = input("Enter the amount of grams of fats per serving: ")
    carbohydrates = input("Enter the amount of carbohydrates per serving: ")
    added_sugar = input("Enter the amount of added sugar per serving: ")

    #lists macro nutrient quantities per serving for an ingredient (macros in grams/serving)
    nutrition_list = {'calories':int(calories),'protein':int(protein),'fats':int(fats),'carbohydrates':int(carbohydrates),'added sugar':int(added_sugar)}

    #updates the values in db.json
    recipe["nutrients"] = nutrition_list    
    submit_db_entry.resubmit(recipe, recipeid)


macros(1)