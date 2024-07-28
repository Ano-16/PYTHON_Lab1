import math

# Heron's formula
def calculate_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def get_triangle_sides():
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))
    return a, b, c


print("Enter the sides of the first triangle:")
a1, b1, c1 = get_triangle_sides()


print("Enter the sides of the second triangle:")
a2, b2, c2 = get_triangle_sides()

# Calculate the areas of both triangles
area1 = calculate_area(a1, b1, c1)
area2 = calculate_area(a2, b2, c2)

# Calculate the total area
total_area = area1 + area2

# percentage contribution of each triangle
percentage1 = (area1 / total_area) * 100
percentage2 = (area2 / total_area) * 100

# Print the results
print(f"Area of the first triangle: {area1:.2f}")
print(f"Area of the second triangle: {area2:.2f}")
print(f"Total area enclosed by both triangles: {total_area:.2f}")
print(f"First triangle's contribution: {percentage1:.2f}%")
print(f"Second triangle's contribution: {percentage2:.2f}%")
