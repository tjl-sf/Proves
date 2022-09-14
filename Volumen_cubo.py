# Python Program to Calculate the Volume and Surface Area of Cuboid

# Take the input from the User
length = float(input("Enter the Length of a Cuboid: "))
width = float(input("Enter the Width of a Cuboid: "))
height = float(input("Enter the Height of a Cuboid: "))

if length < 0:
    raise ValueError("No tiene sentido introducir longitud negativa")

if type(length) not in [int, float]:
    raise ValueError("La longitud tiene que ser real o entero")
# Calculate the Volume
Volume = length * width * height;

# Print the Output
print("The Volume of a Cuboid = %.2f" %Volume);
