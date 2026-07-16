"""[LEARNING LOGS] Colors"""
color1 = input("first color: ").strip().lower()
color2 = input("second color: ").strip().lower()

if (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
    print("Orange")
elif (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
    print("Violet")
elif (color1 == "yellow" and color2 == "blue") or (color1 == "blue" and color2 == "yellow"):
    print("Green")
elif color1 not in ["red", "yellow", "blue"] or color2 not in ["red", "yellow", "blue"]:
    print("Error")
elif color1 == color2:
    print(color1.capitalize())
else:
    print("Error")