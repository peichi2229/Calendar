"""
This is a
Calendar 
Project
"""

from time import sleep, strftime
name = raw_input("Enter your name: ")
calendar = {}

def welcome():
  print "Welcome %s" % name
  print "The Calandar is starting!"
  sleep(1)
  print "Today is: " + strftime("%A, %B %d, %Y")
  print "The time is: " + strftime("%H:%M:%S")
  sleep(1)
  print "What would you like to do?"

def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("Enter your choice. A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == 'V':
      if len(calendar.keys()) < 1:
        print "Your calendar is empty!"
      else:
        print calendar
    elif user_choice == 'U':
       date = raw_input("What date? ")
       update = raw_input("Enter the update: ")
       calendar[date] = update
       print "Your calendar has been updated!"
       print calendar
    elif user_choice == 'A':
       event = raw_input("Enter event: ")
       date = raw_input("Enter date (MM/DD/YYYY): ")
       if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
         print "The entered date was invalid!"
         try_again = raw_input("Try Again? Y for Yes, N for No: ")
         try_again.upper()
         if try_again == 'Y':
           continue
         else:
           start = False
       else:
         calendar[date] = event
         print "The event has been added!"
         print calendar
    elif user_choice == 'D':
      if len(calendar.keys()) < 1: 
        print "Your calendar is empty!"
      else:
        event = raw_input("What event? ")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print "The event has been deleted!"
            print calendar
          else:
            print "The entered event was incorrect!"
    elif user_choice == "X":
      start = False
    else:
      print "Invalid Command!"
      start = False
    
start_calendar()
