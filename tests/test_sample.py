from unittest import TestCase

from context import src
from src.my_module import get_cheapest_hotel

class MyTest(TestCase):
    def test1(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"))

    def test2(self):
        result = "Bridgewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"))

    def test3(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"))

    def test4(self):
        """
        In this test case, the total price for each hotel is:\n
        R$200 for Lakewood\n
        R$220 for Bridgewood\n
        R$370 for Ridgewood\n
        Thus, the cheapest hotel should be Ridgewood.
        """
        date_sequence = 'Regular: 08May2022(sun), 09May2022(mon)'

        expected_result = 'Lakewood'
        actual_result = get_cheapest_hotel(date_sequence)

        self.assertEqual(expected_result, actual_result)

    def test5(self):
        """
        In this test case, the total price for each hotel is:\n
        R$180 for Lakewood\n
        R$120 for Bridgwood\n
        R$300 for Ridgewood\n
        Thus, the cheapest hotel should be Bridgwood.
        """
        date_sequence = 'Regular: 07May2022(sat), 08May2022(sun)'

        expected_result = 'Bridgewood'
        actual_result = get_cheapest_hotel(date_sequence)

        self.assertEqual(expected_result, actual_result)

    def test6(self):
        """
        In this test case, the total price for each hotel is:\n
        R$160 for Lakewood\n
        R$160 for Bridgewood\n
        R$140 for Ridgewood\n
        Thus, the cheapest hotel should be Ridgewood.
        """
        date_sequence = 'Rewards: 08May2022(sun), 09May2022(mon)'

        expected_result = 'Ridgewood'
        actual_result = get_cheapest_hotel(date_sequence)

        self.assertEqual(expected_result, actual_result)
