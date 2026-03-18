
while True:
    print("\n--- Temperature Converter Menu ---")
    print("1. Convert from Celsius")
    print("2. Convert from Fahrenheit")
    print("3. Convert from Kelvin")
    print("4. Exit")

    choice = input("\nPick an option (1-4): ")

    if choice == '4':
        print("Catch you later!")
        break

    if choice not in ['1', '2', '3']:
        print("Invalid choice. Please try again.")
        continue

    try:
        temp = float(input("Enter the temperature value: "))
    except ValueError:
        print("That's not a number. Please enter a valid temperature.")
        continue

    print("-" * 30)

    if choice == '1':
        # Celsius to F and K
        f = (temp * 9 / 5) + 32
        k = temp + 273.15
        print(f"{temp}°C is equal to:")
        print(f"Fahrenheit: {round(f, 2)}°F")
        print(f"Kelvin:     {round(k, 2)}K")

    elif choice == '2':
        # Fahrenheit to C and K
        c = (temp - 32) * 5 / 9
        k = c + 273.15
        print(f"{temp}°F is equal to:")
        print(f"Celsius:    {round(c, 2)}°C")
        print(f"Kelvin:     {round(k, 2)}K")

    elif choice == '3':
        # Kelvin to C and F
        c = temp - 273.15
        f = (c * 9 / 5) + 32
        print(f"{temp}K is equal to:")
        print(f"Celsius:    {round(c, 2)}°C")
        print(f"Fahrenheit: {round(f, 2)}°F")

    # print("-" * 30)
