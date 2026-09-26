pasta=("Pasta Arrabiata", "Italian", 20, "Medium")
biryani=("Biryani", "Indian", 45, "Hard")
print ("Recipe 1:", pasta)
print("Name:", pasta[0])
print("Cuisine:", pasta[1])
print("Difficulty Level:", pasta[-1])

all_recipes =(pasta, biryani)
print("First Recipe Name:" , all_recipes[0][0])
print("Second recipe time to cook:", all_recipes[1][2], "minutes")
print("Pasta Details(sliced):", pasta[1:3])

print("Pasta recipe details:")
for detail in pasta:
    print(" - ", detail)

pasta_ingredients = {"tomato", "garlic", "olive oil", "chili flakes", "pasta"}
biryani_ingredients = {"rice", "chicken", "yogurt", "spices", "saffron"}
print("Pasta Ingredients:", pasta_ingredients)
print("Biryani Ingredients:", biryani_ingredients)
print("Total pasta ingredients:", len(pasta_ingredients))

pasta_ingredients.add("basil")
pasta_ingredients.discard("chili flakes")
print("Updated Pasta Ingredients:", pasta_ingredients)

all_ingredients = pasta_ingredients.union(biryani_ingredients)
common = pasta_ingredients.intersection(biryani_ingredients)
only_pasta = pasta_ingredients.difference(biryani_ingredients)
unique_to_each = pasta_ingredients.symmetric_difference(biryani_ingredients)

print("All ingredients (union):",   all_ingredients)
print("Common ingredients (intersection):", common)
print("Only in pasta (difference):", only_pasta)
print("Not shared (sym. difference ):", unique_to_each)
