from src import *
import sys

print("\n\n--------------------------------------------")
print("Welcome to Binary probability calculator 1.0.")
print("--------------------------------------------")

while 1:

    res = input('\nWould you like to calculate a probability? Y/N\n > ')

    if res == 'Y':

        totalEvents = input('Please, enter number of total events: ')
        trueEvents = input('Please, enter number of true events: ')
        print()

        if totalEvents == None or trueEvents == None or (not trueEvents.isnumeric()) or (not totalEvents.isnumeric()):
            print("One of the inputs is void or invalid.")
            continue


        calWrapper(int(trueEvents),int(totalEvents))

    elif res == 'N':
        sys.exit(0)
    else:
        print("Invalid response.")
