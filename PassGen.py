import random
import string
import time
import sys


print("██████╗░░█████╗░░██████╗░██████╗  ░██████╗░███████╗███╗░░██╗")
print("██╔══██╗██╔══██╗██╔════╝██╔════╝  ██╔════╝░██╔════╝████╗░██║")
print("██████╔╝███████║╚█████╗░╚█████╗░  ██║░░██╗░█████╗░░██╔██╗██║")
print("██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗  ██║░░╚██╗██╔══╝░░██║╚████║")
print("██║░░░░░██║░░██║██████╔╝██████╔╝  ╚██████╔╝███████╗██║░╚███║")
print("╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░  ░╚═════╝░╚══════╝╚═╝░░╚══╝")
print("-----------------------------------------------------------------------")

print("(1) Create a password     (2) Exit")
print("")



def generate_password(length):
    """Generates a random password of the specified length"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

action_number = int(input("Please select what you want to do: "))
if action_number == 1:
    print("Creating functions ...")
    time.sleep(2)
    print("")
    print("Building system...")
    time.sleep(3)
    
    length_of_pass = int(input("Please enter the length of the password you want to create: "))
    time.sleep(4)
    
    password = generate_password(length_of_pass)
    print("Your new password is:", password)
    input("Exitting when you press enter : ")

if action_number == 2:
    print("Good bye :)")
    time.sleep(2)
    sys.exit()
