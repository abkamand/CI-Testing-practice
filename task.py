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

    while (days > 365):
        if leap_year_counter == 4:
            days = days - leap_year_days
            year_counter += 1
            leap_year_counter = 0
        else:
            days = days - normal_year_days
            year_counter += 1
            leap_year_counter += 1
