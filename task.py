def my_datetime(num_sec):
    # convert seconds to days, 86400 seconds in a day
    days = num_sec // 86400

    # create array that represents the amount of days in a month in a yearly calendar
    days_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # initialize leap_year_counter to 2 since we start at 1970
    leap_year_counter = 2
    # initialize normal_year days to 365 and leap_year_days to 366
    normal_year_days = 365
    leap_year_days = 366

    #initialize current_year to 1970, current_month to 1
    current_year = 1970
    current_month = 1

    # convert days to years, update current_year
    while (leap_year_counter == 4 and days > 366) or (leap_year_counter != 4 and days > 365):
        # if we're in a leap year
        if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
            days = days - leap_year_days
            leap_year_counter = 1
        # not a leap year
        else:
            days = days - normal_year_days
            leap_year_counter += 1
        
        current_year +=1
    
    # testing output
    #print("Current Year =" + str(current_year))
    
    # if we landed on a leap year, set 2nd element in days_months to 29
    if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
        days_months[1] = 29

    for month in days_months:
        # break loop if we hit last month
        if days <= month:
            break
        else:
            days = days - month
            current_month += 1

    # finally, get our current_day
    current_day = days + 1

    # testing output
    #print("Current Month =" + str(current_month))

    # testing output
    #print("Unformatted Date =" + str(current_month) + "-" + str(days) + "-" + str(current_year))

    # convert our integers into MM-DD-YYYY string format
    string_day = ""
    string_month = ""
    string_year = str(current_year)

    if current_day > 1 and current_day < 10:
        string_day = "0" + str(current_day)
    else:
        string_day = str(current_day)
    
    if current_month > 1 and current_month < 10:
        string_month = "0" + str(current_month)
    else:
        string_month = str(current_month)
    
    return "Final, formatted date: " + string_month + "-" + string_day + "-" + string_year 