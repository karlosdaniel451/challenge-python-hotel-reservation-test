# For debuggin purposes.
def main():
    print(extract_days_of_week_from_dates('Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)'))
    print(extract_days_of_week_from_dates('Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)'))
    print(extract_days_of_week_from_dates('Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)'))


def get_cheapest_hotel(number: str) -> str:   #DO NOT change the function's name
    cheapest_hotel = "cheapest_hotel_name"
    return cheapest_hotel


def extract_days_of_week_from_dates(dates: str) -> list[str]:
    extracted_days_of_week: list[str] = []

    for date in dates.split(','):
        extracted_days_of_week.append(date.split('(')[1].split(')')[0])

    return extracted_days_of_week


if __name__ == '__main__':
    main()
