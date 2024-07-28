ListColour = [["Black", "Red", "Maroon", "Yellow"], ["000000", "FF0000", "800000", "FFFF00"]]

# Function to convert lists to a list of dictionaries
def convert_to_dicts(names, codes):
    result = []
    for name, code in zip(names, codes):
        result.append({'colorName': name, 'colorCode': code})
    return result

color_dicts = convert_to_dicts(ListColour[0], ListColour[1])
print(color_dicts)
