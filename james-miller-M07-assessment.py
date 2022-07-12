from datetime import datetime
import json
from bs4 import BeautifulSoup
import requests
from config import holidaysjson


# The Holiday class defines Holiday objects to be used in the HolidayList class
class Holiday:
      
    # Holiday object constructor
    def __init__(self, name, date):
        self.name = name        
        self.date = datetime.strptime(date, '%Y-%m-%d')
    
    # String output for when Holiday is printed.
    def __str__ (self):
        return self.name + " (" + self.date.strftime("%Y-%m-%d") + ")"
          
           
# -------------------------------------------
# The HolidayList class acts as a wrapper and container for the list of holidays
# --------------------------------------------
class HolidayList:
    def __init__(self):
       self.innerHolidays = []
   
    def addHoliday(self, holidayObj):
        # Makes sure holidayObj is a Holiday Object by checking the type
        # Uses innerHolidays.append(holidayObj) to add holiday
        # Prints to the user that a holiday has been added
        if isinstance(holidayObj, Holiday):
            found_holiday = self.findHoliday(holidayObj.name, holidayObj.date.strftime("%Y-%m-%d")) 
            if isinstance(found_holiday, Holiday):
                print("\nOops! The holiday indicated has already been added.")
            else:
                self.innerHolidays.append(holidayObj)
                print("\nSuccess:")
                print("%s has been added to the holiday list." % holidayObj)
        else:
            raise ValueError()

    def findHoliday(self, HolidayName, Date):
        # Searches for the specified Holiday object in innerHolidays
        # Returns the Holiday object to the calling function 
        for holiday in self.innerHolidays:
            if holiday.name == HolidayName and holiday.date.strftime("%Y-%m-%d") == Date:
                return holiday

    def removeHoliday(self, HolidayName, Date):
        # Finds the specified Holiday object in innerHolidays by searching the name/date combination
        # Removes the Holiday from innerHolidays
        # Informs user that the Holiday object has been deleted
        hol_to_remove = self.findHoliday(HolidayName, Date)
        dummylist = list(self.innerHolidays)
        print(len(dummylist))
        if isinstance(hol_to_remove, Holiday):
            dummylist.remove(hol_to_remove)
            print("\nSuccess:")
            print("%s has been removed from the holiday list." % (HolidayName))
        else:
            print("\nThat holiday is already not in the list")
        # print(len(dummylist))
        self.innerHolidays = dummylist
        # print(len(self.innerHolidays))

    def read_json(self, filelocation):
        # Reads in itemss from the specified json file location
        # Creates Holiday objects
        # Calls the addHoliday function to add Holiday objects to inner list.
        file = open(filelocation)
        table = json.load(file)
        # print(type(table))
        # print(table["holidays"])
        for row in table["holidays"]:
            holiday_name = row["name"]
            holiday_date = row["date"]
            a_holiday = Holiday(holiday_name, holiday_date)
            # print(a_holiday)
            self.addHoliday(a_holiday)

    def save_to_json(self, filelocation):
        # Converts each Holiday object into a dictionary-like structure.
        # Adds the Holiday dictionary structures to a list, then adds that list to a dictionary
        # Converts the dictionary to json format and writes the json text to specified json file, 
        #       which is stored in and imported from the config.py file.
        saving_dict = {"holidays" : []}
        saving_holiday = {}
        
        for holiday in self.innerHolidays:
            saving_holiday = {"name": holiday.name, "date": holiday.date.strftime("%Y-%m-%d")}
            # print(saving_holiday)
            saving_dict["holidays"].append(saving_holiday)

        saving_json = json.dumps(saving_dict, indent=4)
        # print(saving_json)

        f = open(filelocation,"w")
        # print("file opened")
        f.write(f"{saving_json}")
        print("\nChanges saved!")
        f.close()
        
    def getHTML(url):
        # Makes the connection to the specified web page for scraping
            response = requests.get(url)
            return response.text

    def scrapeHolidays(self):
        # Scrapes holidays from specified web page (https://www.timeanddate.com/holidays/us/) 
        # Gets the holidays from current year, plus the 2 prior and 2 future years, 
        #   and converts them to holiday objects. Years are currently hard-coded.
        # Checks if name and date of Holiday obj are already in innerHolidays to avoid duplicate holidays
        # Adds non-duplicates to innerHolidays using the addHoliday() function
        years = [2020, 2021, 2022, 2023, 2024]
        for year in years:
            html = HolidayList.getHTML("https://www.timeanddate.com/holidays/us/%s?hol=33554809" % (year))
            soup = BeautifulSoup(html,'html.parser')

            table = soup.find('tbody').find_all('tr', attrs= {"class": "showrow"})
            # print(list(table))

            for row in table:
                holiday_name = ''
                split_uf_date = []
                # title = row.find('img')
                if row.find('a') is not None:
                    # print(row.find('a').text)
                    holiday_name = row.find('a').text
                    # print(holiday_name)
                
                if row.find('th') is not None:
                    # print(row.find('th').text)
                    unformatted_date = row.find('th').text
                    split_uf_date = unformatted_date.split()
                    # print(split_uf_date)
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
                # print("a_holiday is: ")
                # print(a_holiday)
                self.addHoliday(a_holiday)

    def numHolidays(self):
        # Returns the total number of Holiday objects in innerHolidays
        return len(self.innerHolidays)
    
    def filter_holidays_by_week(self, year, week_number):
        # Uses a Lambda function to filter by week number and save this as holidays
        # Uses the filter on innerHolidays to get holidays only for the year and week specified
        # Returns a filtered list of Holiday objects
        holidays = []

        if(not (isinstance(week_number, int))):
            raise ValueError()
        
        if(not (isinstance(year, int))):
            raise ValueError()
        
        holidays = list(filter(lambda holiday: holiday.date.isocalendar()[0] == year and
                          holiday.date.isocalendar()[1] == week_number, self.innerHolidays))
        
        return holidays
        
    def displayHolidaysInWeek(self, holidayList):
        # Uses the list from filter_holidays_by_week to display the list of Holiday objects
        year = holidayList[0].date.isocalendar()[0]
        week = holidayList[0].date.isocalendar()[1]
        if len(holidayList) == 0:
            print("\nThere are no holidays in week #%s of %s." % (week, year))
        else:
            # year = holidayList[0].date.isocalendar()[0]
            # week = holidayList[0].date.isocalendar()[1]
            print("\nThese are the holidays for {} week #{}: ".format(year, week))
            for holiday in holidayList:
                print(holiday)
        

    # def getWeather(weekNum):
    #     # Convert weekNum to range between two days
    #     # Use Try / Except to catch problems
    #     # Query API for weather in that week range
    #     # Format weather information and return weather string.

    def viewCurrentWeek(self):
        # Uses the Datetime Module to look up current week and year
        # Uses the list from filter_holidays_by_week() 
        # Calls to displayHolidaysInWeek() function to display the holidays in the week
        # Will eventually ask user if they want to get the weather
        # If user wants the weather, will make call to getWeather() and display the results
        # print("\nYou are in viewCurrentWeek. UNDER CONSTRUCTION!\n")
        week = datetime.now().isocalendar()[1]
        year = datetime.now().isocalendar()[0]
        self.displayHolidaysInWeek(self.filter_holidays_by_week(year, week))
        # displayHolidaysInWeek(self, holidayList)


