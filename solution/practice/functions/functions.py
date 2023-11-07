def kg_to_grams(kg):
    return kg * 1000

kg = float(input("Enter weight in kilograms: "))
grams = kg_to_grams(kg)
print(f"The weight in grams is {grams}")