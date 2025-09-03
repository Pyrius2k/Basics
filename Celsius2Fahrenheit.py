# Celsius to Fahrenheit conversion
while True:
    try:
        # Input for temperature in °C
        user_input = input('Enter temperature in °C [0...100°C] or "q" to quit: ')

        # Check if the user wants to quit the program
        if user_input.lower() == 'q':
            print("Program terminated.")
            break

        celsius = float(user_input)

        # Check if the temperature is within the valid range
        if not (0 <= celsius <= 100):
            print('Temperature is outside the valid range!')
            continue  # Jumps back to the start of the loop

        # Convert Celsius to Fahrenheit
        fahrenheit = 32 + (9/5) * celsius

        # Print the result
        print(f'\n{celsius}°C equals {fahrenheit}°F\n')

    except ValueError:
        print(f'Invalid input. Please enter a number or "q".\n')