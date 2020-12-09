import datetime, time, random, webbrowser
from datetime import datetime

current_time = time.strftime("%H:%M:%S")

url1 = "https://www.youtube.com/watch?v=u8w9lItR05U"
url2 = "https://www.youtube.com/watch?v=Kbik2irlE8U"

# Check the input from user
def check_alarm_input(alarm_time):
    if (0 <= alarm_minute <= 60) and (0 <= alarm_hour <= 24):
        return True
    else:
        return False
    return False

# Get input from user for the alarm
print("Please set a time for alarm. Note: 24-hour time notation.")
while True:
    print("")
    print ("Currently the time is:", current_time)
    alarm_hour = int(input("Please enter the hour (format: 'HH'): "))
    alarm_minute = int(input("Please enter the minute (format: 'MM'): "))
    print("")
    try:
        if check_alarm_input(alarm_minute):
            break
        if check_alarm_input(alarm_hour):
            break
        else:
            raise ValueError
    except ValueError:
        print("ERROR: The time should have been entered in 24-hour time notation. \nMinute is between 0 and 60. Hour it is between 0 and 24.")

print("The alarm has been set for:", alarm_hour, ":" ,alarm_minute)
print("")

# loop until time matches alarm time
while True:
    if (alarm_hour == datetime.now().hour and alarm_minute == datetime.now().minute):
        print("\nIt's the time!")
        web_url = random.choice([url1, url2])
        webbrowser.open(web_url)
        break