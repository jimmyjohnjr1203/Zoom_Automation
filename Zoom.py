import keyboard, time, subprocess
import pandas as pd
from datetime import datetime, date
import pyscreeze
import pyautogui

#reading the meeting details
df = pd.read_csv('meetingschedule.csv')
df_new = pd.DataFrame()
# check the date
current_date = date.today()
day_of_week = current_date.isoweekday()
print(str(day_of_week))
# only look at the meetings happening today
if day_of_week < 4: 
    todays_meetings = df[df['First_Day'] == day_of_week]
else:
    todays_meetings = df[df['Second_Day'] == day_of_week]

check_time = True
while(check_time == True):
    #Check the current system time
    timestr = datetime.now().strftime("%H:%M") 
    #Check if the current time is mentioned in the Dataframe and end loop
    if timestr in todays_meetings.Time.values:
        print('Time found in database')
        check_time = False

print('Opening Zoom')
df_new = todays_meetings[todays_meetings['Time'].astype(str).str.contains(timestr)]
print (df_new)
#Open the Zoom app
subprocess.Popen("C:\\Users\\jackl\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
print('Zoom opened')
time.sleep(3)
#Locate the position of the join button on the screen
position = pyautogui.locateCenterOnScreen("buttons\\join_button.png")
#Move the cursor to the position of the button
pyautogui.moveTo(position[0], position[1])
#Perform click operation
pyautogui.click()
print('Join selected')
time.sleep(3)
#Write the meeting ID from the dataframe onto the Zoom App
keyboard.write(df_new.iloc[0,1])
print('MeetingId placed')

#For tapping the Turn off video option on Zoom app
position = pyautogui.locateCenterOnScreen("buttons\\turn_off_vid_button.png")
pyautogui.moveTo(position[0], position[1])
pyautogui.click()
time.sleep(2)

#For tapping on the Join button
position = pyautogui.locateCenterOnScreen("buttons\\join_button_2.png")
pyautogui.moveTo(position[0], position[1])
pyautogui.click()
time.sleep(7)

#Reads the Meeting Passcode from the dataframe and enters into the zoom app
keyboard.write(str(df_new.iloc[0,2]))
time.sleep(3)

#For finally joining the meeting
position = pyautogui.locateOnScreen("buttons\\join_meeting.png")
pyautogui.moveTo(position[0], position[1])
pyautogui.click()

#Wait for one minute before the next iteration starts
#time.sleep(60)



