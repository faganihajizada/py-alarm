import datetime, time, random, webbrowser
from datetime import datetime

class bcolors:
    GREEN = '\033[92m'
    WARN = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

current_time = time.strftime("%H:%M:%S")

print("")
print(bcolors.WARN + "Please set a time for alarm. Note: 24-hour time notation." + bcolors.ENDC)
print (bcolors.WARN + "Currently the time is: " + current_time + bcolors.ENDC)
print("")

# Check the input from user and check if it's integer and if it's supported value
def check_alarm_input_hour(hour):
  while True:
    try:
        alarm_hour = int(input(hour))
    except ValueError:
       print(bcolors.FAIL + "The added value is not an integer. Please try again." + bcolors.ENDC)
       continue
    else:
      if (0 <= alarm_hour <= 24): 
        return alarm_hour
      else:
        print(bcolors.FAIL + "You have entered an invalid value\nThe time should have been entered in 24-hour time notation. Allowed values: between 0 and 24" + bcolors.ENDC)

def check_alarm_input_minute(minute):
  while True:
    try:
        alarm_minute = int(input(minute))
    except ValueError:
        print(bcolors.FAIL + "The added value is not an integer. Please try again." + bcolors.ENDC)
        continue
    else:
      if (0 <= alarm_minute < 60):
        return alarm_minute
      else:
        print(bcolors.FAIL + "You have entered an invalid value\nThe time should have been entered in 24-hour time notation. Allowed values: between 0 and 59" + bcolors.ENDC)


alarm_hour = check_alarm_input_hour(bcolors.GREEN + "Please enter the hour (format: 'HH'): " + bcolors.ENDC)
alarm_minute = check_alarm_input_minute(bcolors.GREEN + "Please enter the minute (format: 'MM'): " + bcolors.ENDC)

print("")
print("#########################################################################################")
print(bcolors.WARN, "The alarm has been set for:", alarm_hour, ":" ,alarm_minute, bcolors.ENDC)
print("#########################################################################################")

# open file and read urls
with open('video-list.txt', 'r') as video_file:
    video_links = video_file.readlines()

# loop until time matches alarm time
while True:
    if (alarm_hour == datetime.now().hour and alarm_minute == datetime.now().minute):
        print(bcolors.GREEN + "\nIt's time! Opening a randomly choosed video from the list in web browser" + bcolors.ENDC)
        randomly_selecte_video=random.choice(video_links)
        webbrowser.open(randomly_selecte_video)
        break