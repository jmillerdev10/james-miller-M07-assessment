import datetime
import json
from attr import attrs
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass
from config import holidaysjson
from config import weatherurl
from config import querystring
from config import headers

holidays_dict = {}


# # -------------------------------------------
# # Modify the holiday class to 
# # 1. Only accept Datetime objects for date. 
# # 2. You may need to add additional functions
# # 3. You may drop the init if you are using @dataclasses
# # --------------------------------------------
@dataclass
class Holiday:
    name: str
    date: datetime       
    
    def __str__ (self):
        # String output
        # Holiday output when printed.
        return self.name + " (" + self.date.strftime("%Y-%m-%d") + ")"
          
           
# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------
@dataclass
class HolidayList:
    innerHolidays: list

   
    def addHoliday(holidayObj):
        # Make sure holidayObj is an Holiday Object by checking the type
        # Use innerHolidays.append(holidayObj) to add holiday
        # print to the user that you added a holiday
        print("addHoliday UNDER CONSTRUCTION")
        print("holidayObj type is:")
        print(type(holidayObj))
        # HolidayList(innerHolidays).append(holidayObj) # not sure why it is not recognizing innerHolidays. Also tried HolidayList.innerHolidays, but that doesnt work either
        # print(innerHolidays)

#     def findHoliday(HolidayName, Date):
#         # Find Holiday in innerHolidays
#         # Return Holiday

#     def removeHoliday(HolidayName, Date):
#         # Find Holiday in innerHolidays by searching the name and date combination.
#         # remove the Holiday from innerHolidays
#         # inform user you deleted the holiday

    def read_json(filelocation):
        # Read in things from json file location
        # Use addHoliday function to add holidays to inner list.

        file = open(filelocation)
        file_dict = json.load(file)
        print(type(file_dict))
        print(file_dict["holidays"])
        for holy_date in file_dict["holidays"]:
            print("holy_date is: ")
            print(holy_date)
            holy_date_name = holy_date["name"]
            holy_date_date = holy_date["date"]
            holyobj = Holiday(holy_date_name, holy_date_date)
            HolidayList.addHoliday(holyobj)
        return file_dict

#     def save_to_json(filelocation):
#         # Write out json file to selected file.
        
    def scrapeHolidays(year):
        # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
        # Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
        # Check to see if name and date of holiday is in innerHolidays array
        # Add non-duplicates to innerHolidays
        # Handle any exceptions. 
        print("UNDER CONSTRUCTION")
        

        def getHTML(url):
            response = requests.get(url)
            return response.text

        # year = 2022
        # print("https://www.timeanddate.com/holidays/us/%s?hol=33554809" % (year))
        # html = getHTML("https://www.timeanddate.com/holidays/us/%s?hol=33554809" % (year))
        html = getHTML("https://www.timeanddate.com/holidays/us/2022?hol=33554809")
        soup = BeautifulSoup(html,'html.parser')

        table = soup.find('tbody').find_all('tr')
        # print(list(table))
        holidays = []

        for row in table:
            holiday = {}
            # title = row.find('img')
            if row.find('a') is not None:
                # print(row.find('a').text)
                holiday['name'] = row.find('a').text
            if row.find('th') is not None:
                # print(row.find('th').text)
                holiday['date'] = row.find('th').text
            # print([holiday['date'], holiday['name']])
            # print(row.find(class_ = 'star-rating')["class"][1])
            holidays.append(holiday)

        for holiday in holidays:
            if holiday == {}:
                holidays.remove(holiday)
        # jholidays = {'%s holidays' % year: holidays}

        # test_file = open('json_file.json', 'w')
        # json.dump(jholidays, test_file, indent = 4)
        # test_file.close()
        # print(list(holidays))
        return holidays

#     def numHolidays():
#         # Return the total number of holidays in innerHolidays
    
#     def filter_holidays_by_week(year, week_number):
#         # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
#         # Week number is part of the the Datetime object
#         # Cast filter results as list
#         # return your holidays

#     def displayHolidaysInWeek(holidayList):
#         # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
#         # Output formated holidays in the week. 
#         # * Remember to use the holiday __str__ method.

    def getWeather(weekNum): 
        # Convert weekNum to range between two days
        # Use Try / Except to catch problems
        # Query API for weather in that week range
        # Format weather information and return weather string.
        response = requests.request("GET", weatherurl, headers=headers, params=querystring)    
        print(response.text)
        

#     def viewCurrentWeek():
#         # Use the Datetime Module to look up current week and year
#         # Use your filter_holidays_by_week function to get the list of holidays 
#         # for the current week/year
#         # Use your displayHolidaysInWeek function to display the holidays in the week
#         # Ask user if they want to get the weather
#         # If yes, use your getWeather function and display results



def main():
    global holidays_dict
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
    # booty = open(locdog)
    # butt = json.load(booty)
    # print(butt)
    
    print(holidays_dict)
    # response = requests.get(apiurl, headers)
    # response = requests.request("GET", weatherurl, headers=headers, params=querystring)    
    # print(response.text)
    # for i in range(2020, 2025):
    #     year = i
    #     jholidays = scrapeHolidays(year)
    #     holidays_dict["%s holidays" % (year)] = jholidays
    # # print(holidays_dict)
    # test_file = open('json_file.json', 'w')
    # json.dump(holidays_dict, test_file, indent = 4)
    # test_file.close()

if __name__ == "__main__":
    main();


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





