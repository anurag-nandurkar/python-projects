Here’s the `README.md` content in plain text format:

---

# Recipe Manager

## Description
The **Recipe Manager** is a simple Python-based application that allows users to add, view, and manage their favorite recipes. The recipes are stored in a JSON file (`recipes.json`), making it easy to save and retrieve recipes without using a database. This is a beginner-friendly project, perfect for those looking to learn basic file handling, JSON manipulation, and user input in Python.

## Features
- **Add a Recipe**: Users can input a recipe name, a list of ingredients, and cooking instructions.
- **View All Recipes**: Lists all available recipe names and allows users to select a recipe to view its ingredients and instructions.
- **JSON Data Storage**: Recipes are stored in a `recipes.json` file, making data management simple and persistent.

## Project Structure
```
recipe-manager/
├── README.md
├── recipes.json
└── recipe_manager.py
```

- `README.md`: This file contains information about the project.
- `recipes.json`: The JSON file where all recipes are stored.
- `recipe_manager.py`: The main Python script for the application.

## Prerequisites
- Python 3.x installed on your system
- Basic knowledge of Python programming

## Setup Instructions

### Step 1: Clone the Repository
To get started, clone this repository to your local machine using the following command:
```bash
git clone <repository-url>
```

### Step 2: Navigate to the Project Folder
```bash
cd recipe-manager
```

### Step 3: Install Dependencies
The project does not have external dependencies, so you can directly run the Python script. However, it's recommended to create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### Step 4: Run the Application
```bash
python recipe_manager.py
```

## Usage
### Main Menu
Once you run the script, you will see the following options:
```
Recipe Manager Menu:
1. Add Recipe
2. View All Recipes
3. Exit
```

#### 1. Add Recipe
- Choose option **1** to add a new recipe.
- You will be prompted to enter the following details:
  - **Recipe Name**: The name of the recipe.
  - **Ingredients**: A list of ingredients (comma-separated).
  - **Instructions**: Cooking instructions.

Example:
```
Enter recipe name: Pancakes
Enter ingredients (comma-separated): Flour, Milk, Eggs, Sugar
Enter instructions: Mix all ingredients and fry in a pan.
```

#### 2. View All Recipes
- Choose option **2** to view the list of all recipe names.
- The application will display a list of available recipes. You can then select a recipe by its number to view its ingredients and instructions.

Example:
```
Recipe List:
1. Pancakes
2. Spaghetti

Enter the recipe number to view details (or 0 to cancel): 1

Recipe Details for 'Pancakes':
Ingredients:
  - Flour
  - Milk
  - Eggs
  - Sugar
Instructions: Mix all ingredients and fry in a pan.
```

#### 3. Exit
- Choose option **3** to exit the application.

## JSON Data File (`recipes.json`)
The recipes are stored in a JSON file named `recipes.json` in the following format:
```json
{
    "recipes": [
        {
            "name": "Pancakes",
            "ingredients": ["Flour", "Milk", "Eggs", "Sugar"],
            "instructions": "Mix all ingredients and fry in a pan."
        },
        {
            "name": "Spaghetti",
            "ingredients": ["Spaghetti noodles", "Tomato sauce", "Garlic", "Basil"],
            "instructions": "Boil noodles, add sauce, and serve."
        }
    ]
}
```

## Error Handling
The application includes basic error handling:
- **JSONDecodeError**: If the JSON file is empty or corrupted, the program initializes it with an empty list of recipes.
- **Invalid Input**: The program checks for invalid inputs, such as non-integer menu choices or recipe numbers that are out of range.

## Enhancements
Here are some potential enhancements that could be made in future versions:
- **Edit Recipe**: Add functionality to edit existing recipes.
- **Delete Recipe**: Implement an option to delete a recipe.
- **Search Recipes**: Allow users to search for recipes by name or ingredient.
- **User Authentication**: Add a simple login system to manage different users' recipes.
- **GUI Version**: Create a graphical user interface (GUI) using Tkinter or PyQt.

## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please make sure to update tests as appropriate.

