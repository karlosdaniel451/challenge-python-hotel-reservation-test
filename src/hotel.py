from dataclasses import dataclass

from . import day


@dataclass
class HotelReservation:
    day_of_week: day.DayOfWeek
    has_client_loyalty : bool
    

@dataclass
class Hotel:
    name: str
    rating: int
    price_for_weekend_with_loyalty: float
    price_for_weekday_without_loyalty: float
    price_for_weekday_with_loyalty: float
    price_for_weekend_without_loyalty: float

    def get_price_for_reservation(self, reservation: HotelReservation) -> float:
        """
        Calculate and return the price for a given reservation, considering
        whether the client has loyalty or not and whether it is in a weekday
        or in weekend.
        """
        if reservation.day_of_week.is_weekday():
            if reservation.has_client_loyalty:
                # If reservation is for weekday and client is loyal.
                return self.price_for_weekday_with_loyalty
            # If reservation is for weekday and client is not loyal.
            return self.price_for_weekday_without_loyalty

        # If reseservation is for weekend and client is loyal.
        if reservation.has_client_loyalty:
            return self.price_for_weekend_with_loyalty
        
        # If reservation is for weekend and client is not loyal.
        return self.price_for_weekend_without_loyalty



def get_lakewood_instance() -> Hotel:
    return Hotel(
        name='Lakewood',
        rating=3,
        price_for_weekday_without_loyalty=110,
        price_for_weekday_with_loyalty=80,
        price_for_weekend_without_loyalty=90,
        price_for_weekend_with_loyalty=80
    )

def get_bridgewood_instance() -> Hotel:
    return Hotel(
        name='Bridgewood',
        rating=4,
        price_for_weekday_without_loyalty=160,
        price_for_weekday_with_loyalty=110,
        price_for_weekend_without_loyalty=60,
        price_for_weekend_with_loyalty=50
    )

def get_ridgewood_instance() -> Hotel:
    return Hotel(
        name='Ridgewood',
        rating=5,
        price_for_weekday_without_loyalty=220,
        price_for_weekday_with_loyalty=100,
        price_for_weekend_without_loyalty=150,
        price_for_weekend_with_loyalty=40
    )
