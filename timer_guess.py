from datetime import datetime
from time import sleep

input("Press enter to start and the timer will begin in 3 seconds")
sleep(3)

start_time = datetime.now().strftime("%M:%S")
start_minute, start_second = start_time.split(":")

input("\nTimer started, press enter when you think 10 seconds had passed\n")

end_time = datetime.now().strftime("%M:%S")
end_minute, end_second = end_time.split(":")

minutes_passed = end_minute - start_minute
seconds_passed = seconds_passed - minutes_passed * 60

if int(minutes_passed) == 0:
    print(f"{seconds_passed} seconds have passed")
    if int(seconds_passed) == 10:
        print("\nYou did it perfectly!\n")
else:
    print(f"\n{minutes_passed} minutes and {seconds_passed} seconds have passed\n")
