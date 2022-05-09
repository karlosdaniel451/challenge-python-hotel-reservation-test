from . import day
from . import hotel

lakewood_hotel = hotel.get_lakewood_instance()
bridgewood_hotel = hotel.get_bridgewood_instance()
ridgewood_hotel = hotel.get_ridgewood_instance()

# For debuggin purposes.
def main():
    # print(extract_days_of_week_from_dates('Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)'))
    # print(extract_days_of_week_from_dates('Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)'))
    # print(extract_days_of_week_from_dates('Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)'))
    # print(extract_days_of_week_from_dates('(mon),foobar(tues),(thur)'))

    # for day_of_week in days_of_week:
    #     #print(day_of_week.value)
    #     print(day_of_week.is_weekday())
    pass


def get_cheapest_hotel(number: str) -> str:   # DO NOT change the function's name
    has_client_loyalty = number.startswith('Rewards')
    days_of_weeks_of_reservations = extract_days_of_week_from_dates(
        dates=number)

    total_price_for_lakewood = 0.0
    total_price_for_bridgewood = 0.0
    total_price_for_ridgewood = 0

    for day in days_of_weeks_of_reservations:
        reservation = hotel.HotelReservation(
            day_of_week=day,
            has_client_loyalty=has_client_loyalty
        )

        total_price_for_lakewood += lakewood_hotel.get_price_for_reservation(reservation)
        total_price_for_bridgewood += bridgewood_hotel.get_price_for_reservation(reservation)
        total_price_for_ridgewood += ridgewood_hotel.get_price_for_reservation(reservation)

    if total_price_for_lakewood < total_price_for_bridgewood:
        if total_price_for_lakewood < total_price_for_ridgewood:
            return lakewood_hotel.name
        else:
            return ridgewood_hotel.name
    
    if total_price_for_lakewood == total_price_for_bridgewood:
        if total_price_for_bridgewood < total_price_for_ridgewood:
            return bridgewood_hotel.name
        else:
            return ridgewood_hotel.name

    if total_price_for_bridgewood < total_price_for_ridgewood:
        return bridgewood_hotel.name

    return ridgewood_hotel.name


def extract_days_of_week_from_dates(dates: str) -> list[day.DayOfWeek]:
    """
    Extract and return the list of days of the week in `dates`
    delimited by parentheses and commas. For instance, if `dates` is
    equals to '(seg),foobar(tues),(thur)', then the returned list would
    be ['seg', 'tues', 'thur'].
    """
    extracted_days_of_week: list[day.DayOfWeek] = []

    for date in dates.split(','):
        extracted_days_of_week.append(day.DayOfWeek(date.split('(')[1].split(')')[0].upper()))

    return extracted_days_of_week

if __name__ == '__main__':
    main()
