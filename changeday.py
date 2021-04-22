# write a python program to get next day of a given date using if elif else

#finding out leap year 

def isleapyear(year): 
        if (year % 400 == 0):
                leap_year = True
        elif (year % 100 == 0):
                leap_year = False
        elif (year % 4 == 0):
                leap_year = True
        else:
               leap_year = False
        return leap_year       

#month = int(input("Input a month [1-12]: "))




def findmonthlength(month,year): 
                 leap_year=isleapyear(year)
                 month_list=(1, 3, 5, 7, 8, 10, 12) # months having 31 days 
                 if month in month_list:
                             month_length = 31 
                 elif month == 2:
                          if leap_year:
                                    month_length = 29
                          else:
                                  month_length = 28
                 else:
                       month_length = 30
                 return month_length      





def nextdate(day,month,year):
          month_length=findmonthlength(month,year)
          if day < month_length:
                  day += 1
          else:
                 day = 1
                 if month == 12:
                        month = 1
                        year += 1
                 else:
                        month += 1
          return day,month,year



if __name__=="__main__" : 
           date=input("enter a date ")

           date=date.split("-")
           day=int(date[0])
           month=int(date[1])
           year=int(date[2])
            
           next_day,next_month,next_year= nextdate(day,month,year)

           print("The next date is [dd-mm-yyyy] %d-%d-%d." % (next_day, next_month, next_year))




        
            
                  
