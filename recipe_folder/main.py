from flask import Flask
import tkinter as tk
from tkinter import messagebox
import  price_estimate, submit_db_entry


class RecipeInput(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Recipe Builder")
        self.recipeNameVar = tk.StringVar()
        self.ingredientsVar = tk.StringVar()
        self.caloriesVar = tk.StringVar()
        self.proteinVar = tk.StringVar()
        self.carbsVar = tk.StringVar()
        self.fatsVar = tk.StringVar()
        self.sugarVar = tk.StringVar()
   

        tk.Label(self, text="Recipe Name").grid(row=1, column=0)
        tk.Entry(self, textvariable=self.recipeNameVar).grid(row=1, column=1)

        tk.Label(self, text="Ingredients (seperate with comma)").grid(row=2, column=0)
        tk.Entry(self, textvariable=self.ingredientsVar).grid(row=2, column=1)

        tk.Label(self, text="Calories").grid(row=3, column=0)
        tk.Entry(self, textvariable=self.caloriesVar).grid(row=3, column=1)

        tk.Label(self, text="Protein").grid(row=4, column=0)
        tk.Entry(self, textvariable=self.proteinVar).grid(row=4, column=1)

        tk.Label(self, text="Carbs").grid(row=5, column=0)
        tk.Entry(self, textvariable=self.carbsVar).grid(row=5, column=1)

        tk.Label(self, text="Fats").grid(row=6, column=0)
        tk.Entry(self, textvariable=self.fatsVar).grid(row=6, column=1)

        tk.Label(self, text="Sugar").grid(row=7, column=0)
        tk.Entry(self, textvariable=self.sugarVar).grid(row=7, column=1)



        tk.Button(self, text="Submit", command=self.submit).grid(row=9, column=1)
    
    def submit(self):
        recipe = {
            "recipeid": 0,
            "name": self.recipeNameVar.get(),
            "ingredients": {str(i+1): ingredient for i, ingredient in enumerate(self.ingredientsVar.get().split(','))},
            "nutrients": {
                "calories": self.caloriesVar.get(),
                "protein": self.proteinVar.get(),
                "carbs": self.carbsVar.get(),
                "fats": self.fatsVar.get(),
                "added sugar": self.sugarVar.get()
            },
            "price": price_estimate.prices()
        }

        messagebox.showinfo("Recipe", recipe)
        submit_db_entry.submit(recipe)


app = RecipeInput()
app.mainloop()