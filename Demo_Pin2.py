import sys
import getpass

pin ='0123'
limit = 4

for tries in range(1, limit):
    supplied_pin = getpass.getpass('Enter your PIN:')
    if supplied_pin == pin:
        print("Valid PIN")
        print("...and after only",tries,"attempts")
        break
else:
    print("You had",tries,"tries and failed")