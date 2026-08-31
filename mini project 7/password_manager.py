# building a password manager
# ‼️before using it personally / hosting please learn the concept of encryption to save the password database secured‼️

import os
import pyperclip

FILE_NAME = os.path.join(os.path.dirname(__file__), "password.txt")
# this path is given to save the file under the giver folder


def save_password():
    website = input("Enter the website name: ")
    password = input("Enter the password: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{website} [||] {password}\n")


def get_password():
    website = input("Enter website name: ")
    with open(FILE_NAME, "r") as f:
        for line in f:
            if website in line:
                password = line.strip().split("[||]")[1]
                pyperclip.copy(password)
                print("----------------------------------------")
                print("Password has been copied to clipboard.")
                print("----------------------------------------")
                # print(line) --> this is used to print the password in th terminal,
                # to save the password securly do not use this statement
                # it is safe to use it as password is copied to clipboard and paste in the desired locatioh
                break
            else:
                print("website not found in the database.")


def main():
    while True:
        print("PASSWORD MANAGER")
        print("----------------------------------------")
        print("1. Save Password \n2. Get Password \n3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            save_password()

        elif choice == "2":
            get_password()

        elif choice == "3":
            print("Exiting...")
            print("----------------------------------------")
            break

        else:
            print("Invalid choice . Please Try again.")
            print("----------------------------------------")


main()
