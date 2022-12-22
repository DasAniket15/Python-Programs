"""
The metric system of time, originally introduced in the 1790s, during the French
Revolution, was a way to reform their inconsistent, unwieldy, and archaic system of
many time. Ultimately this system was abolished by the end of the revolution. This
program converts the conventional date and time to the decimal equivalent.
"""

#Defining variables
hour = hourDec = min = minDec = sec = secDec = totSec = yearRev =  décade =  0
monthRev = gregorian_datetime = ""


def get_decimal_time(hour: int, min: int, sec: int):
    """
    Accepts values for conventional hour, minute, and second, then converts it into decimal equivalent
    """

    #Converting total time into seconds
    totSec = (hour * 3600) + (min * 60) + (sec)

    #Converting total seconds into decimal hours, minutes, and seconds
    hourDec = int(totSec // 10000)
    minDec = int((totSec - (hourDec * 10000)) // 100)
    secDec = int(totSec - (hourDec * 10000 + minDec * 100))

    #Printing time in decimal format
    print(f"{hourDec}:{minDec}:{secDec}")


def get_decimal_date(month: int, date: int, year: int):
    """
    Accepts values of conventional mm/dd/yyyy date, and converts to French Revolutionary equivalent
    """

    #Declaring local variables
    décade = 0
    monthRev = ""

    #Converting year to French Revolution equivalent
    yearRev = year - 1792

    #Checking for which Décade
    if (date >= 1 and date <= 10):
        décade = 1

    elif (date >= 11 and date <= 20):
        décade = 2

    elif (date >= 21 and date <= 30):
        décade = 3

    #Checking for which month
    if (month == 1):
        monthRev = "Nivôse"

    elif (month == 2):
        monthRev = "Pluviôse"

    elif (month == 3):
        monthRev = "Ventôse"

    elif (month == 4):
        monthRev = "Germinal"

    elif (month == 5):
        monthRev = "Floréal"

    elif (month == 6):
        monthRev = "Prairial"

    elif (month == 7):
        monthRev = "Messidor"

    elif (month == 8):
        monthRev = "Thermidor"

    elif (month == 9):
        monthRev = "Fructidor"

    elif (month == 10):
        monthRev = "Vendémiaire"

    elif (month == 11):
        monthRev = "Brumaire"

    elif (month == 12):
        monthRev = "Frimaire"

    #Printing date in French Revolutionary format
    print(f"{date} {monthRev} Year {yearRev}, Décade {décade}")


def get_french_datetime(gregorian_datetime: str):
    """
    Takes user input and converts, then returns French Revolutionary equivalent
    """

    #Taking input
    gregorian_datetime = input("gregorian_datetime = ")

    #Checking the format of the date and time inputted by user (location of the : characters)
    result1 = gregorian_datetime.find(":")
    hour = int(gregorian_datetime[0 : result1])

    result2 = gregorian_datetime.find(":", result1 + 1)
    min = int(gregorian_datetime[result1 + 1 : result2])

    result3 = gregorian_datetime.find(" ", result2 + 1)
    sec = int(gregorian_datetime[result2 + 1 : result3])

    result4 = gregorian_datetime.find("/", result3 + 1)
    month = int(gregorian_datetime[result3 + 1 : result4])

    result5 = gregorian_datetime.find("/", result4 + 1)
    date = int(gregorian_datetime[result4 + 1 : result5])

    year = int(gregorian_datetime[result5 + 1 : ])

    get_decimal_time(hour, min, sec)
    get_decimal_date(month, date, year)


def main():
    get_french_datetime(gregorian_datetime)


main()