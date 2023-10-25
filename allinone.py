# Here is every main code linked in one file .

import random, os, qrcode

char = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*"

passList = []

# Check if passList.txt file exists and read the existing content
pass_count = 0
if os.path.exists("passList.txt"):
    # Determine the last used number in the existing content
    last_line = ""  # Initialize last_line
    with open("passList.txt", "r") as file:
        for line in file:
            last_line = line
        line = last_line.strip()  # Remove leading and trailing whitespace
        if line:  # Check if the line is not empty
            first_character = line[0]
            if first_character.isnumeric():
                first_character = int(first_character)
                pass_count += first_character

# Create the "QR" folder if it doesn't exist
if not os.path.exists("QR"):
    os.makedirs("QR")

while True:
    passName = input("Enter a name for the password (or type 'q' to stop): ")
    if passName.lower() == "q":
        break

    length = int(input("Enter the password length: "))
    password = ""

    for i in range(length):
        password += random.choice(char)

    print(f"Your generated password is: {password}")

    choice = int(input("Want to make a QR code?\n1 for yes\nAnything else for no: "))

    if choice == 1:
        qr_password = f"Your Generated password is: {password}"
        img = qrcode.make(qr_password)
        qr_filename = f"QR/{passName}.png"  # Save QR code in the "QR" folder
        img.save(qr_filename)
        print(f"Your QR code has been generated and saved as '{qr_filename}'")

    pass_count += 1
    passList.append(f"{pass_count}. {passName}: {password}")

with open("passList.txt", "a") as f:
    for line in passList:
        f.write(f"{line}\n")

print(
    "**************************************\n\nThank you for using our program\n\n**************************************"
)
