
def leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return("Leap year")
        else:
            return("Non leap year")
    else:
        return("Non leap year")