def main():
    # 1. Initializes HolidayList Object
    # 2. Loads JSON file via HolidayList read_json() function
    # 3. Scrapes additional holidays using the HolidayList scrapeHolidays() function.
    # 3. Creates a while loop for user to keep working with the application
    # 4. Displays User Menu and waits for user input to determine what to do next
    # 5. Runs appropriate method from the HolidayList object depending on what the user input is
    # 6. Asks the User if they would like to continue
    #       if yes, displays the menu again and waits for user input
    #       if not, ends the while loop, terminating the application. 
    hl = HolidayList()
    hl.read_json(holidaysjson)
    hl.scrapeHolidays()

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
            hl.addHoliday(add_this)
            # print("\nSuccess:\n%s has been added to the list" % (add_this))
            unsaved_changes = True
            do_more = input("\nWould you like to return to the Holiday Menu or exit the application [menu/exit]: ")
            if do_more == 'exit':
                if unsaved_changes:
                    y_n =  input("\nAre you sure you want to exit?\nYour changes will be lost\n[y/n]: ")
                    if y_n == 'y':
                        exit("\nExiting. See you next time!")
                else:
                    y_n = input("\nAre you sure you want to exit? [y/n]: ")
                    if y_n == 'y':
                        exit("\nExiting. See you next time!")
            elif do_more == 'menu': 
                keep_going = True
                pass
        elif main_menu == '2':
            # This is the Remove a Holiday option
            print("\nRemove a Holiday\n====================\n")
            holiday_name = input("\nHoliday Name: ")
            holiday_date = input("Holiday Date: ")
            hl.removeHoliday(holiday_name, holiday_date)
            unsaved_changes = True
            do_more = input("\nWould you like to return to the Holiday Menu or exit the application [menu/exit]: ")
            if do_more == 'exit':
                if unsaved_changes:
                    y_n =  input("\nAre you sure you want to exit?\nYour changes will be lost\n[y/n]: ")
                    if y_n == 'y':
                        exit("\nExiting. See you next time!")
                else:
                    y_n = input("\nAre you sure you want to exit? [y/n]: ")
                    if y_n == 'y':
                        exit("\nExiting. See you next time!")
            elif do_more == 'menu': 
                keep_going = True
                pass
        elif main_menu == '3':
            # This is the save_to_json option
            print("\nSaving Holiday List\n====================\n")
            confirm_save = input("Are you sure you want to save your changes? [y/n]: ")
            if confirm_save == 'y':
                hl.save_to_json(holidaysjson)
                do_more = input("\nWould you like to return to the Holiday Menu or exit the application [menu/exit]: ")
                unsaved_changes = False
                if do_more == 'exit':
                    y_n = input("\nAre you sure you want to exit? [y/n]: ")
                    if y_n == 'y':
                        keep_going = False
                        exit("\nExiting. See you next time!")
                elif do_more == 'menu': 
                    keep_going = True
                    pass
            elif confirm_save == 'n':
                print("\nCanceled:\nHoliday list file save canceled.")
                do_more = input("\nWould you like to return to the Holiday Menu or exit the application [menu/exit]: ")
                unsaved_changes = True
                if do_more == 'exit':
                    if unsaved_changes:
                        y_n =  input("\nAre you sure you want to exit?\nYour changes will be lost\n[y/n]: ")
                        if y_n == 'y':
                            exit("\nExiting. See you next time!")
                    else:
                        y_n = input("\nAre you sure you want to exit? [y/n]: ")
                        if y_n == 'y':
                            exit("\nExiting. See you next time!")
                elif do_more == 'menu': 
                    keep_going = True
                    pass
        elif main_menu == '4':
            # This is the View Holiday option            
            print("\nView Holidays\n====================\n")
            wrong_input = True
            while(wrong_input):
                try:
                    year = int(input("\nWhich year?: "))
                    week = (input("Which week? #[1-52 (1-53 for year 2020), Leave blank for the current week]: "))
                    
                    if week != "":
                        if(int(week) <= 53 and int(week) >= 1):
                            wrong_input = False
                            week = int(week)
                            filtered_holidays = (hl.filter_holidays_by_week(year, week))
                            if(len(filtered_holidays) == 0):
                                print("\nThere are no holidays in week #%s of %s." % (week, year))
                            else: 
                                hl.displayHolidaysInWeek(filtered_holidays)
                        else:
                            print("\nOops! Your input is outside of the expected range. Please try again: ")
                    else:
                        hl.viewCurrentWeek()
                        wrong_input = False
                except:    
                    print("\nOops! You either entered incorrect information or the week entered does not exist in the year specified")
            do_more = input("\nWould you like to return to the Holiday Menu or exit the application [menu/exit]: ")
            if do_more == 'exit':
                if unsaved_changes:
                    y_n =  input("\nAre you sure you want to exit?\nYour changes will be lost\n[y/n]: ")
                    if y_n == 'y':
                        exit("\nExiting. See you next time!")
                else:
                    y_n = input("\nAre you sure you want to exit? [y/n]: ")
                    if y_n == 'y':
                        exit("\nExiting. See you next time!")
            elif do_more == 'menu': 
                keep_going = True
                pass    
        elif main_menu == '5':
            # This closes the application
            print("\nExit\n====================\n")
            if unsaved_changes:
                y_n =  input("\nAre you sure you want to exit?\nYour changes will be lost\n[y/n]: ")
                if y_n == 'y':
                    exit("\nExiting. See you next time!")
            else:
                y_n = input("\nAre you sure you want to exit? [y/n]: ")
                if y_n == 'y':
                    exit("\nExiting. See you next time!")
            
