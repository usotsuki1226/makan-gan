import tkinter as tk
from tkinter import messagebox, Checkbutton, IntVar, Toplevel
import random
import json
from PIL import ImageTk, Image

def load_recipes(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def display_recipes():
    selected = [cuisine for cuisine, var in selected_cuisines.items() if var.get() == 1]
    
    if not selected:
        messagebox.showerror("Error", "Sorry, there are no recipes listed in your preferred continent.")
        return

    matched_recipes = []
    for cuisine in selected:
        for recipe in recipes[cuisine]["recipes"]:
            if all(ingredient in recipe["ingredients"] for ingredient in ingredient_list):
                matched_recipes.append((recipe["name"], recipe["ingredients"], cuisine))

    if matched_recipes:
        for name, ingredients, cuisine in matched_recipes:
            show_recipe_with_image(name, ingredients, cuisine)
    else:
        messagebox.showerror("Error", "No recipes match the ingredients you've entered.")

def show_recipe_with_image(name, ingredients, cuisine):
    recipe_window = Toplevel(root)
    recipe_window.title(name)
    image_path = cuisine_images[cuisine]
    image = Image.open(image_path)
    image = image.resize((100, 100), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(recipe_window, image=photo)
    image_label.image = photo
    image_label.pack(pady=10)
    recipe_text = f"Recipe: {name}\n\nIngredients: {', '.join(ingredients)}"
    recipe_label = tk.Label(recipe_window, text=recipe_text, font=("Arial", 12), justify="left")
    recipe_label.pack(pady=10)
    close_button = tk.Button(recipe_window, text="Close", command=recipe_window.destroy)
    close_button.pack(pady=10)

def save_ingredients():
    ingredient = ingredient_entry.get().strip().lower()
    if ingredient:
        ingredient_list.append(ingredient)
        ingredient_entry.delete(0, tk.END)
    refresh_ingredients()

def refresh_ingredients():
    ingredients_label.config(text="Ingredients: " + ", ".join(ingredient_list))
    ingredients_label.pack()

def input_cuisines():
    cuisine_window.pack(fill="both", expand=True)
    main_menu.pack_forget()

def reset_app():
    for var in selected_cuisines.values():
        var.set(0)
    ingredient_list.clear()
    refresh_ingredients()
    cuisine_window.pack_forget()
    main_menu.pack(fill="both", expand=True)

def random_recipe():
    random_cuisine = random.choice(list(recipes.keys()))
    random_recipe = random.choice(recipes[random_cuisine]["recipes"])
    show_recipe_with_image(random_recipe['name'], random_recipe['ingredients'], random_cuisine)

def remove_ingredients():
    global remove_window
    remove_window = Toplevel(root)
    remove_window.title("Remove Ingredients")
    
    selected_for_removal.clear()
    
    for ingredient in ingredient_list:
        var = IntVar()
        checkbox = Checkbutton(remove_window, text=ingredient, variable=var, bg=bg_color, fg=fg_color, selectcolor=bg_color)
        checkbox.pack(anchor="w")
        selected_for_removal[ingredient] = var
    

    confirm_button = tk.Button(remove_window, text="Remove Selected Ingredients", command=confirm_removal, bg=button_bg, fg=fg_color)
    confirm_button.pack(pady=10)

def confirm_removal():
    global remove_window
    for ingredient, var in selected_for_removal.items():
        if var.get() == 1:
            ingredient_list.remove(ingredient)
    refresh_ingredients()
    remove_window.destroy()

root = tk.Tk()
root.iconbitmap("f:/nyamnyam/sombrero.ico")
root.title("Sombrero")
root.geometry("400x600")

bg_color = "black"
fg_color = "white"
button_bg = "gray"
root.configure(bg=bg_color)

recipes = load_recipes('F:/nyamnyam/ingredients.json')

ingredient_list = []
selected_for_removal = {}  

cuisine_images = {
    "Mexican": "f:/nyamnyam/taco.png",
    "American": "f:/nyamnyam/burger.png",
    "Italian": "f:/nyamnyam/pasta.png",
    "Asian": "f:/nyamnyam/nasi.png"
}

selected_cuisines = {cuisine: IntVar() for cuisine in recipes}

main_menu = tk.Frame(root, bg=bg_color)
main_menu.pack(fill="both", expand=True)

tk.Label(main_menu, text="Welcome to NyamNyam!", font=("Arial", 16), bg=bg_color, fg=fg_color).pack(pady=10)
tk.Button(main_menu, text="Select Cuisines & Input Ingredients", command=input_cuisines, bg=button_bg, fg=fg_color).pack(pady=5)
tk.Button(main_menu, text="Get Random Recipe", command=random_recipe, bg=button_bg, fg=fg_color).pack(pady=5)
tk.Button(main_menu, text="Exit", command=root.quit, bg=button_bg, fg=fg_color).pack(pady=5)

cuisine_window = tk.Frame(root, bg=bg_color)

cuisines = ["American", "Italian", "Asian", "Mexican"]

for idx, cuisine in enumerate(cuisines):
    cuisine_frame = tk.Frame(cuisine_window, bg=bg_color)
    cuisine_frame.pack(anchor="w")
    Checkbutton(
        cuisine_frame, text=cuisine, variable=selected_cuisines[cuisine], onvalue=1, offvalue=0,
        bg=bg_color, fg=fg_color, selectcolor=bg_color
    ).pack(side="left", padx=5)

tk.Button(cuisine_window, text="Show Recipes", command=display_recipes, bg=button_bg, fg=fg_color).pack(pady=10)

ingredients_label = tk.Label(cuisine_window, text="Ingredients: ", font=("Arial", 12), bg=bg_color, fg=fg_color)
ingredients_label.pack(pady=10)

ingredient_entry = tk.Entry(cuisine_window, width=30, bg=button_bg, fg=fg_color)
ingredient_entry.pack(pady=5)

tk.Button(cuisine_window, text="Add Ingredient", command=save_ingredients, bg=button_bg, fg=fg_color).pack(pady=5)
tk.Button(cuisine_window, text="Remove Ingredient", command=remove_ingredients, bg=button_bg, fg=fg_color).pack(pady=5)
tk.Button(cuisine_window, text="Cancel", command=reset_app, bg=button_bg, fg=fg_color).pack(pady=5)

root.mainloop()
