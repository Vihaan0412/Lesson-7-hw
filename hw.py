char = input("Enter a single character: ")
ascii_value = ord(char)

if ascii_value is 65:
    print("True! You entered capital 'A'.")
else:
    print(f"False! The ASCII value is {ascii_value}, which is not 65.")