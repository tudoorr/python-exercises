from datetime import datetime
import string

input("Press enter when you want to start entering the alphabet, the timer will also begin")
start_time = datetime.now().strftime("%M:%S")
start_minute, start_second = start_time.split(":")
alphabet = input(">")
end_time = datetime.now().strftime("%M:%S")
end_minute, end_second = end_time.split(":")

if alphabet.lower() == string.ascii_lowercase:
    minutes_passed = int(end_minute) - int(start_minute)
    seconds_passed = int(end_second) + minutes_passed * 60 - int(start_second)
    if minutes_passed == 0:
        print(f"You typed the alphabet in {seconds_passed} seconds!")
        if seconds_passed < 15:
            print("Wow, that's pretty fast!")
    else:
        print(f"\n{minutes_passed} minutes and {seconds_passed} seconds took you to enter the alphabet, you're slow!)
else:
    print("You did not enter the alphabet correctly, try again!\n")
