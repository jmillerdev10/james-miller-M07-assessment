from calendar import week
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
holidays_list = []


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
    
    # def __str__ (self):
    #     # String output
    #     # Holiday output when printed.
    #     return self.name + " (" + self.date + ")" # might need to add something like the following to the end of self.date for formatting ".strftime("%Y-%m-%d")"
          
           
# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------
@dataclass
class HolidayList:
    innerHolidays: list
    

    # def __init__(self, holidayObj):
    #     self.holidayObj = holidayObj
    #     self.innerHolidays.append(holidayObj)
   
    def addHoliday(holidayObj):
        global holidays_list
        duplicate = False
        # Make sure holidayObj is an Holiday Object by checking the type
        # Use innerHolidays.append(holidayObj) to add holiday
        # print to the user that you added a holiday
        print("addHoliday UNDER CONSTRUCTION")
        # print("holidayObj type is:")
        # print(type(holidayObj))
        print('holidayObj is (56)')
        print(holidayObj)
        # print(type(holidays_list))
        
        # print("innerHolidays is: ")
        # print(innerHolidays)
        # HolidayList([holidayObj]) # not sure why it is not recognizing innerHolidays. Also tried HolidayList.innerHolidays, but that doesnt work either
        # innerHolidays.append(holidayObj)
        # print(type(holidays_list))
        for holiday in holidays_list.innerHolidays:
            if holidayObj == holiday:
                duplicate = True
                print("This holiday is 100 \'%\' duplicated. Will not append")
            elif holidayObj['name'] == holiday['name'] and holidayObj['date'] != holiday['date']:
                duplicate = True
                append_date = True
                print("This holiday is duplicated, but the date is not. Will append date")
        if duplicate:
            return
        elif append_date:

        else:
            holidays_list.innerHolidays.append(holidayObj)
        # print(holidays_list)
        # print("HolidayList is: ")
        # print(holidays_list)

#     def findHoliday(HolidayName, Date):
#         # Find Holiday in innerHolidays
#         # Return Holiday

#     def removeHoliday(HolidayName, Date):
#         # Find Holiday in innerHolidays by searching the name and date combination.
#         # remove the Holiday from innerHolidays
#         # inform user you deleted the holiday

    def read_json(filelocation):
        global holidays_list
        # Read in things from json file location
        # Use addHoliday function to add holidays to inner list.

        # print("holidays_list is: ")
        # print(type(holidays_list))
        file = open(filelocation)
        file_dict = json.load(file)
        print(type(file_dict))
        print(file_dict["holidays"])
        for holy_date in file_dict["holidays"]:
            print("holy_date is (89): ")
            print(holy_date)
            holy_date_name = holy_date["name"]
            holy_date_date = holy_date["date"]
            holyobj = Holiday(holy_date_name, holy_date_date)
            # HolidayList.addHoliday(holyobj)
            # HolidayList(holyobj)
            # print("HOlidayList = ")
            # print(HolidayList)
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

        year = 2021
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
                unformated_date = row.find('th').text
                split_uf_date = unformated_date.split()
                # print(split_uf_date[0])
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

                formatted_datetime = datetime.datetime(year, int(split_uf_date[0]), int(split_uf_date[1]))
                formatted_date = formatted_datetime.strftime('%Y-%m-%d')
                # print(formatted_date)


                holiday['date'] = formatted_date
            holidays.append(holiday)
        # print(holidays)
        for holiday in holidays:
            # print(type(holiday))
            if holiday == {}:
                holidays.remove(holiday)
            else:
        #         file_dict['holidays'].append(holiday)
        #         holy_date_name = holiday["name"]
        #         holy_date_date = holiday["date"] 
        #         holyscrapedobj = Holiday(holy_date_name, holy_date_date)
        #         # print("type(holyscrapedobj) is: ")
        #         # print(type(holyscrapedobj))
                HolidayList.addHoliday(holiday)
        print(holidays_list)

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
        weather_range = range(weekNum, 8) 
        # Convert weekNum to range between two days
        # Use Try / Except to catch problems
        # Query API for weather in that week range
        # Format weather information and return weather string.
        response = requests.request("GET", weatherurl, headers=headers, params=querystring)    
        # print(response.text)
        raw_weather = response.text
        weather_list = json.loads(raw_weather)
        # print("weather_list is: ")
        # print(weather_list['list'][0]['dt'])
        weekly_forecast = []
        for day in weather_list['list']:
            # for city in day:
            #     print(city)
            # print("day is: ")
            # print(day)

            epochTime = day['dt'] # "How do I get this from the API?"
            forecast = day['weather'][0]['main']
            # print('epochTime is: ')
            # print(epochTime)
            weather_date = datetime.datetime.fromtimestamp(epochTime).strftime('%Y-%m-%d')
            # print('formated date is: ')
            # print(weather_date)
            # print('forecast is: ')
            # print(forecast)                        
            weekly_forecast.append([weather_date, forecast])
        # print('Your weekly forecast: ')
        # print(weekly_forecast)
        # print(weather_list['list'])

        return weekly_forecast
        

