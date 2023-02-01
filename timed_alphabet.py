from datetime import datetime
import string

input("Press enter when you want to start entering the alphabet, the timer will also begin")
start_second = datetime.now().strftime("%S")
alphabet = input(">")

if alphabet.lower() == string.ascii_lowercase:
    end_second = datetime.now().strftime("%S")
    if end_second < start_second:
        seconds_passed = int(end_second) + 60 - int(start_second)
    else:
        seconds_passed = int(end_second) - int(start_second)
    if seconds_passed < 60:
        print(f"You took {seconds_passed} seconds to enter the alphabet")
    else:
        minutes_passed = seconds_passed % 60
        seconds_passed = seconds_passed - minutes_passed * 60
        print(f"\nYou took {minutes_passed} minutes and {seconds_passed} seconds to enter the alphabet\n")
else:
    print("You did not enter the alphabet correctly!\n")
