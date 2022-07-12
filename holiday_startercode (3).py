# import datetime
from datetime import datetime, timedelta
from datetime import time
# from datetime import timedelta
import time
import json
from bs4 import BeautifulSoup
from hamcrest import instance_of
import requests
from dataclasses import dataclass
from config import holidaysjson


# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------
class Holiday:
      
    def __init__(self, name, date):
        #Your Code Here
        self.name = name        
        self.date = datetime.strptime(date, '%Y-%m-%d')
    
    def __str__ (self):
        # String output
        # Holiday output when printed.
        return self.name + " (" + self.date.strftime("%Y-%m-%d") + ")" # might need to add something like the following to the end of self.date for formatting ".strftime("%Y-%m-%d")"

          
           
# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------
class HolidayList:
    def __init__(self):
       self.innerHolidays = []
   
    def addHoliday(self, holidayObj):
        # Make sure holidayObj is an Holiday Object by checking the type
        # Use innerHolidays.append(holidayObj) to add holiday
        # print to the user that you added a holiday
        if isinstance(holidayObj, Holiday):
            found_holiday = self.findHoliday(holidayObj.name, holidayObj.date.strftime("%Y-%m-%d")) 
            if isinstance(found_holiday, Holiday):
                print("The holiday is already added")
            else:
                self.innerHolidays.append(holidayObj)
                print("Succesfully added holiday")
                print(holidayObj)
        else:
            raise ValueError()

    def findHoliday(self, HolidayName, Date):
        # Find Holiday in innerHolidays
        # Return Holiday
        for holiday in self.innerHolidays:
            if holiday.name == HolidayName and holiday.date.strftime("%Y-%m-%d") == Date:
                return holiday

    def removeHoliday(self, HolidayName, Date):
        # Find Holiday in innerHolidays by searching the name and date combination.
        # remove the Holiday from innerHolidays
        # inform user you deleted the holiday
        # print(list(self.innerHolidays))
        hol_to_remove = self.findHoliday(HolidayName, Date)
        dummylist = list(self.innerHolidays)
        print(len(dummylist))
        if isinstance(hol_to_remove, Holiday):
            dummylist.remove(hol_to_remove)
            # del self[hol_to_remove]
            print("\nSuccess:")
            print("%s has been removed from the holiday list." % (HolidayName))
        else:
            print("That holiday is already not in the list")
        print(len(dummylist))
        self.innerHolidays = dummylist
        print(len(self.innerHolidays))

    def read_json(self, filelocation):
        # Read in things from json file location
        # Use addHoliday function to add holidays to inner list.
        file = open(filelocation)
        table = json.load(file)
        print(type(table))
        print(table["holidays"])
        for row in table["holidays"]:
            holiday_name = row["name"]
            holiday_date = row["date"]
            a_holiday = Holiday(holiday_name, holiday_date)
            # print(a_holiday)
            self.addHoliday(a_holiday)

        #     print("holy_date is (89): ")
        #     print(holy_date)
        #     holy_date_name = holy_date["name"]
        #     holy_date_date = holy_date["date"]
        #     holyobj = Holiday(holy_date_name, holy_date_date)
        # return file_dict

    def save_to_json(self, filelocation):
        # Write out json file to selected file.
        saving_dict = {"holidays" : []}
        saving_holiday = {}
        
        for holiday in self.innerHolidays:
            saving_holiday = {"name": holiday.name, "date": holiday.date.strftime("%Y-%m-%d")}
            print(saving_holiday)
            saving_dict["holidays"].append(saving_holiday)

        saving_json = json.dumps(saving_dict, indent=4)
        print(saving_json)

        f = open(filelocation,"w")
        print("file opened")
        f.write(f"{saving_json}")
        print("changes saved")
        f.close()
        
    def getHTML(url):
            response = requests.get(url)
            return response.text

    def scrapeHolidays(self):
        # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
        # Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
        # Check to see if name and date of holiday is in innerHolidays array
        # Add non-duplicates to innerHolidays
        # Handle any exceptions.
        years = [2020, 2021, 2022, 2023, 2024]
        for year in years:
            html = HolidayList.getHTML("https://www.timeanddate.com/holidays/us/%s?hol=33554809" % (year))
            soup = BeautifulSoup(html,'html.parser')

            table = soup.find('tbody').find_all('tr', attrs= {"class": "showrow"})
            # print(list(table))
            holidays = []

            for row in table:
                holiday_name = ''
                split_uf_date = []
                # title = row.find('img')
                if row.find('a') is not None:
                    # print(row.find('a').text)
                    holiday_name = row.find('a').text
                    print(holiday_name)
                
                if row.find('th') is not None:
                    # print(row.find('th').text)
                    unformatted_date = row.find('th').text
                    split_uf_date = unformatted_date.split()
                    print(split_uf_date)
                    if split_uf_date[0] == 'Jan':
                        split_uf_date[0] = '01'
                    elif split_uf_date[0] == 'Feb':
                        split_uf_date[0] = '02'
                    elif split_uf_date[0] == 'Mar':
                        split_uf_date[0] = '03'
                    elif split_uf_date[0] == 'Apr':
                        split_uf_date[0] = '04'
                    elif split_uf_date[0] == 'May':
                        split_uf_date[0] = '05'
                    elif split_uf_date[0] == 'Jun':
                        split_uf_date[0] = '06'
                    elif split_uf_date[0] == 'Jul':
                        split_uf_date[0] = '07'
                    elif split_uf_date[0] == 'Aug':
                        split_uf_date[0] = '08'
                    elif split_uf_date[0] == 'Sep':
                        split_uf_date[0] = '09'
                    elif split_uf_date[0] == 'Oct':
                        split_uf_date[0] = '10'
                    elif split_uf_date[0] == 'Nov':
                        split_uf_date[0] = '11'
                    elif split_uf_date[0] == 'Dec':
                        split_uf_date[0] = '12'
                a_holiday = Holiday(holiday_name, str(year) + "-" + str(split_uf_date[0]) + "-" + str(split_uf_date[1]))
                print("a_holiday is: ")
                print(a_holiday)
                self.addHoliday(a_holiday)

    def numHolidays(self):
        # Return the total number of holidays in innerHolidays
        return len(self.innerHolidays)
    
    def filter_holidays_by_week(self, year, week_number):
        # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
        # Week number is part of the the Datetime object
        # Cast filter results as list
        # return your holidays
        holidays = []
        print("You are in filter_holidays_by_week.\nIt will get you a list of dates for the week\nbut does not use the filter function, nor a lambda")

        # WEEK  = 20 - 2 # as it starts with 0 and you want week to start from sunday
        startdate = time.asctime(time.strptime('%s %d 0' % (int(year), int(week_number)-1), '%Y %W %w')) 
        startdate = datetime.strptime(startdate, '%a %b %d %H:%M:%S %Y') 
        dates = [startdate.strftime('%Y-%m-%d')] 
        for i in range(1, 7): 
            day = startdate + timedelta(days=i)
            dates.append(day.strftime('%Y-%m-%d')) 
        print(dates)
        # week = filter(lambda x: x = week_number)
        # for day in week:

        # holidays.append(holiday)

    def displayHolidaysInWeek(self, holidayList):
        # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
        # Output formated holidays in the week. 
        # * Remember to use the holiday __str__ method.
        print("You are in displayHolidaysInWeek. It does not work yet")


    # def getWeather(weekNum):
    #     # Convert weekNum to range between two days
    #     # Use Try / Except to catch problems
    #     # Query API for weather in that week range
    #     # Format weather information and return weather string.

    # def viewCurrentWeek():
    #     # Use the Datetime Module to look up current week and year
    #     # Use your filter_holidays_by_week function to get the list of holidays 
    #     # for the current week/year
    #     # Use your displayHolidaysInWeek function to display the holidays in the week
    #     # Ask user if they want to get the weather
    #     # If yes, use your getWeather function and display results



