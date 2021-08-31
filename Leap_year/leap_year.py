
def leap_year():
    print ("Enter a year:", end=" ")
    year=int(input())
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            print("Leap year")
        else:
            print("Non leap year")
    else:
        print("Non leap year")
leap_year()