import json
from datetime import date as datelib
import numpy as np


def writeJSONToFile(filename, dict):
    with open(filename, "w") as outfile:
        json.dump(dict, outfile)


def videoIsRecent(ISODate, daysFromToday):
    date = ISODate[:10]
    now_date = datelib.today().strftime("%Y/%m/%d")
    days_diff = getDaysDiff(date, now_date)
    if days_diff > daysFromToday: return False
    return True
    
def getDaysDiff(date,  now_date):
    return abs(getDays(date) - getDays(now_date))
    
def getDays(date):
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:10])
    ans = 0

    for i in range(1900, year):
        if isLeap(i):
            ans += 366
        else:
            ans += 365
        
    for i in range(1, month):
        match i:
            case 1: ans += 31
            case 2: 
                if isLeap(year): ans += 29 
                else: ans += 28
            case 3: ans += 31
            case 4: ans += 30
            case 5: ans += 31
            case 6: ans += 30
            case 7: ans += 31
            case 8: ans += 31
            case 9: ans += 30
            case 10: ans += 31
            case 11: ans += 30
            case 12: ans += 31
    ans += day - 1
    return ans
    
def isLeap(Y):
    if Y % 400 == 0:
        return True
    elif Y % 100 == 0:
        return False
    elif Y % 4 == 0:
        return True
    else:
       return False