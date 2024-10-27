import tkinter as tk
import random
import webbrowser
from PIL import Image, ImageTk  # Import the necessary libraries for image handling

window = tk.Tk()
window.title('My Recipe Selector')
window.geometry('400x400')
window.iconbitmap(r"F:\nyamnyam\sombrero.ico")

# Load the background image
background_image = Image.open("F:/nyamnyam/justindisini.png")
background_image = background_image.resize((400, 400), Image.ANTIALIAS)  # Resize to fit the window
bg_image = ImageTk.PhotoImage(background_image)

# Create a Label widget to display the background image
bg_label = tk.Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Make it fill the window

label_font = ("Arial", 12)
l = tk.Label(window, bg='white', width=100, text='Select Ingredients')
l.pack()

ingredients = ["onion", "garlic", "rice", "egg", "chicken", "pepper", 
               "tomato", "carrot"]
cuisines = ["All", "Asian", "American"]
recipes = {
    "nasgor": {
        "ingredients": ["onion", "garlic", "rice", "egg"], 
        "cuisine": "Asian",
        "link": "https://www.youtube.com/watch?v=zZNhVv7fmSE"
    },
    "fried rice": {
        "ingredients": ["onion", "garlic", "rice", "egg", "chicken"], 
        "cuisine": "Asian",
        "link": "https://www.youtube.com/watch?v=zZNhVv7fmSE"
    },
    "vegetable stir-fry": {
        "ingredients": ["pepper", "carrot", "tomato"], 
        "cuisine": "Asian",
        "link": "https://www.youtube.com/watch?v=h8IXBipqYgs"
    },
    "chicken soup": {
        "ingredients": ["chicken", "onion", "garlic", "carrot"], 
        "cuisine": "Asian",
        "link": "https://www.youtube.com/watch?v=xudhMRXvJI0"
    },
    "IDK CONTOH AMERIKA": {
        "ingredients": ["chicken", "onion", "garlic", "egg"], 
        "cuisine": "Asian",
        "link": "https://www.youtube.com/watch?v=GMYCMzvOJ5Q"
    }
}

selected_ingredients = []

selected_cuisine = tk.StringVar(window)
selected_cuisine.set(cuisines[0])  
cuisine_menu = tk.OptionMenu(window, selected_cuisine, *cuisines)
cuisine_menu.pack()

def print_selection():
    selected_ingredients.clear()
    if var1.get() != 0: selected_ingredients.append(ingredients[0])  
    if var2.get() != 0: selected_ingredients.append(ingredients[1])  
    if var3.get() != 0: selected_ingredients.append(ingredients[2])  
    if var4.get() != 0: selected_ingredients.append(ingredients[3])  
    if var5.get() != 0: selected_ingredients.append(ingredients[4])  
    if var6.get() != 0: selected_ingredients.append(ingredients[5])  
    if var7.get() != 0: selected_ingredients.append(ingredients[6])  
    if var8.get() != 0: selected_ingredients.append(ingredients[7])  

def clear_previous_labels():
    for widget in window.pack_slaves():
        if isinstance(widget, tk.Label) and widget != l:
            widget.destroy()

def check_recipes():
    clear_previous_labels()
    cuisine = selected_cuisine.get()
    possible_recipes = []
    
    for recipe_name, details in recipes.items():
        recipe_ingredients = details["ingredients"]
        recipe_cuisine = details["cuisine"]
        
        matching_ingredients = sum(1 for item in recipe_ingredients if item in selected_ingredients)
        match_ratio = matching_ingredients / len(recipe_ingredients)
        
        if match_ratio >= 0.75:  # 75% tolerance
            if cuisine == "All" or cuisine == recipe_cuisine:
                possible_recipes.append((recipe_name, details["link"]))
    
    if possible_recipes:
        for name, link in possible_recipes:
            recipe_label = tk.Label(window, text=name, fg="blue", cursor="hand2")
            recipe_label.pack()
            recipe_label.bind("<Button-1>", lambda e, url=link: webbrowser.open_new(url))
    else:
        l.config(text='No matching recipes.')

def get_random_recipe():
    clear_previous_labels()
    cuisine = selected_cuisine.get()
    filtered_recipes = [
        (name, details["link"]) for name, details in recipes.items() 
        if cuisine == "All" or details["cuisine"] == cuisine
    ]
    
    if filtered_recipes:
        random_recipe = random.choice(filtered_recipes)
        random_label = tk.Label(window, text=f'Random Recipe: {random_recipe[0]}', fg="blue", cursor="hand2")
        random_label.pack()
        random_label.bind("<Button-1>", lambda e, url=random_recipe[1]: webbrowser.open_new(url))
    else:
        l.config(text='No recipes available for this cuisine.')

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()
var7 = tk.IntVar()
var8 = tk.IntVar()

checkboxes = [
    tk.Checkbutton(window, text='onion', variable=var1, onvalue=1, offvalue=0, command=print_selection),
    tk.Checkbutton(window, text='garlic', variable=var2, onvalue=1, offvalue=0, command=print_selection),
    tk.Checkbutton(window, text='rice', variable=var3, onvalue=1, offvalue=0, command=print_selection),
    tk.Checkbutton(window, text='egg', variable=var4, onvalue=1, offvalue=0, command=print_selection),
    tk.Checkbutton(window, text='chicken', variable=var5, onvalue=1, offvalue=0, command=print_selection),
    tk.Checkbutton(window, text='pepper', variable=var6, onvalue=1, offvalue=0, command=print_selection),
    tk.Checkbutton(window, text='tomato', variable=var7, onvalue=1, offvalue=0, command=print_selection),
    tk.Checkbutton(window, text='carrot', variable=var8, onvalue=1, offvalue=0, command=print_selection),
]

for checkbox in checkboxes:
    checkbox.pack()

button = tk.Button(window, text='Show Recipe Options', command=check_recipes)
button.pack(pady=10)

random_button = tk.Button(window, text='Get Random Recipe', command=get_random_recipe)
random_button.pack(pady=10)

window.mainloop()