#     def viewCurrentWeek():
#         # Use the Datetime Module to look up current week and year
#         # Use your filter_holidays_by_week function to get the list of holidays 
#         # for the current week/year
#         # Use your displayHolidaysInWeek function to display the holidays in the week
#         # Ask user if they want to get the weather
#         # If yes, use your getWeather function and display results



# def main():
#     global holidays_list
#     # Large Pseudo Code steps
#     # -------------------------------------
#     # 1. Initialize HolidayList Object
#     # 2. Load JSON file via HolidayList read_json function
#     # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
#     # 3. Create while loop for user to keep adding or working with the Calender
#     # 4. Display User Menu (Print the menu)
#     # 5. Take user input for their action based on Menu and check the user input for errors
#     # 6. Run appropriate method from the HolidayList object depending on what the user input is
#     # 7. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 
#     holidays_list = HolidayList(HolidayList.read_json(holidaysjson))
#     print("holidays_list is (238): ")
#     print(type(holidays_list))
#     HolidayList.scrapeHolidays(2022)
#     # scraped_list = (HolidayList.scrapeHolidays(2022))
#     # print(scraped_list)
#     for scrape in scraped_list:
#         # print("scrape is: ")
#         # print(scrape)
#         HolidayList.addHoliday(scrape)
#     print(holidays_list)
#     weather_dict = HolidayList(HolidayList.getWeather(1))
#     print('Your weekly forecast: ')
#     print(weather_dict)
#     # add_this = {'name': '', 'date': ''}
#     # print(add_this)
#     main_menu = input('\nHoliday Menu\n====================\n1. Add a Holiday\n2. Remove a Holiday\n3. Save Holiday List\n4. View Holidays\n5. Exit\n\n')
#     if main_menu == '1':
#         print("UNDER CONSTRUCTION")
#         print("\nAdd a Holiday\n====================\n")
#         hol_name = input("Holiday: ")
#         hol_date = input("Date: ")
#         add_this = {'name': hol_name, 'date': hol_date}
#         print(add_this)
#         HolidayList.addHoliday(add_this)
#         print("Success:\n%s has been added to the list" % (add_this))
#     elif main_menu == '2':
#         print("UNDER CONSTRUCTION")
#     elif main_menu == '3':
#         print("UNDER CONSTRUCTION")
#     elif main_menu == '4':
#         print("UNDER CONSTRUCTION")
#     else:
#         exit("\nExiting. See you next time!")

# if __name__ == "__main__":
#     main();


    # Read in things from json file location
    # Use addHoliday function to add holidays to inner list.

    # print("holidays_list is: ")
    # print(type(holidays_list))



def getHTML(url):
    response = requests.get(url)
    return response.text

file = open(holidaysjson)
file_dict = json.load(file)
print(type(file_dict))
print(file_dict)
print(file_dict["holidays"])
for holy_date in file_dict["holidays"]:
    print("holy_date is: ")
    print(holy_date)
    holy_date_name = holy_date["name"]
    holy_date_date = holy_date["date"]
    holyobj = Holiday(holy_date_name, holy_date_date)
    print("holyobj is: ")
    print(holyobj)
holidays_list = HolidayList(file_dict['holidays'])
print("holidays_list (306) is ")
print((holidays_list))
    # HolidayList.addHoliday(holyobj)

year = 2021
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
        unformated_date = row.find('th').text
        split_uf_date = unformated_date.split()
        # print(split_uf_date[0])
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

        formatted_datetime = datetime.datetime(year, int(split_uf_date[0]), int(split_uf_date[1]))
        formatted_date = formatted_datetime.strftime('%Y-%m-%d')
        # print(formatted_date)


        holiday['date'] = formatted_date
    holidays.append(holiday)
# print(holidays)
for holiday in holidays:
    # print(type(holiday))
    if holiday == {}:
        holidays.remove(holiday)
    else:
#         file_dict['holidays'].append(holiday)
#         holy_date_name = holiday["name"]
#         holy_date_date = holiday["date"] 
#         holyscrapedobj = Holiday(holy_date_name, holy_date_date)
#         # print("type(holyscrapedobj) is: ")
#         # print(type(holyscrapedobj))
        HolidayList.addHoliday(holiday)
print(holidays_list)
            
#             # HolidayList.addHoliday(holiday)
# print(file_dict["holidays"])
    # jholidays = {'%s holidays' % year: holidays}
    # print(Holiday(row.find('a').text, row.find('th').text))
    # holiday_object = (holiday['name'], holiday['date'])
    # print(holiday_object)
    # print([holiday['date'], holiday['name']])
    # print(row.find(class_ = 'star-rating')["class"][1])
    # print(holiday)
    # to_append = Holiday(holiday["name"], holiday['date'])
    # print("to_append type is (139): ")
    # print(type(to_append))
    # print("holidays_list type is (141)")
    # print(type(holidays_list))
    # HolidayList.addHoliday(to_append)
    # print(holidays_list)



    

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