if __name__ == "__main__":
    main()


# Sticking this stuff at the bottom of the file to salvage from for the weather API stuff, in
# case I get ambitious later...
    # weather_dict = HolidayList(HolidayList.getWeather(1))
    # print('Your weekly forecast: ')
    # print(weather_dict)

# The following would be for the actual function, whereas the above has to do with calling the function
    # def getWeather(weekNum):
    #         weather_range = range(weekNum, 8) 
    #         # Convert weekNum to range between two days
    #         # Use Try / Except to catch problems
    #         # Query API for weather in that week range
    #         # Format weather information and return weather string.
    #         response = requests.request("GET", weatherurl, headers=headers, params=querystring)    
    #         # print(response.text)
    #         raw_weather = response.text
    #         weather_list = json.loads(raw_weather)
    #         # print("weather_list is: ")
    #         # print(weather_list['list'][0]['dt'])
    #         weekly_forecast = []
    #         for day in weather_list['list']:
    #             # for city in day:
    #             #     print(city)
    #             # print("day is: ")
    #             # print(day)

    #             epochTime = day['dt'] # "How do I get this from the API?"
    #             forecast = day['weather'][0]['main']
    #             # print('epochTime is: ')
    #             # print(epochTime)
    #             weather_date = datetime.datetime.fromtimestamp(epochTime).strftime('%Y-%m-%d')
    #             # print('formated date is: ')
    #             # print(weather_date)
    #             # print('forecast is: ')
    #             # print(forecast)                        
    #             weekly_forecast.append([weather_date, forecast])
    #         # print('Your weekly forecast: ')
    #         # print(weekly_forecast)
    #         # print(weather_list['list'])

    #         return weekly_forecast