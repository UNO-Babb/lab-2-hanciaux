#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6)%24
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  hours = input("How many hours? ")
  #Ask user for minutes
  minutes = input("How many minutes? ")
  #Calculate the time after the user-supplied time has passed.
  hours=int(hours) 
  minutes=int(minutes)

  newMinute=(currentMinute + minutes)
  excess=newMinute//60
  newHour=(currentHour + hours + excess)
  
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  newHour = (newHour%12)
  newMinute = (newMinute%60)
  strHour = str(newHour)
  strMinute = str(newMinute)
  if newMinute < 10:
    strMinute = "0" + strMinute
  if newHour == 0:
    strHour = "12"
  print(strHour + ":" + strMinute)
if __name__ == '__main__':
  main()