def main():
    # Large Pseudo Code steps
    # -------------------------------------
    # 1. Initialize HolidayList Object
    # 2. Load JSON file via HolidayList read_json function
    # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
    # 3. Create while loop for user to keep adding or working with the Calender
    # 4. Display User Menu (Print the menu)
    # 5. Take user input for their action based on Menu and check the user input for errors
    # 6. Run appropriate method from the HolidayList object depending on what the user input is
    # 7. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 
    hl = HolidayList()
    hl.read_json(holidaysjson)
    hl.scrapeHolidays()
    # test_holiday = Holiday("Today Day", "2022-07-10")
    # print(test_holiday)
    # hl.addHoliday(test_holiday)
    # hl.addHoliday(test_holiday)
    # find_test = hl.findHoliday(test_holiday.name, test_holiday.date.strftime("%Y-%m-%d"))
    # print(find_test)

    start_up = hl.numHolidays()
    print("\nHoliday Management")
    print("====================")
    print("There are %s holidays stored in the system" % (start_up))

    keep_going = True
    unsaved_changes = True
    while keep_going:
        main_menu = input('\nHoliday Menu\n====================\n1. Add a Holiday\n2. Remove a Holiday\n3. Save Holiday List\n4. View Holidays\n5. Exit\n\n')
        if main_menu == '1':
            # This is the Add a Holiday option
            print("\nAdd a Holiday\n====================\n")
            hol_name = input("Holiday: ")
            hol_date = input("Date: ")
            add_this = Holiday(hol_name, hol_date)
            print(add_this)
            print(type(add_this))
            hl.addHoliday(add_this)
            print("\nSuccess:\n%s has been added to the list" % (add_this))
            unsaved_changes = True
            do_more = input("Would you like to return to the Holiday Menu or exit the application [menu/exit]: ")
            if do_more == 'exit':
                if unsaved_changes:
                    y_n =  input("Are you sure you want to exit?\nYour changes will be lost\n[y/n]: ")
                    if y_n == 'y':
                        exit("\nExiting. See you next time!")
                else:
                    y_n = input("Are you sure you want to exit? [y/n]: ")
                    if y_n == 'y':
                        exit("\nExiting. See you next time!")
            elif do_more == 'menu': 
                keep_going = True
                pass
            # need to get user input after this runs to find out if they want to keep running the app or exit.
            # note sure if it will need to be in each of these if/elifs or if I can do it once outside of that
        elif main_menu == '2':
            # This is the Remove a Holiday option
            holiday_name = input("Holiday Name: ")
            holiday_date = input("Holiday Date: ")
            hl.removeHoliday(holiday_name, holiday_date)
            unsaved_changes = True
            do_more = input("Would you like to return to the Holiday Menu or exit the application [menu/exit]: ")
            if do_more == 'exit':
                if unsaved_changes:
                    y_n =  input("Are you sure you want to exit?\nYour changes will be lost\n[y/n]: ")
                    if y_n == 'y':
                        exit("\nExiting. See you next time!")
                else:
                    y_n = input("Are you sure you want to exit? [y/n]: ")
                    if y_n == 'y':
                        exit("\nExiting. See you next time!")
            elif do_more == 'menu': 
                keep_going = True
                pass
        elif main_menu == '3':
            # This is the save_to_json option
            hl.save_to_json("test.json")
            do_more = input("Would you like to return to the Holiday Menu or exit the application [menu/exit]: ")
            unsaved_changes = False
            if do_more == 'exit':
                y_n = input("Are you sure you want to exit? [y/n]: ")
                if y_n == 'y':
                    keep_going = False
                    exit("\nExiting. See you next time!")
            elif do_more == 'menu': 
                keep_going = True
                pass
        elif main_menu == '4':
            # This is the View Holiday option, which does not presently have it's own function, but probably uses at least findHoliday
            print("You are still in the main menu. This does not work yet")
            year = input("Which year?: ")
            week = input("Which week? #[1-52, Leave blank for the current week: ")
            hl.filter_holidays_by_week(year, week)

            # I have no idea how I am supposed to find holidays for a given week 

            # uncomment below block when this feature is working so it asks if they want to continue
            # if do_more == 'exit':
            #     if unsaved_changes:
            #         y_n =  input("Are you sure you want to exit?\nYour changes will be lost\n[y/n]: ")
            #         if y_n == 'y':
            #             exit("\nExiting. See you next time!")
            #     else:
            #         y_n = input("Are you sure you want to exit? [y/n]: ")
            #         if y_n == 'y':
            #             exit("\nExiting. See you next time!")
            #     keep_going = False
            #     exit("\nExiting. See you next time!")
            # elif do_more == 'menu': 
            #     keep_going = True
            #     pass
        elif main_menu == '5':
            # This closes the application
            if unsaved_changes:
                y_n =  input("Are you sure you want to exit?\nYour changes will be lost\n[y/n]: ")
                if y_n == 'y':
                    exit("\nExiting. See you next time!")
            else:
                y_n = input("Are you sure you want to exit? [y/n]: ")
                if y_n == 'y':
                    exit("\nExiting. See you next time!")
            # Need to add a condition for if there have been changes that need to be saved...
            # i.e. if any holidays have been added or removed
            # Also need condition for if they do not want to exit
        # do_more = input("Would you like to return to the Holiday Menu or exit the application [menu/exit]: ")
        # if do_more == 'exit':
        #     keep_going = False

    





if __name__ == "__main__":
    main()

# Additional Hints:






# ---------------------------------------------
# You may need additional helper functions both in and out of the classes, add functions as you need to.
#
# No one function should be more then 50 lines of code, if you need more then 50 lines of code
# excluding comments, break the function into multiple functions.
#
# You can store your raw menu text, and other blocks of texts as raw text files 
# and use placeholder values with the format option.
# Example:
# In the file test.txt is "My name is {fname}, I'm {age}"
# Then you later can read the file into a string "filetxt"
# and substitute the placeholders 
# for example: filetxt.format(fname = "John", age = 36)
# This will make your code far more readable, by seperating text from code.





