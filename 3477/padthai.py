"""PAD THAI"""
ingredients = {
    "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
    "Bean Sprouts", "Noodle", "Chives", "Lime",
    "Egg", "Oil", "Peanuts"
}

flavors = {"Sweet", "Sour", "Salty"}

used = set()
taste = set()

while True:
    item = input()
    if item == "Cook":
        break
    used.add(item)

while True:
    item = input()
    if item == "End":
        break
    taste.add(item)

if not used.issubset(ingredients):
    print("This is not Pad Thai!!!")
elif used != ingredients:
    print("This is bad!")
elif taste != flavors:
    print("Not Bad...")
else:
    print("Delicious!")
