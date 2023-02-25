from datetime import datetime
from time import sleep

input("Press enter to start and the timer will begin in 3 seconds")
sleep(3)
start_minute, start_second = datetime.now().strftime("%M:%S").split(":")
input("\nTimer started, press enter when you think 10 seconds had passed\n")
end_minute, end_second = datetime.now().strftime("%M:%S").split(":")

minutes_passed = int(end_minute) - int(start_minute)
seconds_passed = int(end_second) + minutes_passed * 60 - int(start_second)

if minutes_passed == 0:
    print(f"{seconds_passed} seconds have passed")
    if seconds_passed == 10:
        print("\nYou did it perfectly!\n")
else:
    print(f"\n{minutes_passed} minutes and {seconds_passed} seconds have passed\n")
