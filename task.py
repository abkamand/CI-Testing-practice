def my_datetime(num_sec):
    # initialize start_day, start_month, start_year
    start_day = 1
    start_month = 1
    start_year = 1970

    # convert seconds to days, 86400 seconds in a day
    days = num_sec // 86400

    # create array that represents the amount of days in a month in a yearly calendar
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # initialize month_counter and year_counter to 0
    month_counter = 0
    year_counter = 0
    # initialize leap_year_counter to 2
    leap_year_counter = 2
    # initialize normal_year days to 365 and leap_year_days to 366
    normal_year_days = 365
    leap_year_days = 366

    # convert days to years, store in year_counter
    while (days > 365):
        if leap_year_counter == 4:
            days = days - leap_year_days
            year_counter += 1
            leap_year_counter = 0
        else:
            days = days - normal_year_days
            year_counter += 1
            leap_year_counter += 1
    
    # testing output
    print("Years to add =" + str(year_counter))

    # convert leftover days to months, store in month_counter
    #while (days < 365 and days > 30):
    
    # if we landed on a leap year, set 2nd element in days_in_months to 29
    if leap_year_counter == 0:
        days_in_months[1] = 29

    for month in days_in_months:
        days = days - days_in_months[month]
        month_counter += 1 

        # break loop if we hit last month
        if days < 31:
            break
    
    # testing output
    print("Months to add =" + str(month_counter))
    
    
    # we now have our years to add, our months to add, all that remain are days
    # add our counters to our start variables for days, months, years
    final_day = start_day + days
    final_month = start_month + month_counter
    final_year = start_year + year_counter

    # testing output
    print("Unformatted Date =" + str(final_month) + "-" + str(final_day) + "-" + str(final_year))

    # convert our integers into MM-DD-YYYY string format
    string_day = ""
    string_month = ""
    string_year = str(final_year)

    if final_day > 1 and final_day < 10:
        string_day = "0" + str(final_day)
    
    if final_month > 1 and final_month < 10:
        string_month = "0" + str(final_month)
    
    return "Final, formatted date: " + string_month + "-" + string_day + "-" + string_year 

# basic input testing
print(my_datetime(0))
print(my_datetime(123456789))
