tuple_string = ("Apple", "Honeydew", "Banana", "Dragonfruit", "Grapes")

def extract_rear_elements(tup):
    rear_elements = [s[-1] for s in tup]
    return rear_elements

# Extract the rear elements
rear_elements = extract_rear_elements(tuple_string)

print("Rear elements:", rear_elements)
