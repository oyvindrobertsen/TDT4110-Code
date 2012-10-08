def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True

    return False

def weekday_newyear(year):

    days = 0
    rng = range(1900,(year))

    for i in rng:
        if is_leap_year(i) == True:
            days = days + 366
        else:
            days = days + 365

    day_of_week = days % 7

    return day_of_week

def is_workday(weekday):
    if 0 <= weekday < 5:
        return True
    else:
        return False

def workdays_in_year(year):
    workdays = 0
    day_range = [weekday_newyear(year)]


    if is_leap_year(year) == True:
        for i in range(1,366):
            if day_range[i - 1] == 6:
                day_range.append(0)
            else:
                day_range.append(day_range[i - 1] + 1)
    else:
        for i in range(1,365):
            if day_range[i - 1] == 6:
                day_range.append(0)
            else:
                day_range.append(day_range[i - 1] + 1)

    for x in range(0,len(day_range)):
        if is_workday(day_range[x]) == True:
            workdays = workdays + 1
        else:
            pass

    return workdays

def main():
    years = range(1900,1920)
    day_table = ['man','tir','ons','tor','fre','lør','søn']
    for i in years:
        j = weekday_newyear(i)

        print(i, day_table[j])

    print('============================')

    for i in years:
        j = workdays_in_year(i)

        print(i ,'har', j ,'arbeidsdager')


main()
