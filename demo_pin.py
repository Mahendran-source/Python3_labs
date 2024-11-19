#! /usr/bin/env python3
# Author: Mahendran Moorthy
# Version: 1.0
# Description: Program to compare PIN with master pin and check 3 times.

master_pin = "0123"
pin = None
attempt = 0

while pin != master_pin and attempt < 3:
    pin = input("Enter the PIN: ")
    attempt += 1
    if pin == master_pin:
        print("Valid PIN")
        break
    else:
        print("Invalid PIN")
else:
    #Executes only ONCE when condition becomes False!
    print("Too many attempts")
    print("Your card has been retained. Have a nice day!")

print("Done")

