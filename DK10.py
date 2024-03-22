months_and_days = {
    "1": 31,       # January
    "2": 28,       # February (29 in leap years)
    "3": 31,       # March
    "4": 30,       # April
    "5": 31,       # May
    "6": 30,       # June
    "7": 31,       # July
    "8": 31,       # August
    "9": 30,       # September
    "10": 31,      # October
    "11": 30,      # November
    "12": 31       # December
}


def leap_year(year):
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    return True


if __name__ == '__main__':
    arg = input().split()
    month = arg[0]
    year = int(arg[1])
    if year <= 0 or int(month) not in range(1, 12):
        print("INVALID")
    else:
        if month == "2" and leap_year(year):
            print(29)
        else:
            print(months_and_days[month])
