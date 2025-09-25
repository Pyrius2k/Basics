while True:
    try:
        user_input = input('Enter temperature in °C [0...100°C] or "q" to quit: ')

        if user_input.lower() == 'q':
            print("Program terminated.")
            break

        celsius = float(user_input)

        if not (0 <= celsius <= 100):
            print('Temperature is outside the valid range!')
            continue  


        fahrenheit = 32 + (9/5) * celsius

  
        print(f'\n{celsius}°C equals {fahrenheit}°F\n')

    except ValueError:

        print(f'Invalid input. Please enter a number or "q".\n')
