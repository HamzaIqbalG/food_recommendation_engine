import json

def load_recipes(filename):
    """
    Load recipes from a JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)

def find_recipes_by_ingredient(recipes, ingredient):
    """
    Find recipes that use a specific ingredient.
    """
    matching_recipes = [recipe for recipe in recipes if ingredient in recipe['ingredients']]
    return matching_recipes

def main():
    print("Welcome to CookBook Companion - Your Personalized Food Recommendation Engine!")
    
    # Load recipes (assuming they are stored in a JSON file for this example)
    recipes = load_recipes('recipes.json')

    # Get user input for an ingredient
    ingredient = input("Enter an ingredient you have: ").strip().lower()

    # Find and display recipes
    found_recipes = find_recipes_by_ingredient(recipes, ingredient)
    if found_recipes:
        print(f"Recipes with {ingredient}:")
        for recipe in found_recipes:
            print(recipe['name'])  # Assuming each recipe has a 'name' key
    else:
        print(f"No recipes found with {ingredient}.")

if __name__ == "__main__":
    main()
 
