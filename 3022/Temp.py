"""Temp"""
def main():
    """Temp"""
    temp = float(input(""))
    from_format = input("")
    to_convert = input("")
    result = 0
    final_result = 0
    if from_format == "C":
        result = temp 
    elif from_format == "K":
        result = temp - 273.15
    elif from_format == "F":
        result = (temp - 32) * 5/9
    elif from_format == "R":
        result = (temp - 491.67) * 5/9
    if to_convert == "C":
        final_result = result
    elif to_convert == "K":
        final_result = result + 273.15
    elif to_convert == "F":
        final_result = result * 9/5 + 32
    elif to_convert == "R":
        final_result = result * 9/5 + 491.67
        
    print(f"{final_result:.2f}")
main()
