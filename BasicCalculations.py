
# Helper function that multiplies
def multiply(z1, z2):
    return z1 * z2

# Helper function that calculates the volume and surface area of a cuboid
def cuboid(length, width, height):
    volume = length * width * height
    surface_area = 2 * (length * width + length * height + width * height)
    return volume, surface_area

# Test the multiply function
print('Calling functions from a Python script:\n')
print('Multiplying two numbers:\n')
try:
    z1 = float(input('First number: '))
    z2 = float(input('Second number: '))
    result = multiply(z1, z2)
    print(f'The result is: {result}\n')
except ValueError:
    print('Error: Invalid input. Please enter a number.\n')

# Test the cuboid function
print('Calculating the volume and surface area of a cuboid:\n')
try:
    L = float(input('Length [cm]: '))
    W = float(input('Width [cm]: '))
    H = float(input('Height [cm]: '))
    
    # Call the function
    volume, surface_area = cuboid(L, W, H)
    
    print(f'\nThe volume of the cuboid is {volume:.2f} cm³')
    print(f'The surface area of the cuboid is {surface_area:.2f} cm²\n')
except ValueError:
    print('Error: Invalid input. Please enter only numbers.\n')

print('Program finished!')