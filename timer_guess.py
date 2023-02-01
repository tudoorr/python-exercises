from datetime import datetime

input("Press enter to start and the timer will begin")

start_second = datetime.now().strftime("%S")
print(start_time)

input("\nTimer started, press enter when you think 10 seconds had passed\n")

end_second = datetime.now().strftime("%S")
print(end_time)

if end_second < start_second:
    seconds_passed = int(end_second) + 60 - int(start_second)
else:
    seconds_passed = int(end_second) - int(start_second)

if seconds_passed < 60:
    print(f"{seconds_passed} seconds have passed")
else:
    minutes_passed = seconds_passed % 60
    seconds_passed = seconds_passed - minutes_passed * 60
    print(f"\n{minutes_passed} minutes and {seconds_passed} seconds have passed\n")

if seconds_passed == 10 and minutes_passed == 0:
    print("\nYou did it perfectly!\n")
