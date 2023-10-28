import os
from password_generator import generate_password
from qr_creator import create_qr_code

def generate_password_and_qr():
    try:
        passName = input("Enter a name for the password (or type 'q' to stop): ")
        if passName.lower() == "q":
            print("No Problem !!")
            return None

        length = int(input("Enter the password length: "))
        password = generate_password(length)
        print(f"Your generated password is: {password}")

        choice = input("Want to make a QR code?\n'y' for yes\n'n' for no: ")
        if choice == 'y':
            qr_password = f"Your Generated password is: {password}"
            qr_filename = f"QR/{passName}.png"
            create_qr_code(qr_password, qr_filename)
        elif choice == 'n':
            print("No problem !!")
        return f"{passName}: {password}"
    except ValueError:
        print("Invalid input. Please enter a valid password length.")
        return None

def delete_password_from_file(filename, pass_name):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
        with open(filename, "w") as f:
            found = False  # Flag to track if the name was found
            for line in lines:
                if not line.startswith(f"{pass_name}:"):
                    f.write(line)
                else:
                    found = True  # Name was found in the file
            if not found:
                print("Enter a valid name. Name not found in the password list.")
    except FileNotFoundError:
        print(f"File {filename} not found. No passwords were deleted.")

def delete_qr_code(qr_folder, pass_name):
    try:
        qr_list = os.listdir(qr_folder)
        if pass_name in [qr_name.split('.')[0] for qr_name in qr_list]:
            qr_filename = f"{qr_folder}/{pass_name}.png"
            os.remove(qr_filename)
            print(f"Deleted QR code for {pass_name}")
        else:
            print(f"No QR code found for {pass_name}")
    except FileNotFoundError:
        print(f"Folder {qr_folder} not found. No QR code was deleted.")

def list_passwords(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
        if not lines:
            print("No passwords found in the list.")
        else:
            print("Current Password List:")
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print(f"File {filename} not found. No passwords were listed.")

def list_qr_codes(qr_folder):
    try:
        qr_list = os.listdir(qr_folder)
        if not qr_list:
            print("No QR codes found in the folder.")
        else:
            print("Available QR Codes:")
            for qr_name in qr_list:
                print(qr_name.split('.')[0])
    except FileNotFoundError:
        print(f"Folder {qr_folder} not found. No QR codes were listed.")

def main():
    print("Welcome to the Password + Qr Generator Program!")
    if not os.path.exists("QR"):
        os.makedirs("QR")

    while True:
        print("\nOptions:")
        print("1. Generate a new password and QR code")
        print("2. Delete a password from the file")
        print("3. Delete a QR code")
        print("4. List current passwords")
        print("5. List available QR codes")
        print("6. Quit")
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            password_entry = generate_password_and_qr()
            if password_entry:
                with open("passList.txt", "a") as f:
                    f.write(f"{password_entry}\n")
        elif choice == "2":
            pass_name = input("Enter the name of the password to delete: ")
            delete_password_from_file("passList.txt", pass_name)
        elif choice == "3":
            pass_name = input("Enter the name of the QR code to delete: ")
            delete_qr_code("QR", pass_name)
        elif choice == "4":
            list_passwords("passList.txt")
        elif choice == "5":
            list_qr_codes("QR")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please select a valid option.")

    print("**************************************\n\nThank you for using our program\n\n**************************************")

if __name__ == "__main__":
    main()
